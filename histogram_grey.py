import cv2
from matplotlib import pyplot as plt
import pandas as pd

img=cv2.imread("grey_scale.jpg")

histr=cv2.calcHist([img],[0],[256],[0,255])

df=pd.DataFrame(data=histr)

df.columns=["No. of pixels "]

plt.plot(histr)
plt.savefig("new_histogram.jpg")
plt.show()