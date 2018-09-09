# Importing required modules
import PyPDF2
import os

# Define the read (PDF) and write (csv) folders
read_folder = os.path.abspath("")
write_folder = os.path.abspath("")

# create pdf file object
pdfFile = open(read_folder + '/' + 'PSAT2scores2018Sheet6.pdf', 'rb')
print('pdf file name = {}'.format(pdfFile))

# create a PDF reader object
pdfReader = PyPDF2.PdfFileReader(pdfFile)

# count number of pages in pdf file
pageCount = pdfReader.numPages
print('page count = {}'.format(pageCount))

# extract text from pdf document
for i in range(pageCount):
    page = pdfReader.getPage(i)
    page_content = page.extractText()
    if page_content != "":  # check for blank page
        print(page_content.encode('utf-8'))
    else:
        print('A blank page!')

# close the pdf file object
pdfFile.close()

#print(pdfPage.extractText())
#print(pdfPage)
