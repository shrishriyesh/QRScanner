import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from matplotlib import pyplot as plt
img=cv2.imread('QR.png',)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernel=np.ones((5,5), np.float32)/25
dst=cv2.filter2D(img, -1, kernel)
blur=cv2.blur(img,(5,5))
gblur=cv2.GaussianBlur(img,(5,5),0)
median=cv2.medianBlur(img,3)
bilfil=cv2.bilateralFilter(img,9,75,75)
dst = cv2.fastNlMeansDenoising(img,None,7,7,15)
fil= cv2.fastNlMeansDenoisingColored(img,None, 10, 10, 7, 15)
decoded=pyzbar.decode(median)
for obj in decoded:
    print(obj.data)
titles=['OG','2D convolved','blurred','gblur','med',"bilfil","FastColFil","Fast","FastColour"]
imgs=[img, dst,blur,gblur,median,bilfil,dst,fil]
for i in range(8):
    plt.subplot(3,3, i+1), plt.imshow(imgs[i],'gray')
    plt.title(titles[i])
plt.show()