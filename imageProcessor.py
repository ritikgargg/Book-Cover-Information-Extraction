from abc import ABC, abstractmethod

# Use of the interface ImageProcessor provides the ability to use any library for image processing, preserving the overall code structure.
# Different implementations of readImage() function also provides the flexibility to support data extraction from other formats of input files.


class ImageProcessor(ABC):

    @abstractmethod
    def readImage(self, path):
        pass
