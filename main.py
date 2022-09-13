import sys
import os

from inputValidator import InputValidator
from pilImageProcessor import PILImageProcessor
from tesseractOcrProcessor import TesseractOCRProcessor
from excelProcessor import ExcelProcessor

from fileValidator import inputFileValidator
from titleExtraction import extractTitle
from authorsExtraction import extractAuthors
from isbnsExtraction import extractISBNs
from publishersExtraction import extractPublishers


def produceImageList(flag, path):
    '''Produces a list of file path(s), which contains the input file path or 
    the file paths of all the files in the input directory(depending on the flag).'''

    imgList = []
    if(flag == 0):
        imgList.append(path)
    else:
        dirList = os.listdir(path)
        for fileName in dirList:
            imgList.append(path + "\\" + fileName)
    return imgList


def processDataBeforeInsertion(title, authors, publishers, isbns):
    '''Processes the data to refine and join the output lists before insertion in excel file'''

    result = []

    strAuthors = ",".join(authors)
    strPublishers = ",".join(publishers)
    strISBNs = ",".join(isbns)

    result.append(title)
    result.append("".join(strAuthors.splitlines()))
    result.append(",".join(strPublishers.splitlines()))
    result.append(",".join(strISBNs.splitlines()))

    return result


def main(argv):
    try:
        ipValidator = InputValidator()
        imgProcessor = PILImageProcessor()
        ocrProcessor = TesseractOCRProcessor()

        # Name of the output excel file.
        outFileName = "output.xlsx"
        # Headers of the output excel file.
        headers = ["Title of the book", "Names of the authors",
                   "Publishers", "ISBN numbers"]
        excelProcessor = ExcelProcessor(outFileName, headers)

        # Validating the count of input command-line arguments
        if(len(argv) != 3):
            ipValidator.moduleUsageMessage(argv[0])
        else:
            flag = int(argv[1])
            # Validating the value of the parameter 'flag'
            ipValidator.checkFlagValidity(argv[0], flag)

            path = argv[2]

            imgList = produceImageList(flag, path)

            for i in range(len(imgList)):

                # Validating the format of input files against the permissible formats.
                if(inputFileValidator(imgList[i])):
                    img = imgProcessor.readImage(imgList[i])

                    # Text extraction using OCR
                    imgText = ocrProcessor.imageToString(img)
                    imgDict = ocrProcessor.imageToData(img)

                    # Extraction of title, authors, publishers and ISBN numbers from the recognised text output
                    title = extractTitle(imgDict)
                    authors = extractAuthors(imgText)
                    publishers = extractPublishers(imgText)
                    isbns = extractISBNs(imgText)

                    # print(imgText)
                    # print("Title: ", title)
                    # print("Authors: ", authors)
                    # print("Publishers: ", publishers)
                    # print("ISBNs: ", isbns)

                    data = processDataBeforeInsertion(
                        title, authors, publishers, isbns)

                    # Insert the output row in the excel file
                    excelProcessor.insertRow(i + 1, data)

        # Close the excel file
        excelProcessor.close()
    except Exception as error:
        # Catch and print exceptions
        print(error)


main(sys.argv)
