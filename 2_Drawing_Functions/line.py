import cv2 as cv
path='1.jpg'
image=cv.imread(path,0)
window_name='Line on Image Sample'
start_c=(100,100)
end_c=(550,550)
color=(0,0,0)
thick=9
image_line=cv.line(image,start_c,end_c,color,thick)
cv.imshow(window_name,image_line)
cv.waitKey(0)
cv.destroyAllWindows()