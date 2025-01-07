from codes import *


# region snippet1
ds = data.get('facefeat')
faces = ds.field(0)
features = ds.field(1)
# endregion snippet1


# region snippet2
model = KMeans(K=7)
model.train(features)
# endregion snippet2


# region snippet3
pred = model.predict_all(features)
fig() + plot(faces, pred, type='face_cluster')
# endregion snippet3


# region snippet4
Ks = [4, 5, 6, 7, 8]
losses = []
for k in Ks:
    model = KMeans(K=k)
    model.train(features, visual=False)
    losses.append(model.loss)
fig() + plot(losses, Ks, type='elbow')
# endregion snippet4
