import pytesseract
from PIL import Image

file = 'd:/11.jpg'
im = Image.open(file)
# 进行灰度处理
im = im.convert('L')
# 设置二值化阈值
threshold = 120
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
# 通过表格转换成二进制图片，1的作用是白色，0就是黑色
im = im.point(table, '1')
print(pytesseract.image_to_string(im))
im.show()
