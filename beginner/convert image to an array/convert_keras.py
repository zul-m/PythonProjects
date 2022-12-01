import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from keras_preprocessing.image import load_img
from keras_preprocessing.image import img_to_array

image = load_img("array.png")
data = img_to_array(image)

print(data)