import cv2

img = cv2.imread('images/capybara.jpg')
h,w = img.shape[:2]
resized = cv2.resize(img, (w//3,h//3))

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)

def nothing(x):
    pass

cv2.namedWindow('detect edge')
cv2.createTrackbar('Low', 'detect edge', 100, 255, nothing)
cv2.createTrackbar('High', 'detect edge', 100, 255, nothing)

while True:
    x = cv2.getTrackbarPos('Low', 'detect edge')
    y = cv2.getTrackbarPos('High', 'detect edge')

    edge = cv2.Canny(blur, x, y)
    cv2.imshow('detect edge', edge)

    if cv2.waitKey(1) & 0xFF == 27: # Chờ nhấn phím ESC để thoát
        break

cv2.destroyAllWindows()