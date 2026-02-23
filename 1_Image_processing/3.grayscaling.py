<<<<<<< HEAD
import cv2 as cv
image_path='img/dog.jpg'
img=cv.imread(image_path)
imgr=cv.resize(img,(1900,800))
imggray=cv.cvtColor(imgr,cv.COLOR_BGR2GRAY)
cv.imshow('Gray scale image',imggray)
cv.waitKey(0)
=======
import cv2 as cv
image_path='img/dog.jpg'
img=cv.imread(image_path)
imgr=cv.resize(img,(1900,800))
imggray=cv.cvtColor(imgr,cv.COLOR_BGR2GRAY)
cv.imshow('Gray scale image',imggray)
cv.waitKey(0)
>>>>>>> 5c0a0cbacfb2d82a80bdad567211a90d24cb8d01
cv.destroyAllWinodwos()