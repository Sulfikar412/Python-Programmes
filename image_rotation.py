import PIL
from PIL import Image
from numpy import asarray
import cv2
image=Image.open("spiderman1.jpg").convert("L")
image.show()

data=asarray(image)
print("Numerical array:")
print(data)

rotate_image=image.rotate(35)
rotate_image.show()