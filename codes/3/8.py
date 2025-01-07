from codes import *


# region snippet1
iris = data.get('iris-simple')
fig() + plot(iris)
# endregion snippet1


# region snippet2
iris_train, iris_test = iris.split(7, 3)
fig() + plot(iris_train)
# endregion snippet2


# region snippet3
blc1 = binary_linear_classifier()
blc2 = binary_linear_classifier()
blc1.train(iris_train, alg=Perceptron(lr=0.2))
blc2.train(iris_train, alg=SVM())
fig() + plot(iris_train) + plot(blc1) + plot(blc2)
# endregion snippet3


# region snippet4
acc1 = blc1.accuracy(iris_test)
acc2 = blc2.accuracy(iris_test)
print('Perceptron Accuracy:', acc1)
print('SVM Accuracy:', acc2)
# endregion snippet4


# region snippet5
point = [2, 0.7]
fig() + plot(iris) + plot(blc1) + plot(blc2) + plot([point])
label1 = blc1.predict(point)
label2 = blc2.predict(point)
print('Perceptron Prediction: ', label1)
print('SVM Prediction: ', label2)
# endregion snippet5
