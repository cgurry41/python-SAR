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
        break #stop after the first page
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close()
    return text


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

create_directory('Final_SAR_PDFs')


for filename in os.listdir('SAR_PDFs'):
    print(filename)
    if filename[-4:] == 'json':
        os.remove('SAR_PDFs/' + filename)
        continue

    if convert('SAR_PDFs/' + filename)[0:8] == 'Selected':
        shutil.copy('SAR_PDFs/'+filename,'Final_SAR_PDFs/'+filename)
