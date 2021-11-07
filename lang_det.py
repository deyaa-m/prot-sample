# Imports
from langdetect import detect
from translate import Translator
from deep_translator import GoogleTranslator

# Read sample
with open('sample_0.json') as file:
    while (line := file.readline().rstrip()):

# Detect        
        lang = detect(line) 

# Translate
        translation = GoogleTranslator(source='auto', target='en').translate(line)
        print(lang)
        print(translation)