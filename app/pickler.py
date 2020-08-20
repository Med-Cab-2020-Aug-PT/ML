import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy


filename = '../data/cannabis.csv'
nlp = spacy.load("en_core_web_lg")


def tokenize(document):
    doc = nlp(document)
    return [
        token.lemma_.strip() for token in doc
        if not token.is_stop and not token.is_punct
    ]


df = pd.read_csv(filename)

tfidf = TfidfVectorizer(
    stop_words='english',
    tokenizer=tokenize,
    ngram_range=(1, 3),
    max_df=.97,
    min_df=3,
)

combo = df['Name'] + '. ' + df['Description'] + ' ' + df['Effects'] + ' ' + df['Flavors']
dtm = tfidf.fit_transform(combo)
dtm = pd.DataFrame(dtm.todense(), columns=tfidf.get_feature_names())

nearest_one = NearestNeighbors(n_neighbors=1, algorithm='kd_tree', n_jobs=-1)
nearest_one.fit(dtm)

data = df.to_dict(orient='records')

for strain in data:
    strain['Effects'] = strain['Effects'].split(',')
    strain['Flavors'] = strain['Flavors'].split(',')
    strain['Nearest'] = strain['Nearest'].split(',')


def recommend(user_input):
    rec = nearest_one.kneighbors(tfidf.transform([user_input]).todense())
    return dict(data[rec[1][0][0]])


if __name__ == '__main__':
    print(recommend("Happy"))
