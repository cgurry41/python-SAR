import io
import shutil
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os


# converts pdf, returns its text content as a string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = io.StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
        #break #stop after the first page
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close()
    print(fname + ' moved')
    return text

#text_doc = convert('/Users/cgurry/PycharmProjects/crawler_3/Aircraft_Weapon_SARs/11-F-1176_JSF_Dec_2009_SAR.pdf')
#print(convert('/Users/cgurry/PycharmProjects/crawler_3/Aircraft_Weapon_SARs/11-F-1176_JSF_Dec_2009_SAR.pdf'))

#converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension.lower() == "pdf":
            pdfFilename = pdfDir + pdf
            text = convert(pdfFilename) #get string of text content of pdf
            textFilename = txtDir + pdf + ".txt"
            textFile = open(textFilename, "w") #make text file
            textFile.write(text) #write text to text file


#create directory for text files
def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

pdfDir = os.path.dirname(os.path.realpath(__file__)) + "/Final_SAR_PDFs/"
txtDir = os.path.dirname(os.path.realpath(__file__)) + "/Text_SARs/"
create_dir(txtDir)
convertMultiple(pdfDir, txtDir)