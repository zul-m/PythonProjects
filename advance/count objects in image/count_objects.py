import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv

from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly

image = cv2.imread("cars.png")
box, label, count = cv.detect_common_objects(image)
output = draw_bbox(image, box, label, count)

plt.imshow(output)
plt.show()

print("Number of cars in this image: " + str(label.count('car')))