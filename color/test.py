# original dim: 936 x 793 (w, h) = 742,248
# downscaled to: 504 x 427 (w, h) = 215,208
# arc and plane downloads match original dim (936, 793) and each other

import cv2

img = cv2.imread('Q:\\print_a_pic\\color\\resized.jpg')
copy = img.copy()
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, w, _ = img.shape


for y in range(h):
    for x in range(w):
        hsv[y][x][1] += 50

back_to_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

cv2.imshow('og', copy)
cv2.imshow('modified', back_to_bgr)
cv2.waitKey(0)

cv2.imwrite('Q:\\print_a_pic\\color\\satboost50.jpg', back_to_bgr)

