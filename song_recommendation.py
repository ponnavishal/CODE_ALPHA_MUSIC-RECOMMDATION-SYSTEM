# -*- coding: utf-8 -*-
"""song recommendation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WBKL6ABZLllJUmah7rqYqHyJPod3uLUf
"""

import pandas as pd

df=pd.read_csv("/content/spotify_millsongdata.csv")

df

df.info()

df.describe()

df.dtypes

df.isnull()

df.isnull().count()

df.isnull().sum()

df.dropna()

df.shape

df.size

df =df.sample(5000).drop('link', axis=1).reset_index(drop=True)

df.size

df.head()

df['text'][0]

df.shape

df['text'] = df['text'].str.lower().replace(r'^\w\s', ' ').replace(r'\n', ' ', regex = True)

!pip install nltk
import nltk
nltk.download('punkt')

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenization(txt):
    tokens = nltk.word_tokenize(txt)
    stemming = [stemmer.stem(w) for w in tokens]
    return " ".join(stemming)

df['text'] = df['text'].apply(lambda x: tokenization(x))

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidvector = TfidfVectorizer(analyzer='word',stop_words='english')
matrix = tfidvector.fit_transform(df['text'])
similarity = cosine_similarity(matrix)

similarity[0]

df[df['song'] =='Bumming Around (Previously Unreleased)']

def recommendation(song_df):
    idx = df[df['song'] == song_df].index[0]
    distances = sorted(list(enumerate(similarity[idx])),reverse=True,key=lambda x:x[1])

    songs = []
    for m_id in distances[1:10]:
        songs.append(df.iloc[m_id[0]].song)

    return songs

recommendation('Bumming Around (Previously Unreleased)')