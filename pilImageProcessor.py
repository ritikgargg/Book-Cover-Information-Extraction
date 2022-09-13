from imageProcessor import ImageProcessor
from PIL import Image

# Implementation of Interface ImageProcessor using PIL library.


class PILImageProcessor(ImageProcessor):

    def readImage(self, path):
        return Image.open(path)
