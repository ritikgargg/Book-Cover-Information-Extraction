import xlsxwriter


class ExcelProcessor:

    def addHeaders(self, headers):
        '''Function to add headers to the worksheet '''
        self.insertRow(0, headers)

    def __init__(self, outFileName, headers):
        '''Initialises the workbook and worksheet to be used and add headers to the worksheet'''

        self.workbook = xlsxwriter.Workbook(outFileName)
        self.worksheet = self.workbook.add_worksheet()

        self.addHeaders(headers)

    def insertRow(self, rowIdx, data):
        '''To insert a row of data at the specified row index'''

        for i in range(len(data)):
            self.worksheet.write(rowIdx, i, data[i])

    def close(self):
        '''Close the workbook'''
        self.workbook.close()
