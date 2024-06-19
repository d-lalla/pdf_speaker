import pyttsx3,PyPDF2
import os

#current path
current_dir = "G:\Il mio Drive\Dome\Dev\pdf_to_audio_converter"

pdfreader = PyPDF2.PdfReader(open(os.path.join(current_dir,'book.pdf'), 'rb'))
speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
# save mp3
speaker.save_to_file(clean_text, os.path.join(current_dir,'story.mp3'))
speaker.runAndWait()

speaker.stop()