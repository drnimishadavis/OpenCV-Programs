import cv2 as cv
import numpy as np
img=cv.imread('img/logo.png',1)
cv.imshow('Opencv logo',img)
cv.waitKey(0)
cv.destroyAllWindows()