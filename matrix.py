# -*- coding: utf-8 -*-


# Main imports
import cv2
import numpy as np

# Reading image and template from txt files

image = np.loadtxt('image.txt', dtype=np.uint8)

template = np.loadtxt('template.txt', dtype=np.uint8)

# Running OpenCV functions to get coordinates of left top corner of template on image

res = cv2.matchTemplate(image, template, cv2.TM_SQDIFF)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

print("Координаты левого верхнего угла картинки по оси x:", min_loc[0], ", по оси y:", min_loc[1])
