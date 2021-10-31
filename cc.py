import cv2
def takesnapshot():
    videoCapture = cv2.VideoCapture(0)
    result = True

    while (result):

        ret, frame = videoCapture.read()
        cv2.imwrite("pic1.jpg", frame)
        result = False

    videoCapture.release()

    cv2.destroyAllWindows()

takesnapshot()        