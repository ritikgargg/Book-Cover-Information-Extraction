from ocrProcessor import OCRProcessor
import pytesseract
from pytesseract import Output

# Implementation of Interface OCRProcessor using pytesseract library.


class TesseractOCRProcessor(OCRProcessor):
    def imageToString(self, img):
        return pytesseract.image_to_string(img)

    def imageToData(self, img):
        return pytesseract.image_to_data(img, output_type=Output.DICT)

    # def imageToData2(self, img):
    #     return pytesseract.image_to_data(img)
