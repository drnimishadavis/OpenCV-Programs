import cv2 as cv
import matplotlib.pyplot as plt
image_path='img/dog.jpg'
img=cv.imread(image_path)
img_rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
# SHRINKING
small=cv.resize(img_rgb,(img_rgb.shape[1]//2,img_rgb.shape[0]//2),interpolation=cv.INTER_AREA)
# ENLARGING
large=cv.resize(img_rgb,(img_rgb.shape[1]*2,img_rgb.shape[0]*2),interpolation=cv.INTER_CUBIC)

plt.subplot(1,3,1);plt.imshow(img_rgb);plt.title("Original")

plt.subplot(1,3,2);plt.imshow(small);plt.title("Shrinked")

plt.subplot(1,3,3);plt.imshow(large);plt.title("Enlarged")

plt.show()