from codes import *


# region snippet
# 1
diff_level = load_private("./data/tmp/diff_level")
# 2
train_data = load_train_data()
print(len(train_data))
print(train_data[0:5])
test_data = load_test_data()
print(len(test_data))
print(test_data[0:5])
# 3
features = []
labels = []
for path, label in train_data:
    features.append(extract_features(path, diff_level))
    labels.append(int(label))

def get_feats_labels(data, diff_level):
    features = []
    labels = []
    for path, label in data:
        features.append(extract_features(path, diff_level))
        labels.append(int(label))
    return features, labels

train_feats, train_labels = get_feats_labels(train_data, diff_level)
print(train_feats[0:5])
print(train_labels[0:5])
save_private([train_feats, train_labels], "./data/tmp/train_features")
train_feats, train_labels = load_private("./data/tmp/train_features")
print(train_feats[0:5])
print(train_labels[0:5])
test_feats, test_labels = get_feats_labels(test_data, diff_level)
save_private([test_feats, test_labels], "./data/tmp/test_features")
# 4
train_data = load_binary_train_data("primary", "junior")
print(len(train_data))
print(train_data[0:5])
test_data = load_binary_test_data("primary", "junior")
test_feats, test_labels = get_feats_labels(test_data, diff_level)
save_private([train_feats, train_labels], "./data/tmp/pri_jun_train_features")
save_private([test_feats, test_labels], "./data/tmp/pri_jun_test_features")
# 5
model = linear_classifier()
model.train(train_feats, train_labels)
pred_y = model.pred(test_feats)
acc = accuracy(pred_y, test_labels)
print(acc)
# endregion snippet
