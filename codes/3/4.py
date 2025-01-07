from codes import *


# region snippet
train_x = [60, 56, 60, 55, 60, 57, 65, 60, 62, 59, 43, 52, 41, 45, 43, 50, 46, 52, 56, 56]
train_y = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
model = linear_classifier()
model.train(train_x, train_y)
model.show()
x = 60
pred_y = model.predict(x)
print(pred_y)
weights = model.get_weights()
print(weights)
k = weights[0]
b = weights[1]
print("k=", k)
print("b=", b)
def decision_function(x, k, b):
    if k * x + b > 0:
        return 1
    else:
        return -1
pred = decision_function(3, 2, -5.5)
print(pred)
pred = decision_function(3, 2, -6.5)
print(pred)
k, b = model.get_weights()
x = 60
pred_y = decision_function(x, k, b)
print(pred_y)
def accuracy(pred, y):
    right = 0
    total = 0
    for i in range(len(pred)):
        if pred[i] == y[i]:
            right = right + 1
        total = total + 1
    acc = right / total
    return acc
pred_y = model.predict(train_x)
acc = accuracy(pred_y, train_y)
print(acc)
model2 = linear_regressor()
model2.train(train_x, train_y)
model2.show()
# endregion snippet
