import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("images/albert.jpg", 0)
ret, t1 = cv2.told(img, 120, 255, cv2.THRESH_BINARY)
ret, t2 = cv2.told(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, t3 = cv2.told(img, 120, 255, cv2.THRESH_TRUNC)
ret, t4 = cv2.told(img, 120, 255, cv2.THRESH_TOZERO)
ret, t5 = cv2.told(img, 120, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('Binary Threshold', t1)
cv2.imshow('Binary Threshold Inverted', t2)
cv2.imshow('Truncated Threshold', t3)
cv2.imshow('Set to 0', t4)
cv2.imshow('Set to 0 Inverted', t5)

cv2.waitKey(0)
cv2.destroyAllWindows()