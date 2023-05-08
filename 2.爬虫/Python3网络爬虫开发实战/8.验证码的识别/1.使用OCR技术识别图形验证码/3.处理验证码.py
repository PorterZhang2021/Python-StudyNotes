import tesserocr
from PIL import Image
# 打开图片
image = Image.open('captcha.png')
# 查看结果
result = tesserocr.image_to_text(image)
print(result)