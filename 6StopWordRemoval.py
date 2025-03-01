from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "We are the students of computer science from CKt college"
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(example_sent)
filtered_sentence = [w for w in word_tokens if not w in stop_words]
print("word token:", word_tokens)
print("filtered Sentence:",filtered_sentence)
