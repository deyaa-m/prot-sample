# Imports
from langdetect import detect
#from translate import Translator
from deep_translator import GoogleTranslator
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import json
import glob


# Read sample
for file in glob.glob('*.json'):
    with open(file) as file:
        sample = json.load(file)
        orig_review = sample['review_text'] #json.dumps(sample, indent=1)
        #print(orig_review)
# Detect        
        lang = detect(orig_review) 

# Translate
        eng_review = GoogleTranslator(source='auto', target='en').translate(orig_review)

# Sentiment Analysis
        #tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

        #model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

        classifier = pipeline("sentiment-analysis")

# output
        print(orig_review)
        print(eng_review)
        print(classifier(eng_review))