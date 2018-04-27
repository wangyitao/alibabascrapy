from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://www.alibaba.com/products/3D_Wall_Panel/1.html'

url3='https://www.alibaba.com/product-detail/Modern-Wall-Art-Decor-interior-3d_60391338563.html'

url2='https://3dboard.en.alibaba.com/company_profile.html'


all_products_first_url='https://3dboard.en.alibaba.com/productlist-1.html'
new_products_first_url='https://3dboard.en.alibaba.com/productlist-1.html?scene=ws&filter=new'
hot_products_first_url='https://3dboard.en.alibaba.com/productlist-1.html?scene=ws&filter=hot'
# 创建chrome参数对象
opt = webdriver.ChromeOptions()
# 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
opt.set_headless()
# 创建chrome无界面对象
browser = webdriver.Chrome()
browser.implicitly_wait(30)  # 隐性等待，最长等30秒
browser.get(all_products_first_url)
#############################滚动操作
s = 'window.scrollTo({}, {})'
i = '0'
m = 40
j = m
while j > 0:
    # k = '(document.body.scrollHeight) / {}'.format(str(j))
    k = '(document.body.scrollHeight)/{}*{}'.format(str(m), str(j))
    browser.execute_script(s.format(i, k))
    i = k
    j -= 1
ii = 'document.body.scrollHeight'
j = 1
while j <= m:
    # k = '(document.body.scrollHeight) / {}'.format(str(j))
    k = '(document.body.scrollHeight)/{}*{}'.format(str(m), str(j))
    browser.execute_script(s.format(ii, k))
    ii = k
    j += 1
locator2 = (By.CSS_SELECTOR, 'img')
locator3 = (By.CSS_SELECTOR, 'div')
locator4 = (By.CSS_SELECTOR, 'span')
locator5 = (By.CSS_SELECTOR, 'a')

# locator=(By.CSS_SELECTOR,'h2')
# locator4=(By.CSS_SELECTOR,'.kv')
# WebDriverWait(spider.browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator))
# WebDriverWait(spider.browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator1))
WebDriverWait(browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator2))
WebDriverWait(browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator3))
WebDriverWait(browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator4))
WebDriverWait(browser, 20, 0.5).until(EC.presence_of_all_elements_located(locator5))
time.sleep(1)

# print(browser.page_source)
from pyquery import PyQuery as pq
import re
doc = pq(str(browser.page_source))

view=doc('.app-productsGalleryView')
soup=BeautifulSoup(str(view),'lxml')
li=soup.find_all('li')
for i in li:
    # print(i)
    img_url=''.join(['http:',i.find_all('img')[0].attrs['src']])
    title=i.find_all(attrs={'class': 'product-title'})[0].find_all('a')[0].get_text().strip()
    detail_url=i.find_all(attrs={'class': 'product-title'})[0].find_all('a')[0].attrs['href'].strip()[1:]
    min_order=i.find_all(attrs={'class': 'product-order-info'})[0].get_text().strip()
    price=i.find_all(attrs={'class': 'product-order-info'})[1].get_text().strip()
    print(detail_url)
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')


# aa=doc('.name-text').text()
# bb=doc('.company-link').attr('href')
# # print(aa)
# # print(bb)
# cc=''.join([str(bb),'company_profile.html'])
# # print(cc)

''' #获取页码
all_products_first_url='https://3dboard.en.alibaba.com/productlist-1.html'
new_products_first_url='https://3dboard.en.alibaba.com/productlist-1.html?scene=ws&filter=new'
hot_products_first_url='https://3dboard.en.alibaba.com/productlist-1.html?scene=ws&filter=hot'


p=doc('.ui-label').text()
all_page=int(re.findall('of.*?(\d+).*?Page',str(p))[0])
for page in range(1,all_page+1):
    all_products_url='https://3dboard.en.alibaba.com/productlist-{}.html'.format(page)
    print(all_products_url)
'''
all_products={}
new_products={}
hot_products={}


'''
ee=str(doc('.widget-supplier-trade-market .ui2-table'))
# print(ee)
soup=BeautifulSoup(ee,'lxml')
ssss=soup.find_all('tr')
# print(ssss)
markets={}
for iiii in ssss[1:]:
    try:
        patten = re.compile('<.*?>', re.S)
        market=patten.sub('',str(iiii)).strip().split('\n')
        markets[market[0].replace(' ','')]=' '.join(market[1:])
        # print(market)
        # print()
    except Exception as e:
        print('没有找到键值对', e)
print(markets)
'''
'''
from bs4 import BeautifulSoup
dd=str(doc('.content-table'))
soup=BeautifulSoup(dd,'lxml')
sss=soup.find_all('tr')
# print(sss)
data={}
for iii in sss:
#     aaa=iii[0].get('data-role')
#     print(aaa)
    try:
        import re

        patten=re.compile('<.*?>',re.S)
        key=iii.attrs['data-role']
        print(iii.attrs['data-role'])
        ppp=str(iii.find_all('td')[0]).strip()
        value=patten.sub('',ppp).strip().replace('\n',' ').replace('  ',' ')
        print(patten.sub('',ppp).strip().replace('\n',' ').replace('  ',' '))
        data[key]=value
        print('####################################')
    except Exception as e:
        print('没有找到键值对',e)
print(data)
#     soup2=BeautifulSoup(iii,'lxml')
#     key=soup2.select('tr')[0].get('data-role')

# for i in dd:
#     print(i)
# a=doc('.title').items()
# for i in a:
#     aa=i.find('a').attr('href')
#     patten=re.compile('.*?www.alibaba.com/product-detail.*')
#     p=patten.findall(str(aa))
#     if p:
#         print(''.join(['http:',p[0]]))
'''

