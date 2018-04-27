# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from common_scrapy.items import AlibabaInternationalItem
import re
from bs4 import BeautifulSoup
import requests


class AlibabaInternationalSpider(scrapy.Spider):
    name = 'alibaba_international'
    allowed_domains = ['alibaba.com']
    start_urls = ['https://www.alibaba.com/products/3D_Wall_Panel/1.html']

    start_url = 'https://www.alibaba.com/products/3D_Wall_Panel/{}.html'

    # 第一次访问的方法重写
    def start_requests(self):
        """
        这里重写了start_requests方法，分别请求了用户查询的url和关注列表的查询以及粉丝列表信息查询
        :return:
        """
        for i in range(1, 101):  # 101
            yield scrapy.Request(self.start_url.format(str(i)), callback=self.parse)

    ## 如果需要调用selenium添加
    def __init__(self):
        # 创建chrome参数对象
        opt = webdriver.ChromeOptions()
        # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
        opt.set_headless()
        # 创建chrome无界面对象
        self.browser = webdriver.Chrome(options=opt)
        self.browser.implicitly_wait(30)  # 隐性等待，最长等30秒
        super(AlibabaInternationalSpider, self).__init__()
        dispatcher.connect(self.closeSpider, signals.spider_closed)

    def closeSpider(self, spider):
        print("spider closed")
        # 当爬虫退出的时关闭浏览器
        self.browser.close()

    # https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&SearchText=3D+Wall+Panel
    # https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&SearchText=3D+Wall+Panel

    # 第一次访问的方法重写
    # def start_requests(self):
    #     """
    #     这里重写了start_requests方法，分别请求了用户查询的url和关注列表的查询以及粉丝列表信息查询
    #     :return:
    #     """
    #     yield scrapy.Request(self.start_url,callback=self.parse)

    def parse(self, response):
        title=''
        price=''
        img=''
        detail_url=''
        min_order=''
        location=''
        try:
            item = AlibabaInternationalItem()
            # print(response.text)

            titles = response.xpath("//h2").extract()
            prices = response.xpath("//div[@class='price']").extract()
            # b=response.xpath("//div[@class='item-content']")
            b = response.xpath("//div[@class='item-content']").extract()
            # pri
            # nt(b)
            bbb = 0
            for i in b:
                # print(i)
                print(bbb, '#####################################')
                bbb += 1
                # print(i)
                with open('ddd.txt', 'a', encoding='utf8') as f:
                    f.write(i + '\n\n' + '#########################################################################')
                #
                soup = BeautifulSoup(i, 'lxml')
                try:
                    img = 'http:' + str(soup.select('img')[0].get('src'))
                except Exception as e:
                    with open('logger.txt', 'a+', encoding='utf8') as f:
                        f.write('img:'+str(e) + '\n\n')
                # application = soup.select('div.kv-prop > div:nth-of-type(6) > b')[0].get_text().strip().replace('\n', '')
                # place = soup.select(' div.kv-prop > div:nth-of-type(3) > b')[0].get_text().strip().replace('\n', '')
                try:
                    title = soup.select('h2')[0].get_text().replace('\n', '').strip()
                except Exception as e:
                    with open('logger.txt', 'a+', encoding='utf8') as f:
                        f.write('title:'+str(e) + '\n\n')
                try:
                    detail_url = 'http:' + soup.select('h2 a')[0].get('href')
                except Exception as e:
                    with open('logger.txt', 'a+', encoding='utf8') as f:
                        f.write('detail_url:'+str(e) + '\n\n')
                try:
                    price = soup.select('.price')[0].get_text().strip().replace(' ', '').replace('\n', '')
                except Exception as e:
                    with open('logger.txt', 'a+', encoding='utf8') as f:
                        f.write('price:'+str(e) + '\n\n')
                details = soup.select('.kv')
                try:
                    min_order = soup.select('.min-order')[0].get_text().strip()
                except Exception as e:
                    with open('logger.txt', 'a+', encoding='utf8') as f:
                        f.write('min_order:'+str(e) + '\n\n')
                try:
                    location = soup.select('div.loc-box > span.location.util-ellipsis')[0].get_text().split('\n')[0]
                except Exception as e:
                    with open('logger.txt', 'a+', encoding='utf8') as f:
                        f.write('location:'+str(e) + '\n\n')
                try:
                    id = str(re.search('(\d{11})', str(i)).group())
                except Exception as e:
                    id = None
                    with open('logger.txt', 'a+', encoding='utf8') as f:
                        f.write('id:'+str(e) + '\n\n')
                url2 = 'https://www.alibaba.com/view/mutiapps/mutiapps.htm?data=%5B%7B%22module_name%22%3A%22supplierBasicInformation%22%2C%22module_data%22%3A%7B%7D%7D%2C%7B%22module_name%22%3A%22supplierAndProductSamples%22%2C%22module_data%22%3A%7B%7D%7D%2C%7B%22module_name%22%3A%22supplierProductionCapacity%22%2C%22module_data%22%3A%7B%7D%7D%2C%7B%22module_name%22%3A%22supplierProductionFlow%22%2C%22module_data%22%3A%7B%7D%7D%2C%7B%22module_name%22%3A%22supplierQualityManagementProcess%22%2C%22module_data%22%3A%7B%7D%7D%2C%7B%22module_name%22%3A%22supplierProductionLineEmployee%22%2C%22module_data%22%3A%7B%7D%7D%2C%7B%22module_name%22%3A%22rd%22%2C%22module_data%22%3A%7B%7D%7D%2C%7B%22module_name%22%3A%22supplierTestReport%22%2C%22module_data%22%3A%7B%7D%7D%2C%7B%22module_name%22%3A%22supplierTradeMarket%22%2C%22module_data%22%3A%7B%7D%7D%2C%7B%22module_name%22%3A%22detailCompanyProfileFooter%22%2C%22module_data%22%3A%7B%7D%7D%5D&detailId={}'.format(
                    id)



                detail_data = requests.get(url2)
                market_soup = BeautifulSoup(detail_data.text, 'lxml')

                c = market_soup.select('tbody')

                p = re.compile('<tr.*?"(odd|even)">.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?</tr>',re.S)
                DDDD = p.findall(str(c))
                market = {}
                for dic in DDDD:
                    try:
                        market[dic[1].replace(' ', '')] = dic[2]
                    except Exception as e:
                        with open('logger.txt', 'a+', encoding='utf8') as f:
                            f.write(str(e) + '\n\n')

                # 够买详情
                buy_detail = {}
                buy = soup.select('.record.util-clearfix .lab')
                try:
                    if len(buy) == 2:
                        buy_detail['Transactions'] = '$' + soup.select('.record.util-clearfix .num')[0].get_text()
                        buy_detail['ResponseRate'] = soup.select('.record.util-clearfix .num')[1].get_text()
                    elif len(buy) == 1:
                        buy_detail['Transactions'] = 0
                        buy_detail['ResponseRate'] = soup.select('.record.util-clearfix .num')[0].get_text()
                except Exception as e:
                    with open('logger.txt', 'a+', encoding='utf8') as f:
                        f.write('buy_detail:'+str(e) + '\n\n')

                print(detail_url)
                detail = {}
                for dd in details:
                    # key,value=str(dd.get('title')).split(':')
                    # detail[key]=value
                    # print(dd)
                    try:
                        patten = re.compile('.*?title="(.*?)".*?', re.S)
                        aa = patten.findall(str(dd))[0]
                        # print(aa)
                        a = str(aa).split(':')
                        key = str(a[0]).replace(' ', '')
                        value = str(a[1]).replace(' ', '')
                        detail[key] = value
                    except Exception as e:
                        with open('logger.txt', 'a+', encoding='utf8') as f:
                            f.write('detail:' + str(e) + '\n\n')
                # print(detail)
                # print(title)
                # print(price)
                # print(img)
                # yield scrapy.Request(detail_url, callback=self.detail_parse)
                item['title'] = title
                item['detail'] = detail
                item['price'] = price
                item['img_url'] = img
                item['detail_url'] = detail_url
                item['min_order'] = min_order
                item['location'] = location
                item['buy_detail'] = buy_detail
                item['market'] = market
                item['id'] = id
                yield item
                # print('\n\n')
        except Exception as e:
            with open('logger.txt', 'a+', encoding='utf8') as f:
                f.write(str(e) + '\n\n')

    def detail_parse(self, response):
        with open('det.txt', 'a', encoding='utf8') as f:
            f.write(response.text + '\n\n' + '#########################################' + '\n')

        """
        for title,price in zip(titles,prices):
            # c=i.xpath('//div[@class="item-content"]//h2').extract_first()
            # print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
            # print(c)
            patten=re.compile('<a.*?>(.*?)</a>',re.S)
            patten2=re.compile('<b>(.*?)</b>',re.S)
            # print(i)
            title=str(title).replace('</strong>','').replace('<strong>','').strip()
            title=patten.findall(title)[0].strip()
            price=patten2.findall(price)[0].strip()
            item['title']=title
            print(title)
            print(price)
"""

        # 'body > div.l-page > div.l-page-main > div.l-main-content > div.l-grid.l-grid-sub > div.l-col-main > div.l-grid.l-grid-extra > div.l-col-main > div > div.l-theme-card-box.ns-theme-offer-attr.uf-theme-card-border.uf-theme-card-margin-bottom > div:nth-child(1) > div:nth-child(1) > div > div > div > div.brand-center-container.has-attr > div > div.title > h2 > a
