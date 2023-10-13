import PyPDF2

pdfFileObj = open("sample.pdf", "rb")

pdfReader = PyPDF2.PdfReader(pdfFileObj)

print(len(pdfReader.pages))

pageObj = pdfReader.pages[0]

print(pageObj.extract_text())

strona = pageObj.extract_text()

with open("strona.txt", "w") as f:
    f.write(strona)

