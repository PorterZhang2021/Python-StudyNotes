import cv2

GAUSSIAN_BLUR_KERNEL_SIZE = (5, 5)
GAUSSIAN_BLUR_SIGMA_X = 0
CANNY_THRESHOLD1 = 200
CANNY_THRESHOLD2 = 450

# 传入待处理的图片信息，返回高斯滤波处理后的图片信息
def get_gaussian_blur_image(image):
    return cv2.GaussianBlur(image, GAUSSIAN_BLUR_KERNEL_SIZE, GAUSSIAN_BLUR_SIGMA_X)

# 传入待处理的图片的信息，返回边缘检测处理后的图片信息
def get_canny_image(image):
    return cv2.Canny(image, CANNY_THRESHOLD1, CANNY_THRESHOLD2)

# 出入待处理图片的信息，返回提取得到的轮廓信息
def get_contours(image):
    contours, _ = cv2.findContours(image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    return contours

# 定义目标轮廓的面积下限和面积上限
def get_contour_area_threshold(image_width, image_height):
    contour_area_min = (image_width * 0.15) * (image_height * 0.25) * 0.8
    contour_area_max = (image_width * 0.15) * (image_height * 0.25) * 1.2
    return contour_area_min, contour_area_max

# 定义目标轮廓的周长下限和周长上限
def get_arc_length_threshold(image_width, image_height):
    arc_length_min = ((image_width * 0.15) + (image_height * 0.25)) * 2 * 0.8
    arc_length_max = ((image_width * 0.15) + (image_height * 0.25)) * 2 * 1.2
    return arc_length_min, arc_length_max

# 定义缺口位置的偏移量下限和偏移量上限
def get_offset_threshold(image_width):
    offset_min = 0.2 * image_width
    offset_max = 0.85 * image_width
    return offset_min, offset_max


def main():

    # 图片
    image_raw = cv2.imread('captcha.bmp')
    # 图片大小
    image_height, image_width, _ = image_raw.shape
    # 高斯滤波处理
    image_gaussian_blur = get_gaussian_blur_image(image_raw)
    # 边缘检测处理
    image_canny = get_canny_image(image_gaussian_blur)
    # 轮廓提取
    contours = get_contours(image_canny)
    cv2.imwrite('image_canny.png', image_canny)
    cv2.imwrite('image_gaussian_blur.png', image_gaussian_blur)
    # 获取目标轮廓的面积下限与面积上限
    contour_area_min, contour_area_max = get_contour_area_threshold(image_width, image_height)
    # 获取目标轮廓的周长下限与周长上限
    arc_length_min, arc_length_max = get_arc_length_threshold(image_width, image_height)
    # 定义缺口位置的偏移量下限和偏移量上限
    offset_min, offset_max = get_offset_threshold(image_width)
    offset = None
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        # 判断阈值
        if contour_area_min < cv2.contourArea(contour) < contour_area_max and \
            arc_length_min < cv2.arcLength(contour, True) < arc_length_max and \
            offset_min < x < offset_max:
            cv2.rectangle(image_raw, (x, y), (x + w, y + h), (0, 0, 255), 2)
            offset = x
    cv2.imwrite('image_label.png', image_raw)
    print('offset', offset)

if __name__ == '__main__':
    main()