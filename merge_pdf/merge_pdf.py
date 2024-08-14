# pip install pypdf3

from PyPDF3 import PdfFileMerger

pdfs = ['sample-1.pdf','sample-2.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_file.pdf")
merger.close()

