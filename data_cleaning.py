import re


def tokenize(text):
    text = text.lower()
    text = re.sub(r'[^a-z -]', r'', text)
    tokens = text.split()
    return tokens


def count_tokens(corpus, threshold=5):
    tokens_counts = dict()
    for text in corpus:
        for word in text:
            if word in tokens_counts:
                tokens_counts[word] += 1
            else:
                tokens_counts[word] = 1
    words_to_remove = []
    for word, count in tokens_counts.items():
        if count < threshold:
            words_to_remove.append(word)
    return tokens_counts, words_to_remove


def remove_rare_words(text, words_to_remove):
    tokens = tokenize(text)
    return ' '.join([word for word in tokens if word not in words_to_remove])


print('loading training data and count tokens...')
file = 'training.txt'
with open(file, 'r') as f:
    tokens_corpus = [tokenize(line.strip().split('\t')[1]) for line in f]
counts, words_to_remove = count_tokens(tokens_corpus)

print('preprocess subset.txt...')
input_file = 'subset.txt'
output_file = 'cleaned_data.txt'
with open(output_file, 'w') as outf, open(input_file, 'r') as inf:
    for line in inf:
        items = line.strip().split('\t')
        title = items[1]
        items[1] = remove_rare_words(title, words_to_remove)
        outf.write('\t'.join(items)+'\n')

# input_files = ['training.txt', 'validation.txt', 'test_set.txt']
# for input_file in input_files:
#     print('preprocess '+input_file+'...')
#     output_file = 'clean_'+input_file
#     with open(output_file, 'w') as outf, open(input_file, 'r') as inf:
#         for line in inf:
#             items = line.strip().split('\t')
#             title = items[1]
#             items[1] = ' '.join(remove_rare_words(title, words_to_remove))
#             outf.write('\t'.join(items) + '\n')
