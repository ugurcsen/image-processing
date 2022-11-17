import cv2
import matplotlib.pyplot as plt
import numpy as np


def transform(img, c):
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            img[i][j] = c * np.log(1 + img[i][j])


img = cv2.imread("../images/albert.jpg", 0)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_GRAY2RGB))
plt.show()

transform(img, 35)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_GRAY2RGB))
plt.show()
