from flair.models import TextClassifier

classifier = TextClassifier.load('en-sentiment')
classifier.save('./models/sentiment-en-mix-distillbert_4.pt')
