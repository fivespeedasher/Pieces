import requests
# 爬取目标
url = 'http://www.mzitu.com'
# 设置报头，Http协议
header = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}
main_page = requests.get(url, headers = header)
print(main_page.text)