from sklearn.feature_extraction.text import CountVectorizer


file = 'labels.txt'
with open(file, 'r') as f:
    labels = [line.strip() for line in f]


vectorizer = CountVectorizer()
print('loading clean training data and fit vectorizer...')
file = 'training.txt'
with open(file, 'r') as f:
    corpus = [line.strip().split('\t')[1] for line in f]
vectorizer.fit_transform(corpus)

input_files = ['cleaned_data.txt', 'clean_training.txt', 'clean_validation.txt', 'clean_test_set.txt']
for input_file in input_files:
    print('vectorize '+input_file+'...')
    if input_file == 'cleaned_data.txt':
        output_file = 'text_features.txt'
    else:
        output_file = 'text_feature_'+input_file
    print('save results to '+output_file+'...')
    with open(output_file, 'w') as outf, open(input_file, 'r') as inf:
        for line in inf:
            items = line.strip().split('\t')
            title = items[1]
            feature_vector = vectorizer.transform([title]).toarray()[0]
            label = labels.index(items[2])
            outf.write(','.join([str(i) for i in feature_vector]) + '\t' + str(label) + '\n')