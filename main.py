import cv2
import numpy

image = cv2.imread('./imagens/war.jpg', 1)

blue, green, red = cv2.split(image)

imageGrayscalePondered = 0.299 * blue + 0.587 * green + 0.114 * red
imageGrayscalePondered = numpy.array(imageGrayscalePondered, dtype=numpy.uint8)

cv2.imshow('Image grayscale pondered', imageGrayscalePondered)
cv2.waitKey(0)
cv2.destroyAllWindows()
