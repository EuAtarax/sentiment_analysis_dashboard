import re
import streamlit as st
from flair.models import TextClassifier
from flair.data import Sentence
from segtok.segmenter import split_single


# initializing the flair model
@st.cache(allow_output_mutation=True)
def get_classifier():
    # classifier = TextClassifier.load('en-sentiment')
    classifier = TextClassifier.load("./models/sentiment-en-mix-distillbert_4.pt")
    return classifier


# setting helper functions
def clean(raw_string: str):
    """ Remove hyperlinks and markup """
    result = re.sub("<[a][^>]*>(.+?)</[a]>", 'Link.', raw_string)
    result = re.sub('&gt;', "", result)
    result = re.sub('&#x27;', "'", result)
    result = re.sub('&quot;', '"', result)
    result = re.sub('&#x2F;', ' ', result)
    result = re.sub('<p>', ' ', result)
    result = re.sub('</i>', '', result)
    result = re.sub('&#62;', '', result)
    result = re.sub('<i>', ' ', result)
    result = re.sub("\n", '', result)
    return result


def make_sentences(text):
    """ Break apart text into a list of sentences """
    sentences = [sent for sent in split_single(text)]
    return sentences


def predict(sentence, clf):
    """ Predict the sentiment of a sentence """
    if sentence == "":
        return 0
    text = Sentence(sentence)
    clf.predict(text)
    value = text.labels[0].value
    if value == 'POSITIVE':
        result = text.labels[0].score
    else:
        result = -text.labels[0].score
    return {'result': round(result, 3),
            'sentiment': value}


def get_scores(sentences, clf):
    """ Call predict on every sentence of a text """
    results = []
    for sen in sentences:
        results.append(predict(sen, clf))
    return results


def get_sum(scores):
    result = sum([x['result'] for x in scores])
    sentiment = get_sentiment(result)
    return result, sentiment


def get_sentiment(scores):
    if scores <=0.5:
        return 'Negative'
    elif scores >= 0.5:
        return 'Positive'
    else:
        return 'Neutral'


