import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('pic.jpg')
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

def show_image(img,title):
    plt.imshow(img,cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

show_image(gray_image,'Original Grayscale Image')

# Binary Threshold
_,thresh_binary=cv2.threshold(gray_image,120,255,cv2.THRESH_BINARY)
show_image(thresh_binary,"Binary Threshold")
# Binary Inverted
_,thresh_binary_inv=cv2.threshold(gray_image,120,255,cv2.THRESH_BINARY_INV)
show_image(thresh_binary_inv,"Binary Inverted")

# Truncated Threshold
_,thresh_trunc=cv2.threshold(gray_image,120,255,cv2.THRESH_TRUNC)
show_image(thresh_trunc,"turncated Threshold")

# To zero Threshold
_,thresh_tozero=cv2.threshold(gray_image,120,255,cv2.THRESH_TOZERO)
show_image(thresh_tozero,"To zero Threshold")

# To Zero Inverted
_,thresh_tozero_inv=cv2.threshold(gray_image,120,255,cv2.THRESH_TOZERO_INV)
show_image(thresh_tozero_inv,"To zero inverted")

cv2.imwrite('binary.png',thresh_binary)
cv2.imwrite('binary_inv.png',thresh_binary_inv)
cv2.imwrite('trucn.png',thresh_trunc)
cv2.imwrite('tozero.png',thresh_tozero)
cv2.imwrite('tozeroinv.png',thresh_tozero_inv)

print("success")