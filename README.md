# OpenCV - Learn
### Yêu cầu: Python313 và các lib trong `requirements.txt`. Cài .venv để chạy project nhé !
### Day 1:
`cv2.imshow('img',img)`: Hiển thị ảnh. <br>
`cv2.waitkey(0)`: Thời gian chờ đóng cửa sổ hoặc chờ nhấn phím, nếu bằng 0 thì không. <br>
`cv2.destroyAllWindows()`: Tắt tự động đóng cửa sổ sau khi nhấn. <br>
`img[100:200, 100:200] = [0, 0, 255]`: Đổi một vùng thành màu đỏ <br>
### Day 2:
`resized = cv2.resize(img, (width, height))`: Resize image <br><br>
`h, w = img.shape[:2]` <br>
`resized = cv2.resize(img, (w//2, h//2))` : Giảm 50% kích thước <br>
`crop = img[y1:y2, x1:x2]`: Cắt ảnh ở tọa độ y:height , x: width <br>
### Day 3:
* Lưu ý: OpenCV dùng bảng màu BGR (Blue - Green - Red) <br>
* Dấu hai chấm là height,width hiện tại của ảnh <br>

`gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)`: Chuyển ảnh sang màu Grayscale <br>
`print(gray.shape)`: In ra kích thước ảnh (Ảnh màu là (h,w,3) , ảnh grayscale là (h,w) <br>
`resized[:,:,0] → kênh BLUE` <br>
`resized[:,:,1] → kênh GREEN` <br>
`resized[:,:,2] → kênh RED` <br>
`gray_manual = gray_manual.astype('uint8')`: Đảm bảo dữ liệu đúng kiểu ảnh (uint8: 0 -> 255) <br>
### Day 4:
* Vì `kernel` cần số thập phân (VD: 1 / 255 = 0.0044 nếu dùng int 1 // 225 = 0 "sai" <br> 
* CNN (Pytorch) và YOLO tất cả đều dùng `float32` <br>
* Dùng `float32` vì: Đủ chính xác + Nhanh hơn + Tiết kiệm RAM => OpenCV tối ưu cho `float32` <br>
* `np.ones(shape, dtype)`: Tạo một ma trận bằng numpy chỉ toàn số 1
  * `shape`: kích thước ma trận
  * `dtype`: kiểu dữ liệu (có thể thêm hoặc không, nên thêm `float32` để chuẩn)
    * `np.float32`: số thực
    * `np.uint8`: số nguyên

``blur = cv2.GaussianBlur(resized, (9, 9), 0)``: <br>
``kernel = np.ones((15,15), np.float32) / (15*15)``: tạo một bộ lọc (kernel) để lấy trung bình của vùng 15×15 pixel xung quanh → làm mờ ảnh (blur) (kích thước càng lớn -> blur càng mạnh), lấy trung bình của 15x15=225 pixel xung quanh mỗi điểm ảnh. <br>
`blur_manual = cv2.filter2D(resized, -1, kernel)`: lấy kernel → quét qua ảnh → tạo ảnh mới theo cách kernel định nghĩa<br>
`np.float32`: Thuộc Numpy -> trong blur dùng làm kiểu dữ liệu của ma trận (số thập phân)