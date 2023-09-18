import cv2
import numpy as np

# 读取图像
image = cv2.imread('pic_init/5.jpg')

# 转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用阈值来分割黑色部分
_, thresholded = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV)

# 查找轮廓
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 去除小的离散区域
min_contour_area = 100  # 设置最小轮廓面积阈值
filtered_contours = [contour for contour in contours if cv2.contourArea(contour) > min_contour_area]

# 计算所有黑色线段的总体边框范围
total_x_min = float('inf')
total_y_min = float('inf')
total_x_max = 0
total_y_max = 0

for contour in filtered_contours:
    x, y, w, h = cv2.boundingRect(contour)
    total_x_min = min(total_x_min, x)
    total_y_min = min(total_y_min, y)
    total_x_max = max(total_x_max, x + w)
    total_y_max = max(total_y_max, y + h)

total_width = total_x_max - total_x_min
total_height = total_y_max - total_y_min

print("所有黑色线段的总体边框范围 (x, y, width, height):", total_x_min, total_y_min, total_width, total_height)

# 在图像上绘制所有线段的总体边框范围
cv2.rectangle(image, (total_x_min, total_y_min), (total_x_max, total_y_max), (0, 255, 0), 2)

# 显示带有标记的图像
cv2.imshow('Detected Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()