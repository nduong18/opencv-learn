import cv2
import numpy as np

img = cv2.imread('images/capybara.jpg')

h,w = img.shape[:2]
resized = cv2.resize(img,(h//3 ,w //3))
cv2.imshow('resized', resized)

blur = cv2.GaussianBlur(resized, (9, 9), 0)
cv2.imshow('blur', blur)

kernel = np.ones((15,15), np.float32) / (15*15)
blur_manual = cv2.filter2D(resized, -1, kernel)
cv2.imshow('blur_manual', blur_manual)

cv2.waitKey(0)
cv2.destroyAllWindows()