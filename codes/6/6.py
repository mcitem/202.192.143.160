from codes import *


# region snippet1
trainset = data.get('ucf-small', subset='train')
video, label = trainset[10]
fig() + plot(video)
print(trainset.meta['label_names'][label])
# endregion snippet1


# region snippet2
flowvideo = optical_flow_video(video)
feat = hof(flowvideo)
fig() + plot(feat, type='featvec')
# endregion snippet2


# region snippet3
trainflow = trainset.map(optical_flow_video, on_field=0)
trainhof = trainflow.map(hof, on_field=0)
print(trainhof[10][0].shape)
# endregion snippet3


# region snippet4
mlc = multi_class_classifier()
mlc.train(trainhof, alg=SVM())
# endregion snippet4


# region snippet5
acctrain = mlc.accuracy(trainhof)
print('Train Accuracy:', acctrain)
# endregion snippet5


# region snippet6
testset = data.get('ucf-small', subset='test')
testflow = testset.map(optical_flow_video, on_field=0)
testhof = testflow.map(hof, on_field=0)
acctest = mlc.accuracy(testhof)
print('Test Accuracy:', acctest)
# endregion snippet6
