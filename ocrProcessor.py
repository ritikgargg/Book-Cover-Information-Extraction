from abc import ABC, abstractmethod

# Use of interface OCRProcessor provides the ability to use any library for OCR text extraction, preserving the overall code structure.


class OCRProcessor(ABC):

    @abstractmethod
    def imageToString(self, img):
        pass

    @abstractmethod
    def imageToData(self, img):
        pass
