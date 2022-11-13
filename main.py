import nltk

nltk.download('punkt')
from textblob import TextBlob

text = "The titular threat of The Blob has always struck me as the ultimate movie"

blob = TextBlob(text)
for sentence in blob.sentences:
  print(sentence.sentiment.polarity)
