import os

import pdfx
from SAR_crawler import file2set


# repository for downloaded pdfs from a website
def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


current_path = os.path.dirname(os.path.realpath(__file__))
directory = '/SAR_PDFs'
pdf_file = current_path + '/DOD_SARs/pdf_list.txt'

# download pdfs from url's in pdf_list.txt
def downloader(url_set,pdf_path):
    print('Downloading pdfs to new SAR_PDFs folder')
    for url in url_set:
        print(url)
        if url[-4:] == '.pdf' or '.PDF':
            try:
                url = url.replace(' ', '%20', 1)
                pdf = pdfx.PDFx(url)
                pdf.download_pdfs(pdf_path)
                print(url)
            except:
                pass


url_set = file2set(pdf_file)
create_dir(current_path + directory)
downloader(url_set,current_path + directory)