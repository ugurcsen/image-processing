import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("images/albert.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1],
]) / 16

img2 = np.zeros(img.shape, dtype=np.uint8)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img2[i][j] = 1 * (img[i][j]**1.5) #img2[i][j] = 15*np.log(1 + img[i][j]) #np.round(np.sum(np.multiply(img[i - 1:i + 2, j - 1:j + 2], kernel)))

# plt.imshow(img2, cmap="gray")
# plt.show()

cv2.imshow("a", img),
cv2.imshow("b", img2),
cv2.waitKey(0)
cv2.destroyAllWindows()
