import PyPDF2 as pdf
import os


pdf_folder = "./put_pdfs_here"

merge = pdf.PdfMerger()

pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

pdf_files.sort()

for file in pdf_files:
    merge.append(os.path.join(pdf_folder, file))

merge.write("merged.pdf")
merge.close()

print(f"Merged {len(pdf_files)} PDFs into 'merged.pdf'")
