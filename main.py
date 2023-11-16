import requests
import os
# import numpy as np
from concurrent.futures import ThreadPoolExecutor
import time
import re
import warnings

warnings.filterwarnings('ignore')
header = {
    'Cookie': 'BIDUPSID=15847C841875F9051352BCD5E71FFB25; PSTM=1700036222; BAIDUID=15847C841875F905EF12D5EEBAB85746:FG=1; BAIDUID_BFESS=15847C841875F905EF12D5EEBAB85746:FG=1; BA_HECTOR=2ga1a02105258h0k258g0l811il8vju1q; ZFY=IVsuAfg2fKZuCEJiTzctIwAA9N:Ap:BB069vo4m3e0hck:C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=39636_39663_39688_39691_39695_39676_39678_39712_39733; PSINO=2; delPer=0; BAIDU_WISE_UID=wapp_1700105592440_781; USER_JUMP=-1; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1700105592; st_key_id=17; arialoadData=false; BDUSS=U9XdkUyYUliVzBPT05hcEVIOXF5MX5OTlBrR2VzaW9mVDVtYTFtVENZcU9HbjFsRVFBQUFBJCQAAAAAAQAAAAEAAADH~Oog19-1ttbH1sEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI6NVWWOjVVlT; BDUSS_BFESS=U9XdkUyYUliVzBPT05hcEVIOXF5MX5OTlBrR2VzaW9mVDVtYTFtVENZcU9HbjFsRVFBQUFBJCQAAAAAAQAAAAEAAADH~Oog19-1ttbH1sEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI6NVWWOjVVlT; STOKEN=8c83f2037946f95af3fcc2ba4993ca397026a74be5fb2b7ffadcf6456b0d412e; tb_as_data=4fa4c57029cc78db9be65792861a15be7cfe2b58645b088d6b168588374c72786be03a9d1cf7d6d9ba654894070c1ad21bfc56159008c83c45a7ca7b13cba3cf9781ee318e616041c5c52473cf73c93c64f5335e080905e2c53ba2d4b9c2a0c3a6245c5ea70cac3dd48fe55101fd48e1; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1700105617; XFI=ed9efba0-8430-11ee-a636-714c3381b557; ab_sr=1.0.1_NzRjMTIzZTI1ZTQyMGM4ZjNiMGE5ZWM3N2E4Y2Y0OTZjN2NkZjk2MTNhMjI5MDljNTZjZmE3ZmIwY2JhNDExZTNiYmQ5MjgyODJhNWI0NDE2ZjVlMDhhODM5NjIyOTJkYjIyMzRlZTFjYjQ3MTAyODFlNDlkY2ZiOGMxMTQwNjM2MWEyODc0MTBhMmY1MjM3NWE5NTdjMWE5MWQyZjNkOWMyNDc0MTJmNzk5YTlmNWQ1MWUzZTk5NTUxYTgyMGJj; st_data=e94a81db8085a6f162eeca9e72b151396fb6a455782fbd6e8d7351442bc72394adb4e72eb91b5b8db665a9e83b9a68d54a55c7775d846542dac4bc3719d70b4c2a56deef46394d1a18ae21bbd213e543d52fcbcfd72f83966fc3904748b846a58fc5ed1fa1a338a5073e0eac283560039e6c66e0f4e5e155149ec1d046edda9d61b4c99f5db27c6be6baba80a48a1a0b; st_sign=616756a3; XFCS=088BF1A923624FA7C55F1B5369D03502FEF78C1AC676FF8AE7D52EC81B867D70; XFT=nn/kC6qOw0EszsTJm95hvVHeKlChrmD/JHtJzMtcFAo=; RT="z=1&dm=baidu.com&si=d05959d1-74cc-446c-a9c0-070752544a53&ss=lp0mz1rb&sl=7&tt=4cf&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=mjc&ul=7eq9',
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
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