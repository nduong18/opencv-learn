import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

if not ret:
    print('Cannot open camera!')
    exit()

def nothing(x):
    pass

cv2.namedWindow('Motion Detection Binary')
cv2.createTrackbar("Thresold", "Motion Detection Binary", 25, 255, nothing)

while True:
    diff = cv2.absdiff(frame1, frame2)

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    x = cv2.getTrackbarPos("Thresold", "Motion Detection Binary")

    _, thresh = cv2.threshold(blur, x, 255, cv2.THRESH_BINARY)
    cv2.imshow('Motion Detection Binary', thresh)

    # cv2.imshow('Gray', gray)
    # cv2.imshow('Blur', blur)
    # cv2.imshow('Diff', diff)

    frame1 = frame2
    ret, frame2 = cap.read()

    if not ret:
        print('Frame Error!')
        exit()

    if cv2.waitKey(1) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()
# pipeline: frame -> frame -> diff -> gray -> blur -> thresold -> show
