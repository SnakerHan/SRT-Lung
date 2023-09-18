import cv2
import numpy as np

# 读取图像
image = cv2.imread('pic_init/5.jpg')

# 进行边缘检测
edges = cv2.Canny(image, 250, 255)

# 检测直线
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=300, minLineLength=190, maxLineGap=5)

# 计算每条线段的长度
for line in lines:
    x1, y1, x2, y2 = line[0]
    length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("线段长度:", length)

# 在图像上绘制检测到的线段
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# 显示带有检测到线段的图像
cv2.imshow('Detected Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()