from codes import *


# region snippet
train_x = [27, 29, 34, 40, 42, 47, 48, 49, 50, 52, 52, 52, 54]
train_y = [6, 7.5, 9, 10.7, 12.8, 15.1, 16, 18.5, 19.4, 18.4, 19.7, 21.8, 21.7]
print_shape(train_x)
print_shape(train_y)
model = linear_regressor()
model.train(train_x, train_y)
model.show()
x = 40
pred_y = model.predict(x)
print(pred_y)
weights = model.get_weights()
print(weights)
k = weights[0]
b = weights[1]
print("k=", k)
print("b=", b)

def linear_function(x, k, b):
    y = k * x + b
    return y

x = 40
pred_y = linear_function(x, k, b)
print(pred_y)
train_y[5] = 30
model = linear_regressor()
model.train(train_x, train_y)
model.show()
# endregion snippet
