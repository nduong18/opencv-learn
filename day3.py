import cv2

img = cv2.imread("./images/capybara.jpg")

# Giảm kích thước ảnh 50%
h,w = img.shape[:2]
resized = cv2.resize(img,(int(w/2),int(h/2)))

# Chỉnh màu ảnh
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
print(gray.shape)

gray_manual = (resized[:,:,0] + resized[:,:,1] + resized[:,:,2]) // 3
gray_manual = gray_manual.astype('uint8')

img_copy = resized.copy()
img_copy[:,:,0] = 0  # tắt blue
img_copy[:,:,1] = 0  # tắt green

cv2.imshow("gray", gray)
cv2.imshow("gray_manual", gray_manual)
cv2.imshow('blue', resized[:,:,0])
cv2.imshow('green', resized[:,:,1])
cv2.imshow('red', resized[:,:,2])
cv2.imshow("img_copy", img_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()