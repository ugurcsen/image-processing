import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("images/albert.jpg")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
plt.show()

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
