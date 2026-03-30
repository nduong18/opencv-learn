### Day 1:
``cv2.imshow('img',img)``: Hiển thị ảnh. <br>
``cv2.waitkey(0)``: Thời gian chờ đóng cửa sổ hoặc chờ nhấn phím, nếu bằng 0 thì không. <br>
``cv2.destroyAllWindows()``: Tắt tự động đóng cửa sổ sau khi nhấn. <br>
``img[100:200, 100:200] = [0, 0, 255]``: Đổi một vùng thành màu đỏ <br>
### Day 2:
``resized = cv2.resize(img, (width, height))``: Resize image <br><br>
``h, w = img.shape[:2]`` <br>
``resized = cv2.resize(img, (w//2, h//2))`` : Giảm 50% kích thước <br>
``crop = img[y1:y2, x1:x2]``: Cắt ảnh ở tọa độ y:height , x: width <br>
### Day 3:
* Lưu ý: OpenCV dùng bảng màu BGR (Blue - Green - Red) <br>
* Dấu hai chấm là height,width hiện tại của ảnh

``gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)``: Chuyển ảnh sang màu Grayscale <br>
``print(gray.shape)``: In ra kích thước ảnh (Ảnh màu là (h,w,3) , ảnh grayscale là (h,w) <br>
``resized[:,:,0] → kênh BLUE`` <br>
``resized[:,:,1] → kênh GREEN`` <br>
``resized[:,:,2] → kênh RED`` <br>
``gray_manual = gray_manual.astype('uint8')``: Đảm bảo dữ liệu đúng kiểu ảnh (uint8: 0 -> 255)