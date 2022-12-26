import cv2
import matplotlib.pyplot as plt


def transform(img, c, g):
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            img[i][j] = c * (img[i][j]**g)


img = cv2.imread("images/albert.jpg", 0)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_GRAY2RGB))
plt.show()

transform(img, 1, 0.8)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_GRAY2RGB))
plt.show()
