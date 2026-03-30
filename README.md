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
`blur_manual = cv2.filter2D(resized, -1, kernel)`: lấy kernel → quét qua ảnh → tạo ảnh mới theo cách kernel định nghĩa <br>
`np.float32`: Thuộc Numpy -> trong blur dùng làm kiểu dữ liệu của ma trận (số thập phân) <br>
### Day 5:
* Dùng `Canny` để detect edge
* Cạnh là nơi pixel thay đổi mạnh (chỗ chuyển đen -> trắng = edge)
* `Pipeline chuẩn`: image -> grayscale -> blur -> canny
  * `Grayscale`:đưa ảnh về 1 kênh -> đỡ bị loạn
  * `Blur`: ảnh thật luôn có noise (nhiễu) -> blur làm mịn ảnh -> giảm noise -> edge sạch hơn
  * `Canny`: detect edge

`cv2.Canny(image, threshold1, threshold2)`: thresold1 - ngưỡng thấp, thresold2 - ngưỡng cao
* Pixel mạnh → chắc chắn là edge . Pixel yếu → có thể là edge => Canny quyết định giữ hay bỏ
* **Quy tắc nhanh điều chỉnh thresold nhanh:**
  * ảnh nhiều noise -> thresold cao
  * ảnh sạch -> thresold thấp
  * object sáng -> thresold thấp
  * object tối -> thresold cao

`cv2.namedWindow('detect edge')`: Tạo 1 window có tên 'detect edge' <br>
`cv2.createTrackbar('Low', 'detect edge', 100, 255, nothing)`: Tạo trackbar với pos = 100 và limit = 255 <br>
`x = cv2.getTrackbarPos('Low', 'detect edge')`: Lấy vị trí ban đầu trong trackbar <br>
### Day 6: Motion dectection system
* `Pipeline`: Frame -> Frame -> Diff -> Gray -> Blur -> Thresold <br>
* Vùng trắng -> Có chuyển động <br>

`cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)`: `0` = camera mặc định , `CAP_DSHOW` = backend ổn định trên windows <br>
`ret, frame1 = cap.read() và ret, frame2 = cap.read()`: lấy 2 frame liên tiếp <br>
`diff = cv2.absdiff(frame1, frame2)`: pixel = |frame1 - frame2| , giống nhau -> 0 (đen), khác nhau > 0 (trắng) <br>
`_, thresh = cv2.threshold(blur, x, 255, cv2.THRESH_BINARY)`: Thresold: trắng -> chuyển động, đen -> ko chuyển động <br>
`cap.release()`: Giải phóng tài nguyên camera sau khi đã xử lý xong tránh xung đột / rò rỉ bộ nhớ <br>