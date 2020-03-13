import PyPDF2

pdfFileObj = open('servidores.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)
content =""
for i in range(0, pdfReader.numPages):
    content += pdfReader.getPage(i).extractText() + "\n"

content = " ".join(content.replace(u"\xa0", " ").strip().split())    

content.readline()
print(content)