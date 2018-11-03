# 绘制团并且添加文字

from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('arial.ttf',24,index=1)
img = Image.new('RGB',(300,200),(255,255,255))
draw = ImageDraw.Draw(img)
draw.text((0,50),u'真性感!',(0,0,0),font=font)
draw.text((0,60),unicode('NI HAOO','utf-8'),(0,0,0),font=font)
img.save(jd,'JPEG')