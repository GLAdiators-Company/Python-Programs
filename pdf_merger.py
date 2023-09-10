from PyPDF2 import PdfReader,PdfWriter
import os

files = os.listdir()
pdfs = []
for pdf in files:
    if(pdf.endswith('.pdf')):
        pdfs.append(pdf)

merger = PdfWriter()
for i in pdfs:
    merger.append(i)

merger.write('Merged_pdf.pdf')



        
