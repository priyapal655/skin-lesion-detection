import numpy as np
import cv2

image = cv2.imread("D:\C++\sample1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (17, 17), 32)

ret,thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

cnts, hier = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for cnt in cnts:
    cv2.drawContours(image,cnts, -1, (0, 0, 255), 3)
    print(cv2.contourArea(cnt))


cv2.imshow("thresh", thresh)
cv2.imshow("Image", image)
cv2.waitKey(0)
