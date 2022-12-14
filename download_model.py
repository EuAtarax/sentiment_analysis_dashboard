from flair.models import TextClassifier
import os

if not os.path.isdir('models'):
    os.mkdir('models')

classifier = TextClassifier.load('en-sentiment')
classifier.save('./models/sentiment-en-mix-distillbert_4.pt')
