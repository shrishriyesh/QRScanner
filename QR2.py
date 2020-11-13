import pyzbar.pyzbar as pyzbar
import cv2
import numpy
def scan():
    i=0
    cap=cv2.VideoCapture(0)
        while i<1:
        _,frame=cap.read()
        #fil = cv2.bilateralFilter(frame, 9, 75, 75)
        #fil= cv2.fastNlMeansDenoisingColored(frame,None, 10, 10, 7, 15)
        fil=cv2.medianBlur(frame, 3)
        decoded=pyzbar.decode(fil)
        for obj in decoded:
            print(obj.data)
            i=i+1
        cv2.imshow("QRCODE",fil)
        cv2.waitKey(5)
        cv2.destroyAllWindows()
scan()

