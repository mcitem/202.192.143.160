from codes import *


# region snippet1
iris = data.get('iris')
feature, label = iris[0]
print("Feature : ", feature)
# endregion snippet1


# region snippet2
def select_features(feature):
    return feature[2:4]

iris2 = iris.map(select_features, on_field=0)
fig() + plot(iris2, type='scatter')
# endregion snippet2


# region snippet3
model = KMeans(K=3)
# endregion snippet3


# region snippet4
def select_features(feature):
    return feature[2:4]

iris2 = iris.map(select_features, on_field=0)
model.train(iris2.field(0))
fig() + plot(model, iris2, type='cluster_statistics')
# endregion snippet4


# region snippet5
model2 = KMeans(K=3)
model2.train(iris.field(0))
fig() + plot(model2, iris, type='cluster_statistics')
# endregion snippet5
