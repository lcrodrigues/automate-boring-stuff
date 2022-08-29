# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import tkinter as tk
import PyPDF2

def text_to_salary(value):
    return float(value[:value.index(',') + 3].replace('.', '').replace(',', '.'))

# creating a pdf file object
pdfFileObj = open('holerite.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
text = pageObj.extract_text()
lines = text.split('\n')

SALARY_SUBSTRING = 'Código Descrição Referência Vencimentos Descontos'

salary_line = next(text for text in lines if SALARY_SUBSTRING in text)

salary = text_to_salary(salary_line)
print(salary)


# closing the pdf file object
pdfFileObj.close()

window = tk.Tk()
greeting = tk.Label(text="Select your file:")

greeting.pack()
window.mainloop()
