# Gaussian Blurring
# Median Blurring
# Bilateral Blur

import cv2 as cv
from matplotlib import pyplot as plt
image_path='img/dog.jpg'
img=cv.imread(image_path)
imgr=cv.resize(img,(1900,800))
imgrgb=cv.cvtColor(imgr,cv.COLOR_BGR2RGB)
plt.imshow(imgrgb)
plt.title('original image')
plt.axis('off')
plt.show()

# Gaussian Blurring
gb=cv.GaussianBlur(imgr,(105,105),0)
gbrgb=cv.cvtColor(gb,cv.COLOR_BGR2RGB)
plt.imshow(gbrgb)
plt.title('Gaussian Blurring')
plt.axis('off')
plt.show()

# Median Blurring
me=cv.medianBlur(imgr,111)
mergb=cv.cvtColor(me,cv.COLOR_BGR2RGB)
plt.imshow(mergb)
plt.title('Median Blurring')
plt.axis('off')
plt.show()

# Bilateral Blur
BI=cv.bilateralFilter(imgr,15,150,150)
BIrgb=cv.cvtColor(BI,cv.COLOR_BGR2RGB)
plt.imshow(BIrgb)
plt.title('Bilateral Blurring')
plt.axis('off')
plt.show()