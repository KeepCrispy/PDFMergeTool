# PDFMergeTool

I just needed to combine PDF files without giving away my first born.

Hope this helps someone else out as well.

requirements:
 pip install pdfrw 
 pip install PyPDF2


To customize for the files you want to combine just change the file names in following lines:

coverpages = PdfReader'file1.pdf').pages
mainpages = PdfReader('file2.pdf').pages

Cheers
