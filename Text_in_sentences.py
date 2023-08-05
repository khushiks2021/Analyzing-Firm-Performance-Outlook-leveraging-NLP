import PyPDF2
import re

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        text = ""

        for page_num in range(num_pages):
            page = reader.pages[page_num]
            content = page.extract_text()

            # Remove design elements and extra whitespaces
            content = re.sub(r'\n+', '\n', content)
            content = re.sub(r'\s{2,}', ' ', content)

            # Extract sentences from MD&A section
            sentences = re.findall(r'[A-Z][^.!?]*[.!?]', content)

            for sentence in sentences:
                # Omitting short sentences if needed
                if len(sentence) > 20:
                    text += sentence.strip() + '\n'

    return text

# Example usage
pdf_file_path = '/Users/chetanyabhan/Documents/Harshal Sir Project/Reliance.pdf'
output_file_path = pdf_file_path.replace('.pdf', '_cleantext.txt')

extracted_text = extract_text_from_pdf(pdf_file_path)

with open(output_file_path, 'w') as output_file:
    output_file.write(extracted_text)
