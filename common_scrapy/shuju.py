# -*- coding: utf-8 -*-
# @Author   : FELIX
# @Date     : 2018/4/25 16:09

import pymongo

item = {
    "company_name": "Jiangyin Lonrace International Trade Co., Ltd.",
    "company_link": "https://lonrace.en.alibaba.com/",
    "company_profile_link": "https://lonrace.en.alibaba.com/company_profile.html",
    "all_products_first_url": "https://lonrace.en.alibaba.com/productlist-1.html",
    "new_products_first_url": "https://lonrace.en.alibaba.com/productlist-1.html?scene=ws&filter=new",
    "hot_products_first_url": "https://lonrace.en.alibaba.com/productlist-1.html?scene=ws&filter=hot",
    "company_data": {
        "companyBusinessType": "Trading Company",
        "companyLocation": "Jiangsu, China (Mainland)",
        "supplierMainProducts": "Wall Panel,Acoustic Ceiling,Gabion,Geotextile,Steel Pipes",
        "assessmentOwnership": "Private Owner                           View More",
        "companyNumberOfEmployees": "11 - 50 People",
        "supplierTotalAnnualSalesVolume": "confidential",
        "companyEstablishedYear": "2007",
        "companyMainMarket": "Southeast Asia 22.00%  North America 18.00%  South America 10.00%",
        "companyCertificatesSummaryIntroduce": "credit certificate",
        "productCertificatesSummaryIntroduce": "CE, CE",
        "patentsSummaryIntroduce": "INSULATION PIPE, INSULATION PIPE"
    },
    "markets": {
        "SoutheastAsia": "22.00%  Wall Panel, Acoustic Ceiling, Gabion, Geotextile, Steel Pipes",
        "NorthAmerica": "18.00%  Wall Panel, Acoustic Ceiling, Gabion, Geotextile, Steel Pipes",
        "SouthAmerica": "10.00%  Wall Panel, Acoustic Ceiling, Gabion, Geotextile, Steel Pipes",
        "MidEast": "10.00%  Wall Panel, Acoustic Ceiling, Gabion, Geotextile, Steel Pipes",
        "SouthAsia": "10.00%  Wall Panel, Acoustic Ceiling, Gabion, Geotextile, Steel Pipes",
        "EasternEurope": "5.00%  Wall Panel, Acoustic Ceiling, Gabion, Geotextile, Steel Pipes",
        "Oceania": "5.00%  Wall Panel, Acoustic Ceiling, Gabion, Geotextile, Steel Pipes",
        "EasternAsia": "5.00%  Wall Panel, Acoustic Ceiling, Gabion, Geotextile, Steel Pipes",
        "WesternEurope": "5.00%  Wall Panel, Acoustic Ceiling, Gabion, Geotextile, Steel Pipes",
        "NorthernEurope": "3.00%  Wall Panel, Acoustic Ceiling, Gabion, Geotextile, Steel Pipes",
        "SouthernEurope": "3.00%  Wall Panel, Acoustic Ceiling, Gabion, Geotextile, Steel Pipes",
        "Africa": "2.00%  Wall Panel, Acoustic Ceiling, Gabion, Geotextile, Steel Pipes",
        "CentralAmerica": "2.00%  Wall Panel, Acoustic Ceiling, Gabion, Geotextile, Steel Pipes"
    }}

MONGO_URI = 'localhost'
MONGO_DATABASE = 'alibaba_international_3d_wall_panels'
INFORMATIONS_MONGO_DATABASE = 'alibaba_international_informations'
client = pymongo.MongoClient(MONGO_URI)
db = client[INFORMATIONS_MONGO_DATABASE]
db['company_profile'].update({'company_link': item['company_link']}, {'$set': item}, True)  # 更新去重
