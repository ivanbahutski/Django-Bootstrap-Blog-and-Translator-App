from googletrans import Translator


def translator(text):
    tr = Translator()
    translation = tr.translate(text=text, dest='ru', src='en')
    return translation.text
