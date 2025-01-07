from codes import *


# region snippet1
iris = data.get('iris-simple')
fig() + plot(iris)
# endregion snippet1


# region snippet2
blc = binary_linear_classifier()
# endregion snippet2


# region snippet3
blc.train(iris, alg=SVM())
fig() + plot(iris) + plot(blc)
# endregion snippet3
