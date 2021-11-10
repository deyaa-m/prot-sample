# Imports
from langdetect import detect
from deep_translator import GoogleTranslator
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import json
import glob


# Read sample
def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        payload = response["Body"].read().decode()
        sample = json.load(payload)
        orig_review = sample['review_text']
    #print(event)

    #for file in glob.glob('*.json'):
    #    with open(file) as file:
    #        sample = json.load(file)
    #        orig_review = sample['review_text'] #json.dumps(sample, indent=1)
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
        return 'Success!'
    except Exception as e:
        print(e)
        raise e
