from codes import *


# region snippet1
corpus, vocab, tf_feat, tfidf_feat = data.get('text-feat')
# endregion snippet1

# region snippet2
tfidf_mat = to_matrix(tfidf_feat)
print("文档-词矩阵尺寸：", tfidf_mat.shape)
# endregion snippet2

# region snippet3
model = topic_model(vocab, tfidf_mat, num_topics=8)
model.train()
# endregion snippet3

# region snippet4
t_mat = model.tmatrix
w_mat = model.wmatrix
print('Size of T Matrix: ', t_mat.shape)
print('Size of W Matrix: ', w_mat.shape)
# endregion snippet4

# region snippet5
high_freqs = model.extract_highfreqs(top_n=5)
fig() + plot(high_freqs)
# endregion snippet5

# region snippet6
id = 87
doc = corpus[id]
fig() + plot(doc)
#
topic_weights = w_mat[id]
fig(2, 1) + [plot(high_freqs), plot(topic_weights)]
# endregion snippet6
