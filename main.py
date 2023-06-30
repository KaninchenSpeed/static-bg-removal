import cv2

def nothing(x):
    pass

cam = cv2.VideoCapture(0)

ref_frame = False
ref_frame_set = False

cv2.namedWindow('preview')
cv2.createTrackbar('threshold', 'preview', 0, 255, nothing)

while (True):
    ret, frame = cam.read()
    disp_frame = frame

    if ref_frame_set:
        min = cv2.getTrackbarPos('threshold', 'preview')

        diff = cv2.absdiff(frame, ref_frame)
        gray_scale = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        denoised = cv2.blur(gray_scale, (5, 5))
        approx_gray_scale = cv2.inRange(denoised, min, 255)
        disp_frame = cv2.bitwise_and(frame, frame, mask=approx_gray_scale)


    cv2.imshow('preview', disp_frame)

    key = cv2.waitKey(1)
    if key == ord('r'):
        ref_frame = frame
        ref_frame_set = True
    
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()