import cv2

img = cv2.imread("./images/capybara.jpg")
h, w = img.shape[:2]
resized = cv2.resize(img, (w//2, h//2))

crop = resized[100:300, 200:400]

cv2.imshow("resized", resized)
cv2.imshow("crop", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
