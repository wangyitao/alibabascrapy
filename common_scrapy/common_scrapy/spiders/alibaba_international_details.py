# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from common_scrapy.items import AlibabaInternationalItem
import re
from bs4 import BeautifulSoup
import requests
from pyquery import PyQuery as pq
import re
from common_scrapy.items import AlibabaInternationalProductsDetailsItem, AlibabaInternationalCompanyProfileItem
import json


class AlibabaInternationalDetailsSpider(scrapy.Spider):
    name = 'alibaba_international_details'
    allowed_domains = ['alibaba.com']
    start_urls = ['http://alibaba.com/']

    start_url = 'https://www.alibaba.com/products/3D_Wall_Panel/{}.html'

    ## 如果需要调用selenium添加
    def __init__(self):
        # 创建chrome参数对象
        opt = webdriver.ChromeOptions()
        # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
        opt.set_headless()
        # 创建chrome无界面对象
        self.browser = webdriver.Chrome(options=opt)
        self.browser.implicitly_wait(30)  # 隐性等待，最长等30秒
        super(AlibabaInternationalDetailsSpider, self).__init__()
        dispatcher.connect(self.closeSpider, signals.spider_closed)

    def closeSpider(self, spider):
        print("spider closed")
        # 当爬虫退出的时关闭浏览器
        self.browser.close()

    # 第一次访问的方法重写
    def start_requests(self):
        """
        这里重写了start_requests方法，分别请求了用户查询的url和关注列表的查询以及粉丝列表信息查询
        :return:
        """
        for i in range(10, 11):  # 101
            yield scrapy.Request(self.start_url.format(str(i)), callback=self.parse)

    def parse(self, response):

        doc = pq(str(response.text))
        try:
            a = doc('.title').items()

            for i in a:
                aa = i.find('a').attr('href')
                patten = re.compile('.*?www.alibaba.com/product-detail.*')
                p = patten.findall(str(aa))
                if p:
                    # print(''.join(['http:', p[0]]))
                    detail_url = ''.join(['http:', p[0]])
                    yield scrapy.Request(url=detail_url, meta={'detail_url': detail_url}, callback=self.detail_parse)
        except Exception as e:
            with open('loggers.txt', 'a', encoding='utf8') as f:
                f.write('65行出错' + str(e) + '\n\n')
        print('parse############################################')

    def detail_parse(self, response):
        detail_url = response.meta['detail_url']
        doc = pq(str(response.text))
        try:
            company_name = doc('.name-text').text()
            company_link = doc('.company-link').attr('href')
            company_profile_link = ''.join([str(company_link), 'company_profile.html'])
            all_products_first_url = ''.join([str(company_link), 'productlist-1.html'])
            new_products_first_url = ''.join([str(company_link), 'productlist-1.html?scene=ws&filter=new'])
            hot_products_first_url = ''.join([str(company_link), 'productlist-1.html?scene=ws&filter=hot'])
            data = {'company_name': company_name, 'company_link': company_link,
                    'company_profile_link': company_profile_link, 'all_products_first_url': all_products_first_url
                , 'new_products_first_url': new_products_first_url, 'hot_products_first_url': hot_products_first_url}

            print(company_name)
            print(company_link)
            print(company_profile_link)
            print(all_products_first_url)
            print(new_products_first_url)
            print(hot_products_first_url)
            # with open('信息.txt', 'a', encoding='utf8') as f:
            #     ddd = 'detail_url:' + detail_url + '\n' + 'company_name:' + company_name + '\n' + 'company_link:' + company_link + '\n' + 'company_detailss_link:' + company_detailss_link + '\n\n\n'
            #     f.write(ddd)
            yield scrapy.Request(url=company_profile_link, meta={'data': data}, callback=self.company_profile_parse)
            yield scrapy.Request(url=new_products_first_url, meta={'data': data, 'flag': 'new'},
                                 callback=self.all_new_hot_page_parse)
            yield scrapy.Request(url=hot_products_first_url, meta={'data': data, 'flag': 'hot'},
                                 callback=self.all_new_hot_page_parse)
            yield scrapy.Request(url=all_products_first_url, meta={'data': data, 'flag': 'all'},
                                 callback=self.all_new_hot_page_parse)
        except Exception as e1:
            with open('loggers.txt', 'a', encoding='utf8') as f:
                f.write('102行出错' + str(e1) + '\n\n')
        # print(response)
        print('detail_parse#################################')

    def all_new_hot_page_parse(self, response):
        data = response.meta['data']
        flag = response.meta['flag']

        if flag == 'all':
            print('all##################################')
            try:
                doc = pq(str(response.text))
                p = doc('.ui-label').text()
                all_page = int(re.findall('of.*?(\d+).*?Page', str(p))[0])
                for page in range(1, all_page + 1):
                    all_products_url = ''.join([str(data['company_link']), 'productlist-{}.html']).format(page)
                    yield scrapy.Request(url=all_products_url, meta={'data': data, 'flag': flag},
                                         callback=self.company_productlist_parse)
            except Exception as e:
                print('all_page_error', e)

        if flag == 'new':
            print('new###########################')
            try:
                doc = pq(str(response.text))
                p = doc('.ui-label').text()
                all_page = int(re.findall('of.*?(\d+).*?Page', str(p))[0])
                for page in range(1, all_page + 1):
                    all_products_url = ''.join(
                        [str(data['company_link']), 'productlist-{}.html?scene=ws&filter=new']).format(page)
                    yield scrapy.Request(url=all_products_url, meta={'data': data, 'flag': flag},
                                         callback=self.company_productlist_parse)
            except Exception as e:
                print('new_page_error', e)

        if flag == 'hot':
            print('hot################################')
            try:
                doc = pq(str(response.text))
                p = doc('.ui-label').text()
                all_page = int(re.findall('of.*?(\d+).*?Page', str(p))[0])
                for page in range(1, all_page + 1):
                    all_products_url = ''.join(
                        [str(data['company_link']), 'productlist-{}.html?scene=ws&filter=hot']).format(page)
                    yield scrapy.Request(url=all_products_url, meta={'data': data, 'flag': flag},
                                         callback=self.company_productlist_parse)
            except Exception as e:
                print('hot_page_error', e)
        print('all_new_hot_page_parse###################################################')

    def company_profile_parse(self, response):
        item = AlibabaInternationalCompanyProfileItem()
        doc = pq(response.text)
        data = response.meta['data']
        dd = str(doc('.content-table'))
        soup = BeautifulSoup(dd, 'lxml')
        sss = soup.find_all('tr')
        # print(sss)

        ################获取基本信息
        company_data = {}
        for iii in sss:
            #     aaa=iii[0].get('data-role')
            #     print(aaa)
            try:
                patten = re.compile('<.*?>', re.S)
                key = iii.attrs['data-role']
                print(iii.attrs['data-role'])
                ppp = str(iii.find_all('td')[0]).strip()
                value = patten.sub('', ppp).strip().replace('\n', ' ').replace('  ', ' ')
                print(patten.sub('', ppp).strip().replace('\n', ' ').replace('  ', ' '))
                company_data[key] = value
                print('####################################')
            except Exception as e:
                print('没有找到键值对', e)

        #######################获取市场信息
        ee = str(doc('.widget-supplier-trade-market .ui2-table'))
        # print(ee)
        soup2 = BeautifulSoup(ee, 'lxml')
        ssss = soup2.find_all('tr')
        # print(ssss)
        markets = {}
        for iiii in ssss[1:]:
            try:
                patten2 = re.compile('<.*?>', re.S)
                market = patten2.sub('', str(iiii)).strip().split('\n')
                markets[market[0].replace(' ', '')] = ' '.join(market[1:])
                # print(market)
                # print()
            except Exception as e:
                print('没有找到键值对', e)

        data['company_data'] = company_data
        data['markets'] = markets
        item['company_data'] = company_data
        item['markets'] = markets
        item['company_name'] = data['company_name']
        item['company_link'] = data['company_link']
        item['flag'] = 'profile'

        with open('公司基本信息包括市场.json', 'a', encoding='utf8')as f:
            json.dump(data, f)
        print('company_profile_parse########################')
        print(data)
        yield item

    def company_productlist_parse(self, response):
        item = AlibabaInternationalProductsDetailsItem()
        data = response.meta['data']
        flag = response.meta['flag']

        doc = pq(response.text)
        view = doc('.app-productsGalleryView')
        soup = BeautifulSoup(str(view), 'lxml')
        li = soup.find_all('li')
        for i in li:
            try:
                datas = {}
                product_img_url = ''.join(['http:', i.find_all('img')[0].attrs['src']])
                product_title = i.find_all(attrs={'class': 'product-title'})[0].find_all('a')[0].get_text().strip()
                product_detail_url = ''.join([data['company_link'],
                                              i.find_all(attrs={'class': 'product-title'})[0].find_all('a')[0].attrs[
                                                  'href'].strip()[1:]])
                product_min_order = i.find_all(attrs={'class': 'product-order-info'})[0].get_text().strip()
                product_price = i.find_all(attrs={'class': 'product-order-info'})[1].get_text().strip()

                item['flag'] = flag
                item['company_name'] = data['company_name']
                item['company_link'] = data['company_link']
                item['product_img_url'] = product_img_url
                item['product_title'] = product_title
                item['product_detail_url'] = product_detail_url
                item['product_min_order'] = product_min_order
                item['product_price'] = product_price

                datas['flag'] = flag
                datas['company_name'] = data['company_name']
                datas['company_link'] = data['company_link']
                datas['product_img_url'] = product_img_url
                datas['product_title'] = product_title
                datas['product_detail_url'] = product_detail_url
                datas['product_min_order'] = product_min_order
                datas['product_price'] = product_price
                with open('公司产品基本信息.json', 'a', encoding='utf8')as f:
                    json.dump(datas, f)
                print('company_productlist_parse######################')
                print(datas)
                yield item
            except Exception as e:
                with open('loggers.txt', 'a', encoding='utf8') as f:
                    f.write('242行出错' + str(e) + '\n\n')
