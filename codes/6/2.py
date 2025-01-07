from codes import *


# region snippet1
cifar_train = data.get('cifar10-small', subset='train')
fig() + plot(cifar_train)
# endregion snippet1


# region snippet2
label_names = cifar_train.meta['label_names']
print(label_names)
# endregion snippet2


# region snippet3
backbone = ssnet(h=32, w=32, c=3)
net = NNClassifier(backbone, ncls=10)
# endregion snippet3


# region snippet4
net.demo_train(cifar_train, epoch=5)
# endregion snippet4


# region snippet5
cifar_test = data.get('cifar10-small', subset='test')
img, label = cifar_test[100]
fig() + plot(img)
label_name = label_names[label]
pred = net.predict(img)
pred_name = label_names[pred]
print("Label is {}, Prediction is {}.".format(label_name, pred_name))
# endregion snippet5
