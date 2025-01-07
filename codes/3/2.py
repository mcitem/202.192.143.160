from codes import *


# region snippet
train_x = [27, 29, 34, 40, 42, 47, 48, 49, 50, 52, 52, 52, 54]
train_y = [6, 7.5, 9, 10.7, 12.8, 15.1, 16, 18.5, 19.4, 18.4, 19.7, 21.8, 21.7]
model = poly_regressor(2)
model.train(train_x, train_y)
model.show()
x = 40
pred_y = model.predict(x)
print(pred_y)
model = poly_regressor(3)
model.train(train_x, train_y)
model.show()
model = poly_regressor(10)
model.train(train_x, train_y)
model.show()
model = poly_regressor(30)
model.train(train_x, train_y)
model.show()
train_y[5] = 30
model = poly_regressor(2)
model.train(train_x, train_y)
model.show()
model = poly_regressor(30)
model.train(train_x, train_y)
model.show()
# endregion snippet
