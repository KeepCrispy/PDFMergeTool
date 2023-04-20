from pdfrw import PdfReader, PdfWriter, PageMerge, PdfDict, PdfObject
from PyPDF2 import PdfFileWriter, PdfFileReader


coverpages = PdfReader'file1.pdf').pages

mainpages = PdfReader('file2.pdf').pages

mergedpages = coverpages + mainpages;

output = PdfWriter()

#Get standard size
baseRects = [[float(num) for num in page.MediaBox] for page in mainpages]
height = max(x[3] - x[1] for x in baseRects)
width = max(x[2] - x[0] for x in baseRects)

mbox = [0, 0, width, height]

for page in mergedpages:
    newpage = PageMerge()
    newpage.mbox = mbox              # Set boundaries of output page
    newpage.add(page)                # Add one old page to new page
    image = newpage[0]               # Get image of old page (first item)
    image.x = (width - image.w) / 2  # Center old page left/right
    image.y = (height - image.h)     # Move old page to top of output page
    output.addpage(newpage.render())


output.write(directoryName +'Combined.pdf' )
