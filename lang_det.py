# Language Detection
from langdetect import detect

with open('sample_2.json') as file:
    while (line := file.readline().rstrip()):
        lang = detect(line) 
        print(lang)

#lang = detect("en, fr, ger")
