import re
import PyPDF2

# def parse_pdf() -> list:
#     with open("data.pdf", "rb") as file:
#         fr = PyPDF2.PdfFileReader(file)
#         data = fr.getPage(0).extractText()

#     regex_invoice_no = re.compile(r"Invoice Number\s*(INV-\d+)")
#     regex_order_no = re.compile(r"Order Number(\d+)")
#     regex_invoice_date = re.compile(r"Invoice Date(\S+ \d{1,2}, \d{4})")
#     regex_due_date = re.compile(r"Due Date(\S+ \d{1,2}, \d{4})")
#     regex_total_due = re.compile(r"Total Due(\$\d+\.\d{1,2})")

#     invoice_no = re.search(regex_invoice_no, data).group(1)
#     order_no = re.search(regex_order_no, data).group(1)
#     invoice_date = re.search(regex_invoice_date, data).group(1)
#     due_date = re.search(regex_due_date, data).group(1)
#     total_due = re.search(regex_total_due, data).group(1)

#     return [invoice_no, due_date, total_due]


# if __name__ == '__main__':
#     print(parse_pdf())

    #===============================

# from io import StringIO
# import re

# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.pdfpage import PDFPage
# from pdfminer.pdfparser import PDFParser

# output_string = StringIO()
# with open('testfile.pdf', 'rb') as in_file:
#     parser = PDFParser(in_file)
#     doc = PDFDocument(parser)
#     rsrcmgr = PDFResourceManager()
#     device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
#     interpreter = PDFPageInterpreter(rsrcmgr, device)
#     for page in PDFPage.create_pages(doc):
#         interpreter.process_page(page)

# finding = re.search(r"INV-\d+\n\d+\n.+\n.+\n\$\d+\.\d+", output_string.getvalue())

# invoice_no, order_no, _, due_date, total_due = finding.group(0).split("\n")

# print(invoice_no, order_no, due_date, total_due)

#===========================================
PDFfile = open("Datalink letters.pdf", "rb")
pdfread = PyPDF2.PdfFileReader(PDFfile)

i = 0
while i < pdfread.getNumPages():
    pageinfo = pdfread.getPage(i)
    print(pageinfo.extractText())
    i = i + 1
