# Book Cover Information Extraction

**1. What does this program do?**

The objective of this assignment is to develop an application(essentially a command-line tool) that extracts the metadata from a collection of book cover pages. For this purpose, scanned images of the cover pages of books are supplied to the application, which then uses an **Optical Character Recognition(OCR)** library and employs certain **heuristics** to extract the following information from the scanned images:

- Title of the book
- Names of the authors
- Publishers
- ISBN numbers

The extracted information is written to a spreadsheet(in `.xlsx` format).

**2. A description of how this program works (i.e. its logic)**

The required inputs for the execution of this application are supplied as command-line arguments. These arguments include a **flag** that tells whether to process a single input file or a directory containing many files and **path** of the input file or the directory.

The input parameters are validated and appropriate messages are displayed in case of **incorrect** usage. `InputValidator` class has functions which assist in the validation of input.

Thereafter, depending on the case applicable, a list of file path(s) is prepared, which contains the input file path or the file paths of all the files in the input directory.

To validate the allowed input file formats, `inputFileValidator()` function from `fileValidator.py` is used. Doing so provides the ability to extend/remove the validation support for other formats of input files.

Next, we have maintained an interface `ImageProcessor`, which is implemented by `PILImageProcessor`. In our current implementation, we have used the **PIL library** for the purpose of reading images. However, the use of the interface `ImageProcessor` provides the ability to replace and employ some other library for image processing, without creating ripple effects. It also provides the flexibility to support data extraction from other formats of input files(by modifying the implementation of `readImage()` accordingly).

We have also maintained an interface `OCRProcessor`, which is implemented by `TesseractOCRProcessor`. In our current implementation, we have used **Tesseract-OCR** for the purpose of text extraction. However, due to the use of interface `OCRProcessor`, one can easily replace and employ some other OCR library, without distorting the code structure.

The `extractTitle()` function in `titleExtraction.py` is responsible for title extraction from the OCR output. For this purpose, we use the heuristic of finding the text with maximum height in the OCR output, since in general, the title of the book has the maximum font-size on the cover pages.

The `extractAuthors()` function in `authorsExtraction.py` is responsible for extracting authors from the OCR output. For this purpose, we have employed **Named Entity Recognition** using `spaCy`.

The `extractPublishers()` function in `publishersExtraction.py` is responsible for extracting publishers from the OCR output. For this purpose, we have employed **Named Entity Recognition** using `spaCy`.

The `extractISBNs()` function in `isbnsExtraction.py` is responsible for extracting ISBN numbers from the OCR output. For this purpose, **regex** matching(with appropriate fallback cases) is used.

`ExcelProcessor` is reponsible for creating and writing the output to a spreadsheet(in `.xlsx` format).

**3. How to compile and run this program**

**Installing all the dependencies**
Install the following libraries/dependencies for running different aspects of this implementation:

- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract)
- pytesseract
- spacy
- PIL
- xlsxwriter
- openpyxl
- pytest
- coverage
  etc.

NOTE: Make sure that tesseract is added in your **PATH**.

**Running the code**
To run this command-line tool, use the following command:
`python main.py <flag> <path>`
where,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<flag>` = A flag(**0 or 1**) that tells whether to process a single input file(**0**) or a directory containing many files(**1**).
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<path>` = Path of the input file or the directory.

For example,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`python main.py 0 images\image1.jpeg`
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`python main.py 1 images`
Provided you have `images\` and `images\image1.jpeg` in the working directory.

The output is written to an excel file(`output.xlsx`).

To run the tests (without **coverage**), use the command given below:
`pytest`

To run the tests (with **coverage**), you can use the following commands:
`coverage run -m pytest test_main.py`
`coverage report -m`
