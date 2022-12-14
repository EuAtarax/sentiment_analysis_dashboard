# Sentiment Analysis of an input text using flair - Dashboard
A simple streamlit app utilizing a Text classification BERT model from flair package.
It is embedded in a streamlit app and is able to analyze the sentiment of a given text.
Text input has to be in English (v1.0), can be multiple sentences and will be analyzed after pressing the button.
Sentiment can be either Positive, Negative or Neutral.

repo: nkhoss/streamlit_app_ex4

## Docker commands (in 'aufgabe4_khoss' folder):
- docker compose build
- docker compose up
Beware, that an evironment variable "STREAMLIT_SERVER_PORT" needs to be set!

## Or via Dockerfile:
- docker build -t sentiment_analysis .
- docker run sentiment_analysis -p 80

The docker repo is automatically updated on every push using github actions. This action may take up to 10 minutes.
For more informations, see .github/workflows/main.yml

## Note:
Unfortunately, the image is 7GB big and therefore quite heavy.
I was not able to reduce the size significantly.
- Also, the model is well over 200mb big, therefore it is uploaded using `git lfs`. Please be mindful of that.


Link to azure website:
https://ds21m011-sentiment-analysis.azurewebsites.net
