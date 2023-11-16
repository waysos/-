import requests
import os
# import numpy as np
from concurrent.futures import ThreadPoolExecutor
import time
import re
import warnings

warnings.filterwarnings('ignore')
header = {
   # 输入Cookie
    'Cookie': '****',
   # 输入伪装浏览器信息
    'user-agent':
        '****'
}

# with open('D:/res/headers.txt','r',encoding='utf-8')as f:
#    headers=f.readlines()

# proxies=[]
# with open('D:/res/https.txt','r',encoding='utf-8') as f:
#    proxies=f.readlines()
# proxy = {'http': 'http://106.11.226.232:8009', 'https': 'http://106.11.226.232:8009'}


def fun(url, page):
    time.sleep(10)
    # proxy={'https':'http://'+np.random.choice(proxies),'http':'http://'+np.random.choice(proxies)}
    r = requests.get(url, headers=header, timeout=10, verify=False, allow_redirects=False)
    if r.status_code != 200:
        print('error')
    print(r.text)
    hrefs = re.findall('href=".*?" title=".*?" target="_blank" class="j_th_tit ">', r.text)
    print(hrefs)
    print(page)
    if len(hrefs) == 0:
        return

    for href in hrefs:
        time.sleep(5)

        href = 'https://tieba.baidu.com' + href[6:19]

        # proxy={'https':'http://'+np.random.choice(proxies),'http':'http://'+np.random.choice(proxies)}
        r = requests.get(href, headers=header, timeout=10, verify=False, allow_redirects=False)

        print(r.encoding)
        r.encoding = 'utf-8'
        print(page)
        texts = re.findall('class="d_post_content j_d_post_content  clearfix" style="display:;">            .*?<',
                           r.text)
        print(texts)
        prefix = 'class="d_post_content j_d_post_content  clearfix" style="display:;">            '
        for i in range(len(texts)):
            texts[i] = texts[i][len(prefix):-1]

        if not os.path.exists('D:/res'):
            os.makedirs('D:/res')

        with open('D:/res/info.txt', 'a', encoding='utf-8') as f:

            f.write(' '.join(texts))


# pool=ThreadPoolExecutor(2)
# 500

# topic = input()
topic = '哈尔滨工程大学'
for page in range(0, 10):
    url = f'https://tieba.baidu.com/f?kw={topic}&ie=utf-8&pn={page * 50}'
    # pool.submit(fun,url)
    fun(url, page)
