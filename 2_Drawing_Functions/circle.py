import cv2 as cv
path='1.jpg'
image=cv.imread(path)
cv.circle(image,center=(250,250),radius=60,color=(0,250,0),thickness=-1)
cv.circle(image,center=(250,250),radius=60,color=(255,0,0),thickness=8)
cv.imshow("Circle on image",image)
cv.waitKey(0)
cv.destroyAllWindows()