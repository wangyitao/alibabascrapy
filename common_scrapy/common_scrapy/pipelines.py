# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class CommonScrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class AlibabaInternationalSpiderPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        print(str(item))
        with open('ttttt.txt', 'a', encoding='utf8')as f:
            import json
            f.write(str(item) + '\n\n')
        print('更新开始')
        try:
            self.db['details'].update({'title': item['title']}, {'$set': item}, True)  # 更新去重
        except Exception as e:
            with open('loggers.txt','a',encoding='utf8') as f:
                f.write('details插入出错'+str(e)+'\n\n')
        print('更新结束')

        return item


class AlibabaInternationalProductsDetailsPipelines(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('INFORMATIONS_MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        print(str(item))
        print('更新开始')
        if item['flag'] == 'all':
            with open('all.txt', 'a', encoding='utf8')as f0:
                import json
                f0.write(str(item) + '\n\n')
            try:
                self.db['all_products_details'].update({'product_detail_url': item['product_detail_url']}, {'$set': item},
                                                       True)  # 更新去重
            except Exception as e:
                with open('loggers.txt', 'a', encoding='utf8') as f:
                    f.write('all_products_details插入出错' + str(e) + '\n\n')

        elif item['flag'] == 'new':
            with open('new.txt', 'a', encoding='utf8')as f1:
                import json
                f1.write(str(item) + '\n\n')
            try:
                self.db['new_products_details'].update({'product_detail_url': item['product_detail_url']}, {'$set': item},
                                                       True)  # 更新去重
            except Exception as e:
                with open('loggers.txt', 'a', encoding='utf8') as f:
                    f.write('new_products_details插入出错' + str(e) + '\n\n')
        elif item['flag'] == 'hot':
            with open('hot.txt', 'a', encoding='utf8')as f2:
                import json
                f2.write(str(item) + '\n\n')
            try:
                self.db['hot_products_details'].update({'product_detail_url': item['product_detail_url']}, {'$set': item},
                                                       True)  # 更新去重
            except Exception as e:
                with open('loggers.txt', 'a', encoding='utf8') as f:
                    f.write('hot_products_details插入出错' + str(e) + '\n\n')
        elif item['flag'] == 'profile':
            with open('profile.txt', 'a', encoding='utf8')as f2:
                import json
                f2.write(str(item) + '\n\n')
            try:
                self.db['company_profile'].update({'company_link': item['company_link']}, {'$set': item},
                                                       True)  # 更新去重
            except Exception as e:
                with open('loggers.txt', 'a', encoding='utf8') as f:
                    f.write('company_profile插入出错' + str(e) + '\n\n')
        print('更新结束')
        return item


class AlibabaInternationalCompanyProfilePipelines(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('INFORMATIONS_MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        print(str(item))
        with open('company_profile.txt', 'a', encoding='utf8')as f:
            import json
            f.write(str(item) + '\n\n')
        print('更新开始')
        try:
            self.db['company_profile'].update({'company_link': item['company_link']}, {'$set': item}, True)  # 更新去重
        except Exception as e:
            with open('loggers.txt', 'a', encoding='utf8') as f:
                f.write('company_profile插入出错' + str(e) + '\n\n')
        print('更新结束')

        return item
