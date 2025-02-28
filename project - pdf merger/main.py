import PyPDF2
import os # Important to manipulate files.

merger = PyPDF2.PdfMerger()
list_files = os.listdir("files")
print(list_files) 

for file in list_files:
    if ".pdf" in file: # Makes sure that it is a pdf file.
        merger.append(f"files/{file}")
        
merger.write("Documentação Completa.pdf")