import fitz
import re


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path) #type: ignore
    text = ""
    for page in doc: 
        text += page.get_text() 
        text = re.sub(r"(\w\.)(\w)", r"\1 \2", text)  # fix words separated by a full stop
        text = re.sub(r'\n+', ' ', text).replace('. ', '.\n') # remove extra newlines
        text = re.sub(r'\d+','',text) # remove numbers
        text = re.sub(r'[^\w\s]','',text)  # remove punctuation
        text = re.sub(r'\s+',' ',text) # remove extra space
        text = text.strip() # remove leading and trailing space
        text = text.split() # split text into words
        text = ' '.join(text) # join words into text
    return text

if __name__ == "__main__":
    text = extract_text_from_pdf("Reliance.pdf")
    with open('prased_text.txt', 'w') as f:
        f.write(text)

