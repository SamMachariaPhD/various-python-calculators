import os
import fitz  # PyMuPDF
import sys
import tempfile

def add_header_footer(input_pdf, header_text, footer_text, output_pdf):
    doc = fitz.open(input_pdf)
    total_pages = len(doc)
    
    for page_num in range(total_pages):
        page = doc[page_num]
        
        # Calculate text width for centering
        font = fitz.Font("helv")
        header_width = font.text_length(header_text, fontsize=8)
        
        # Create footer text with page number
        page_footer = f"Ref. Page [ {page_num + 1} ] {footer_text}"
        footer_width = font.text_length(page_footer, fontsize=8)
        
        # Add centered header
        header_x = (page.rect.width - header_width) / 2
        page.insert_text((header_x, 15), header_text,
                         fontsize=8, color=(0, 0, 1))
        
        # Add centered footer with page number
        footer_x = (page.rect.width - footer_width) / 2
        page.insert_text((footer_x, page.rect.height - 15), page_footer,
                         fontsize=8, color=(0, 0, 1))
        
        # Print progress
        progress = (page_num + 1) / total_pages * 100
        print(f"\rAdding header/footer: {progress:.1f}%", end="")
        sys.stdout.flush()
    
    print("\nSaving PDF with header and footer...")
    
    # Save to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_filename = temp_file.name
        doc.save(temp_filename)
    
    doc.close()
    
    # Replace the original file with the temporary file
    os.replace(temp_filename, output_pdf)

def combine_pdfs(pdf_list, output_pdf):
    doc = fitz.open()
    total_pdfs = len(pdf_list)
    
    for i, pdf_path in enumerate(pdf_list, 1):
        pdf_doc = fitz.open(pdf_path)
        doc.insert_pdf(pdf_doc)
        pdf_doc.close()
        
        # Print progress
        progress = i / total_pdfs * 100
        print(f"\rCombining PDFs: {progress:.1f}%", end="")
        sys.stdout.flush()
    
    print("\nSaving combined PDF...")
    doc.save(output_pdf)
    doc.close()

# Get list of all PDF files in the current folder
pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf') and f != "dekut_combined_pdf.pdf"]

# Sort the list of PDF files
pdf_files.sort()

# Output file path
output_pdf = "STIE07_Proceedings.pdf"

# Delete the output file if it already exists
if os.path.exists(output_pdf):
    os.remove(output_pdf)
    print(f"Deleted existing {output_pdf}")

header_text = "THE 7TH DeKUT INTERNATIONAL CONFERENCE ON SCIENCE, TECHNOLOGY, INNOVATION & ENTREPRENEURSHIP"
footer_text = "@2023 DeKUT INTERNATIONAL CONFERENCE"

# Combine PDFs
combine_pdfs(pdf_files, output_pdf)

# Add header and footer
add_header_footer(output_pdf, header_text, footer_text, output_pdf)

print("Process completed successfully!")
