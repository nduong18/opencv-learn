import cv2

img = cv2.imread("./images/capybara.jpg", cv2.IMREAD_COLOR)

img[100:200, 100:200] = [0, 0, 255]

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

