from codes import *


# region snippet1
cifar_train = data.get('cifar10-small', subset='train')
fig() + plot(cifar_train)
# endregion snippet1

# region snippet2
hog = HOGExtractor()
hog_train = cifar_train.map(hog, on_field=0)
# endregion snippet2

# region snippet3
index = 10
hog_feature, label = hog_train[index]
fig() + plot(hog_feature, type='featvec')

index = 10
image, label = cifar_train[index]
fig() + plot(image, type='hog')
# endregion snippet3


# region snippet4
mlc = multi_class_classifier()
mlc.train(hog_train, alg=SVM())
# endregion snippet4


# region snippet5
acc1 = mlc.accuracy(hog_train)
print('Cifar_train Accuracy: ', acc1)
# endregion snippet5


# region snippet6
cifar_test = data.get('cifar10-small', subset='test')
fig() + plot(cifar_test)
hog_test = cifar_test.map(hog, on_field=0)
# endregion snippet6


# region snippet7
acc2 = mlc.accuracy(hog_test)
print('Cifar_test Accuracy: ', acc2)
# endregion snippet7


# region snippet8
index = 10
image, label = cifar_test[index]
fig() + plot(image)
print('label:', label)

hog_feature = hog(image)
prediction = mlc.predict(hog_feature)
print('prediction: ', prediction)
# endregion snippet8
