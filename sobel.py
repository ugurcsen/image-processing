import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("images/albert.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0],
])

sobelY = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1],
])
sobelX = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1],
])
imgSobelY = cv2.filter2D(src=img, ddepth=-1, kernel=sobelY)
imgSobelX = cv2.filter2D(src=img, ddepth=-1, kernel=sobelX)

imgSobelY = np.abs(imgSobelY)
imgSobelX = np.abs(imgSobelX)

img2 = np.add(imgSobelX, imgSobelY)
img3 = cv2.Sobel(img , -1 , 1, 0)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB))
plt.show()

plt.imshow(cv2.cvtColor(img3, cv2.COLOR_GRAY2RGB))
plt.show()

cv2.imshow("a", img),
cv2.waitKey(0)
cv2.destroyAllWindows()
