import PyPDF2

pdfFileObj = open('meetingminutes.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pdfReader.numPages
# Output: 19

pageObj = pdfReader.getPage(0)
pageObj.extractText()
# Output:
# 'OOFFFFIICCIIAALL  BBOOAARRDD  MMIINNUUTTEESS   Meeting of March 7,
# 2015        \n     The Board of Elementary and Secondary Education shall
# provide leadership and create policies for education that expand opportunities
# for children, empower families and communities, and advance Louisiana in an
# increasingly competitive global market. BOARD  of ELEMENTARY and  SECONDARY
# EDUCATION  '
pdfFileObj.close()

# Encrypted PDFs
pdfReader.isEncrypted
# Output: True

# Enter password 'rosebud' to open file
pdfReader.decrypt('rosebud')
# Output: 1

# Making PDF from two PDFs
pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfWriter.encrypt('swordfish')
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()