import tesserocr
from PIL import Image
import numpy as np

# 获取图像照片
image = Image.open('captcha.png')
# 查看高，宽，像素点向量
print(np.array(image).shape)
# 查看模式
print(image.mode)

# 图片类型和像素的位宽
# 1：像素用1位表示，Python中表示为True或False，即二值化。
# L: 像素用8位表示，取值0~255，表示灰度图像，数字越小，颜色越黑。
# P: 像素用8位表示，即调色板数据
# RGB：像素用3*8位表示，即真彩色
# RGBA: 像素用4*8位表示，即有透明通道的真彩色
# CMYK：像素用4*8位表示，即印刷四色模式
# YCbCr：像素用3*8位表示，即彩色视频格式
# I: 像素用32位整型表示
# F: 像素用32位浮点型表示

# 转换成灰度图像
image = image.convert('L')
# 灰度阈值
threshold = 76
# 图片转化成Numpy数组
array = np.array(image)
# 利用Numpy的where方法对数组进行筛选和处理
# 指定灰度大于阈值的图片的像素设置为255 表示白色 否则设置为0 表示黑色
array = np.where(array > threshold, 255, 0)
image = Image.fromarray(array.astype('uint8'))

# 输出识别结果
print(tesserocr.image_to_text(image))

