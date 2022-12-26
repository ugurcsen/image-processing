import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("images/albert.jpg", 0)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_GRAY2RGB))
plt.show()
plt.hist(img.ravel(), 256, [0, 256])
plt.show()
img = cv2.equalizeHist(img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_GRAY2RGB))
plt.show()
h = img.ravel()
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

k_size = 3
kernel1 = np.ones((k_size, k_size)) / (k_size ** 2)
# img2 = cv2.filter2D(src=img, ddepth=-1, kernel=kernel1)
img2 = np.zeros((img.shape[0], img.shape[1]), np.uint8)
kernel1_x_diff = int(kernel1.shape[0] / 2)
kernel1_y_diff = int(kernel1.shape[1] / 2)
for i in range(kernel1_x_diff, img.shape[0] - kernel1_x_diff):
    for j in range(kernel1_y_diff, img.shape[1] - kernel1_y_diff):
        img2[i][j] = np.sum(np.multiply(
            img[i - kernel1_x_diff:i + kernel1_x_diff + 1, j - kernel1_y_diff:j + kernel1_y_diff + 1], kernel1
        ))

plt.imshow(cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB))
plt.show()

plt.hist(img2.ravel(), 256, [0, 256])
plt.show()

kernel1 = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
img3 = cv2.filter2D(src=img, ddepth=-1, kernel=kernel1)
plt.imshow(cv2.cvtColor(img3, cv2.COLOR_GRAY2RGB))
plt.show()

img4 = cv2.medianBlur(img, 3)
plt.imshow(cv2.cvtColor(img4, cv2.COLOR_GRAY2RGB))
plt.show()
