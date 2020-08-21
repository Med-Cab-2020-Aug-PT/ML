import pickle
import pandas as pd
from time import time


nearest = pickle.load(open('nearest.pickle', 'rb'))
tfidf = pickle.load(open('tfidf.pickle', 'rb'))
df = pd.read_csv('../data/cannabis.csv')
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
    user_query = input("Can I help you? ")
    start = time()
    print(recommend(user_query))
    print(f'{time() - start:.2f} seconds to process')
