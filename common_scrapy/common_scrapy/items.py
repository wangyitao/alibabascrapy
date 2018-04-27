# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CommonScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AlibabaInternationalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    detail = scrapy.Field()
    img_url = scrapy.Field()
    detail_url = scrapy.Field()
    min_order = scrapy.Field()
    location = scrapy.Field()
    buy_detail = scrapy.Field()
    market = scrapy.Field()
    id = scrapy.Field()


class AlibabaInternationalProductsDetailsItem(scrapy.Item):
    flag = scrapy.Field()
    company_name = scrapy.Field()
    company_link = scrapy.Field()
    product_img_url = scrapy.Field()
    product_title = scrapy.Field()
    product_detail_url = scrapy.Field()
    product_min_order = scrapy.Field()
    product_price = scrapy.Field()


class AlibabaInternationalCompanyProfileItem(scrapy.Item):
    company_name = scrapy.Field()
    company_link = scrapy.Field()
    company_data = scrapy.Field()
    markets = scrapy.Field()
    flag = scrapy.Field()
