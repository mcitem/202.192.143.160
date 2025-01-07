from codes import *


# region snippet1
corpus = data.get('corpus')
doc = corpus[87]
fig() + plot(doc)
# endregion snippet1

# region snippet2
word_bags = corpus.map(split_words)
words = word_bags[87]
fig() + plot(words)
# endregion snippet2

# region snippet3
stop_words = load_stopwords()
fig() + plot(stop_words)
# endregion snippet3

# region snippet4
vocabulary = build_vocabulary(
    word_bags, stop_words=stop_words, frequency_threshold=5)
fig() + plot(vocabulary)
print('Vocabulary Length: ', len(vocabulary))
# endregion snippet4

# region snippet5
tf = TermFrequency(vocabulary)
tf_features = word_bags.map(tf)
feat = tf_features[87]
fig() + plot(feat)
# endregion snippet5

# region snippet6
tfidf = TFIDF(vocabulary, word_bags)
tfidf_features = word_bags.map(tfidf)
feat = tfidf_features[87]
fig() + plot(feat)
# endregion snippet6
