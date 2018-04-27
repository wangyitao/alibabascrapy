# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from selenium import webdriver
from scrapy.http import HtmlResponse
from logging import getLogger
from scrapy import signals
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CommonScrapySpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class CommonScrapyDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SeleniumDownloadMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        """
                用chrome抓取页面
                :param request: Request对象
                :param spider: Spider对象
                :return: HtmlResponse
                """

        ##########################
        # 这里填写条件
        if spider.name == 'alibaba_international':
            try:
                spider.browser.get(request.url)
                #############################滚动操作
                s = 'window.scrollTo({}, {})'
                i = '0'
                m = 40
                j = m
                while j > 0:
                    # k = '(document.body.scrollHeight) / {}'.format(str(j))
                    k = '(document.body.scrollHeight)/{}*{}'.format(str(m), str(j))
                    spider.browser.execute_script(s.format(i, k))
                    i = k
                    j -= 1
                i = 'document.body.scrollHeight'
                j = 1
                while j <= m:
                    # k = '(document.body.scrollHeight) / {}'.format(str(j))
                    k = '(document.body.scrollHeight)/{}*{}'.format(str(m), str(j))
                    spider.browser.execute_script(s.format(i, k))
                    i = k
                    j += 1
                ##############################

                # spider.browser.execute_script(
                #     'var i=1000;while(i>0){window.scrollTo(0, (document.body.scrollHeight)/i)}')

                # 鼠标下滑加载
                # for i in range(3): #下滑三次
                #     spider.browser.execute_script('window.scrollTo(0,document.body.scrollHeight);var leftOfPage = document.body.scrollHeight;return leftOfPage;') #执行js代码
                #     time.sleep(2)

                # time.sleep(3)
                if spider.name == 'alibaba_international':
                    # locator1=(By.CSS_SELECTOR,'.item-content')
                    locator2 = (By.CSS_SELECTOR, 'img')
                    locator3 = (By.CSS_SELECTOR, 'div')
                    locator4 = (By.CSS_SELECTOR, 'span')

                    # locator=(By.CSS_SELECTOR,'h2')
                    # locator4=(By.CSS_SELECTOR,'.kv')
                    # WebDriverWait(spider.browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator))
                    # WebDriverWait(spider.browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator1))
                    WebDriverWait(spider.browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator2))
                    WebDriverWait(spider.browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator3))
                    WebDriverWait(spider.browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator4))
                    time.sleep(1)
                    # WebDriverWait(spider.browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator4))
                    print(spider.name)
                # locator = (By.CSS_SELECTOR, '#dg-item-tl-0')
                # WebDriverWait(spider.browser, 20, 0.5).until(EC.presence_of_element_located(locator))

            except:
                print('timeout')

            ##########################
            print("访问：{0}".format(request.url))
            return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source, encoding="utf-8",
                                request=request)
            # 这里填写条件
        if spider.name == 'alibaba_international_details':
            try:
                spider.browser.get(request.url)
                #############################滚动操作
                s = 'window.scrollTo({}, {})'
                i = '0'
                m = 40
                j = m
                while j > 0:
                    # k = '(document.body.scrollHeight) / {}'.format(str(j))
                    k = '(document.body.scrollHeight)/{}*{}'.format(str(m), str(j))
                    spider.browser.execute_script(s.format(i, k))
                    i = k
                    j -= 1
                i = 'document.body.scrollHeight'
                j = 1
                while j <= m:
                    # k = '(document.body.scrollHeight) / {}'.format(str(j))
                    k = '(document.body.scrollHeight)/{}*{}'.format(str(m), str(j))
                    spider.browser.execute_script(s.format(i, k))
                    i = k
                    j += 1
                ##############################

                # spider.browser.execute_script(
                #     'var i=1000;while(i>0){window.scrollTo(0, (document.body.scrollHeight)/i)}')

                # 鼠标下滑加载
                # for i in range(3): #下滑三次
                #     spider.browser.execute_script('window.scrollTo(0,document.body.scrollHeight);var leftOfPage = document.body.scrollHeight;return leftOfPage;') #执行js代码
                #     time.sleep(2)

                locator2 = (By.CSS_SELECTOR, 'img')
                locator3 = (By.CSS_SELECTOR, 'div')
                locator4 = (By.CSS_SELECTOR, 'span')
                locator5 = (By.CSS_SELECTOR, 'a')

                # locator=(By.CSS_SELECTOR,'h2')
                # locator4=(By.CSS_SELECTOR,'.kv')
                # WebDriverWait(spider.browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator))
                # WebDriverWait(spider.browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator1))
                WebDriverWait(spider.browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator2))
                WebDriverWait(spider.browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator3))
                WebDriverWait(spider.browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator4))
                WebDriverWait(spider.browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator5))
                time.sleep(1)

            except:
                print('timeout')

            ##########################
            print("访问：{0}".format(request.url))
            return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source, encoding="utf-8",
                                request=request)
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
