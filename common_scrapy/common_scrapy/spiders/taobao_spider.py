# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from selenium.webdriver.support import expected_conditions as EC

class TaobaoSpiderSpider(scrapy.Spider):
    name = 'taobao_spider'
    allowed_domains = ['taobao.com']
    start_urls = ['http://www.taobao.com/']

    ## 如果需要调用selenium添加
    def __init__(self):
        # 创建chrome参数对象
        opt = webdriver.ChromeOptions()
        # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
        opt.set_headless()
        # 创建chrome无界面对象
        self.browser = webdriver.Chrome(options=opt)
        self.browser.implicitly_wait(30)  # 隐性等待，最长等30秒
        super(TaobaoSpiderSpider, self).__init__()
        dispatcher.connect(self.closeSpider, signals.spider_closed)

    def closeSpider(self, spider):
        print("spider closed")
        # 当爬虫退出的时关闭浏览器
        self.browser.close()

    def parse(self, response):
        # print(response.text)
        print('RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR')
        print(response.text)
        with open('taobao2.html','w',encoding='utf8') as f:
            f.write(response.text)

