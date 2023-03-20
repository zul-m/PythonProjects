from instafilter import Instafilter

model = Instafilter("Lo-fi")
new_image = model("cars.png")

# To save the image, use cv2.
import cv2

cv2.imwrite("modified_image.png", new_image)