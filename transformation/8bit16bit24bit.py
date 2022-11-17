import cv2
import matplotlib.pyplot as plt
import numpy
import numpy as np

# Vanilla
img = cv2.imread("../images/albert.jpg", 0)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_GRAY2RGB))
plt.show()

# Bit parsing
for x in range(0, 8):
    img_temp = img.copy()
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            img_temp[i][j] = img[i][j] & (0b1 << x)
    plt.imshow(cv2.cvtColor(img_temp, cv2.COLOR_GRAY2RGB))
    plt.show()

# 16 bit image
newimg = np.zeros((img.shape[0], img.shape[1]), dtype=np.int64)
print(type(newimg[0][0]))
for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        newimg[i][j] = numpy.int64((img[i][j] / 255) * (2 ** 16))


plt.imshow(newimg, cmap="gray", vmin=0, vmax=(2 ** 16))
plt.show()

# 24 bit image
newimg = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.int64)
for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        newimg[i][j] = [img[i][j], img[i][j], img[i][j]]

plt.imshow(newimg, cmap="brg", vmin=0, vmax=255)
plt.show()
