from PIL import Image
image = Image.open('array.png')

from numpy import asarray
data = asarray(image)

print(data)