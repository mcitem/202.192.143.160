from codes import *


# region snippet
x_train, y_train, l_train = load_dataset("data/train.npz")
fig() + scatter(x_train, y_train, c=l_train)
model = DeepLearning([2, 4, 4, 1])
fig() + structure(model)
f_train = merge_features([x_train, y_train])
model.demo_train('business')
model.show_learning_curve()
x_test, y_test, l_test = load_dataset("data/test.npz")
f_test = merge_features([x_test, y_test])
pred = model.predict(f_test)
print(accuracy(pred > 0.5, l_test))
model.reset_weights()
model.loss = 'mse'
model.demo_train('business_mse')
model.show_learning_curve()
pred = model.predict(f_test)
print(accuracy(pred > 0.5, l_test))
# endregion snippet
