import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("images/albert.jpg", cv2.IMREAD_GRAYSCALE)
s_vs_p = .5
amount = .04

img2 = img.copy()
for x in range(int(img.shape[0]*img.shape[1]*amount*s_vs_p)):
    img2[np.random.randint(0,img.shape[0])][np.random.randint(0,img.shape[1])] = 255

for x in range(int(img.shape[0] * img.shape[1] * amount * (1-s_vs_p))):
    img2[np.random.randint(0, img.shape[0])][np.random.randint(0, img.shape[1])] = 0


# plt.imshow(img2, cmap="gray")
# plt.show()
plt.hist(img.ravel(), 256, [0, 256])
plt.show()
plt.hist(img2.ravel(), 256, [0, 256])
plt.show()
cv2.imshow("a", img)
cv2.imshow("b", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
