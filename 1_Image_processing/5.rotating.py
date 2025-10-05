import cv2 as cv
import matplotlib.pyplot as plt
image_path='img/dog.jpg'
img=cv.imread(image_path)
img_rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
center=(img_rgb.shape[1]//2,img_rgb.shape[0]//2)

matrix=cv.getRotationMatrix2D(center,45,1.0)

rotated=cv.warpAffine(img_rgb,matrix,(img_rgb.shape[1],img_rgb.shape[0]))

plt.imshow(rotated);plt.title("rotated 45 ");plt.axis("off")
plt.show()