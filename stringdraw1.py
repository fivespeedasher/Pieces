#image
from PIL import Image
import requests

pic = requests.get('https://09imgmini.eastday.com/mobile/20180920/20180920172021_59bb256b5e850579e3a0a6f0b272974b_1.jpeg')
with open('MA','wb') as f0:
    f0.write(pic.content)

im = Image.open("MA")
# im.show()
print(im.format,im.size,im.mode)
print(im.getpixel((0,0))) #注意括号的数量，返回的值为r，g，b
