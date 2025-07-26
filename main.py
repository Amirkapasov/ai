import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from gtts import gTTS
from commands import data_set

vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(list(data_set.keys()))

clf = LogisticRegression()
clf.fit(vectors, list(data_set.values()))

def text_to_speech(text):
    tts = gTTS(text=text, lang='ru')
    tts.save('output.mp3')
    os.system('output.mp3')
for i in range(110): 
    text = input('Введите ваш вопрос: ')
    text_vector = vectorizer.transform([text]).toarray()[0]
    answer = clf.predict([text_vector])[0]
    print(answer)
    text_to_speech(answer)
