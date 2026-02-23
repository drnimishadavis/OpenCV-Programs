import cv2 as cv
path='1.jpg'
image=cv.imread(path)
cv.rectangle(image,(5,5),(220,220),(250,0,0),-1)
cv.imshow("rectangle image",image)
cv.waitKey(0)
cv.destroyAllWindows()