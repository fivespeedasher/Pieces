# import re
# ls = 'try正则:content'
# ls_new = re.sub(r'.*:','replace ',ls)
# print(ls_new)


# import re
# content = 'Hello 123 4567 Hallo World_This is a Demo'
# result = re.match('^Hello\s\d',content)
# print(result)
# print(result.group())
# result1 = re.match('^Hello(.*)mo$',content)
# print(result1.group(1))
# # group(1) 匹配第一个小括号里面的(.*)


# # todo  提取jsionp
# import requests
# import re
# url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=553627775790&spuId=855515261&sellerId=2616970884&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvj9vpvoWvUvCkvvvvvjiPPFs9ljY8PsqW6jthPmPWtji8RLMO1jDbnLSUtj38RphvCvvvphmrvpvEvvVlKF6vvCX1dphvmpmvr87TvvvZAghCvCB4cp2Mf3147DiFfJwwalKG7dLNZ4wCvvpvvhHh2QhvCvvvMMGCvpvVvUCvpvvvmphvLUC5znQaI2y7Ripqon0DRdh6H2paqO0QKfUpwhdEDLuTRLa9C7zOdigqrADn9Wv7%2Bu0wjomxfBkKHdUf8%2BCl5d8re361D70Oe8TJEcTtvpvIvvCvpvvv96vvvhNjvvmCJQvvBGwvvvUwvvCj1Qvvv3QvvhNjvvvmj8yCvv9vvhhFXPrvMUyCvvOCvhE20nvtvpvhvvCvpUwCvvpv9hCvRphvCvvvphmrvpvEvUj76D6vvvyf9phvHHiwdlCezHi47Iwat1Q47lr4NrGB&isg=BEREJqyawpG8dHWR9Bg9aBhyFcL29Xdl2VOw0l7lnY_aieZThm04V3o7zSFRkaAf&needFold=0&_ksTS=1520854544124_2463&callback=jsonp2464'
# r = requests.get(url)
# print(r.text)
# text = re.sub(r'.*\(','', r.text)
# text = text[:-1]
# print(text)





