from codes import *

# region snippet1
iris = data.get('iris-simple')
# endregion snippet1

# region snippet2
fig() + plot(iris)
# endregion snippet2

# region snippet3
blc = binary_linear_classifier()
# endregion snippet3

# region snippet4
blc.train(iris, alg=Perceptron())
# endregion snippet4


# region snippet5
blc1 = binary_linear_classifier()
blc1.train(iris, alg=Perceptron(lr=0.4))
blc2 = binary_linear_classifier()
blc2.train(iris, alg=Perceptron(lr=0.05))
blc3 = binary_linear_classifier()
blc3.train(iris, alg=Perceptron(w=[1, 1], b=1))
# endregion snippet5

# region snippet6
fig() + plot(iris) + plot(blc) + plot(blc1) + plot(blc2)
# endregion snippet6
