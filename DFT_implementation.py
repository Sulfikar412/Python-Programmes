from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

image=Image.open("spiderman1.jpg").convert("L")
print("spartial image :")
image.show()

arIm=np.array(image)
dft=np.ftt.ftt2(arIm)
mag=np.log(1+np.abs(np.fft.fftshift(dft)))


print("fourier image :")
plt.title("DFT")
plt.imshow(mag,cmap='gray')
plt.savefig("Image from fourier")
plt.show()

print("Image convert from fourier ")
plt.title(" Image from fourier")
inv_dft=np.fft.ifft2(dft)
plt.imshow(np.abs(inv_dft),cmap='gray')
plt.savefig("BackToImage.png")
plt.show()