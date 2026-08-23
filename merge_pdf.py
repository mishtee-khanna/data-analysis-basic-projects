from pypdf import PdfWriter

merger = PdfWriter()

pdfs = ["ai.pdf" , "f1.pdf"] # The name of your files
for pdf in pdfs:
    merger.append(pdf)

merger.write("projects.pdf") # Merged file name

