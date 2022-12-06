# Import all the necessary Python librarires.
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import keras
import keras.layers as layers
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras.layers import Input
from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import LeakyReLU

# Build an architecture of the LeNet-5 convolutional neural network.
model = keras.Sequential()
model.add(layers.Conv2D(filters = 6, kernel_size = (3, 3), activation = 'relu', input_shape = (32, 32, 1)))
model.add(layers.AveragePooling2D())
model.add(layers.Conv2D(filters = 16, kernel_size = (3, 3), activation = 'relu'))
model.add(layers.AveragePooling2D())
model.add(layers.Flatten())
model.add(layers.Dense(units = 120, activation = 'relu'))
model.add(layers.Dense(units = 84, activation = 'relu'))
model.add(layers.Dense(units = 10, activation = 'softmax'))
model.compile(loss = keras.losses.categorical_crossentropy, optimizer = keras.optimizers.Adam(), metrics = ['accuracy'])

# Visualize the architecture of the convolutional neural network.
import visualkeras
visualkeras.layered_view(model)