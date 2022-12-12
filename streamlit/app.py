import streamlit as st
import utils


st.set_option("deprecation.showfileUploaderEncoding", False)
classifier = utils.get_classifier()

st.title("Sentiment analysis web app")

text = st.text_input("Enter English text to be analyzed.")

if st.button("Analyze sentiment") and text is not None:
    clean_text = utils.clean(text)
    sentences = utils.make_sentences(clean_text)
    score = utils.get_scores(sentences, classifier)
    sum_scores, sentiment = utils.get_sum(score)
    st.write(f'Overall sentiment is {sentiment} and total score is {round(sum_scores,2)}')
