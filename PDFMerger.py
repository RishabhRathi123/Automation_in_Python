import PyPDF2
import os #os' is imported to interact with the operating system, specifically to list files in the current directory.

# Specify the folder where the PDF files are located
folder_path = '/path/to/your/folder'

# List the specific PDF files you want to merge
pdf_files = ['file1.pdf', 'file2.pdf']

# Initialize PdfFileMerger
merger = PyPDF2.PdfFileMerger()

# Append each specified PDF file
for pdf_file in pdf_files:
    full_path = os.path.join(folder_path, pdf_file)
    merger.append(full_path)

# Write the combined PDF to a new file
output_path = os.path.join(folder_path, "combined.pdf")
merger.write(output_path)

print(f"PDF files merged into {output_path}")
