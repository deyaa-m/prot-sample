# Imports
from langdetect import detect
from translate import Translator
from deep_translator import GoogleTranslator
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Read sample
with open('sample_0.json') as file:
    while (line := file.readline().rstrip()):

# Detect        
        lang = detect(line) 

# Translate
        translation = GoogleTranslator(source='auto', target='en').translate(line)

# Sentiment Analysis
        #tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

        #model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

        classifier = pipeline("sentiment-analysis")
        #classifier('it is good to see you.')
# output
        print(lang)
        print(translation)
        print(classifier(line))