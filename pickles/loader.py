import pickle
import pandas as pd
import spacy
from time import time


start = time()
nlp = spacy.load("en_core_web_lg")


def tokenize(document):
    doc = nlp(document)
    return [
        token.lemma_.strip() for token in doc
        if not token.is_stop and not token.is_punct
    ]


nearest = pickle.load(open('pickles/nearest.pickle', 'rb'))
tfidf = pickle.load(open('pickles/tfidf.pickle', 'rb'))
df = pd.read_csv('data/cannabis.csv')
data = df.to_dict(orient='records')
for strain in data:
    strain['Effects'] = strain['Effects'].split(',')
    strain['Flavors'] = strain['Flavors'].split(',')
    strain['Nearest'] = strain['Nearest'].split(',')


def recommend(user_input):
    rec = nearest.kneighbors(
        tfidf.transform([user_input]).todense()
    )
    return dict(data[rec[1][0][0]])


if __name__ == '__main__':
    print(recommend('I have a headache'))
    print(time() - start, 'seconds')
