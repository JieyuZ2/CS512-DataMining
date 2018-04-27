import numpy as np
import re
from sklearn import linear_model
from sklearn.feature_extraction.text import CountVectorizer
regex = re.compile('[^a-z\ -]')


def load_data(file):
    X = []
    y = []
    with open(file, 'r') as f:
        for line in f:
            items = line.strip().split('\t')
            title = items[1]
            label = items[2]
            X.append(vectorizer.transform([title]).toarray()[0])
            y.append(labels.index(label))
    X = np.array(X)
    y = np.array(y)
    return X, y




labels_file = 'labels.txt'
with open(labels_file, 'r') as f:
    labels = [line.strip() for line in f]

vectorizer = CountVectorizer(lowercase=True, min_df=5, stop_words=None)
print('loading clean training data and fit vectorizer...')
file = 'training.txt'
with open(file, 'r') as f:
    corpus = [regex.sub('', line.strip().split('\t')[1].lower()) for line in f]
vectorizer.fit(corpus)


input_files = ['training.txt', 'validation.txt', 'test_set.txt']
for file in input_files:
    X, y = load_data(file)
