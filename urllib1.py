# import urllib.request
# response =urllib.request.urlopen('https://www.baidu.com')
# print(response.read().decode('utf-8'))#编码转换字符串输出,read:获取响应内容。

import urllib.request
proxy_handle=urllib.request.ProxyHandler({
    'http':'http://113.238.139.139',
    'https':'https//113.238.139.139',
    })
opener=urllib.request.build_opener(proxy_handle)
response=opener.open('http://www.baidu.com')
