from codes import *

# region snippet
train_x = [27, 29, 34, 40, 42, 47, 48, 49, 50, 52, 52, 52, 54]
train_y = [6, 7.5, 9, 10.7, 12.8, 15.1, 16, 18.5, 19.4, 18.4, 19.7, 21.8, 21.7]
model = linear_regressor()
model.train(train_x, train_y)
model.show()
def mse_error(pred, y):
    error = 0
    for i in range(len(pred)):
        error = error + (y[i] - pred[i])**2
        error = error / len(pred)
    return error
print(mse_error(train_y, train_y))
pred_y = model.predict(train_x)
error = mse_error(pred_y, train_y)
print(error)

def compute_error(model, x, y):
    pred = model.predict(x)
    error = mse_error(pred, y)
    return error

model2 = poly_regressor(3)
model2.train(train_x, train_y)
model2.show()
print(compute_error(model2, train_x, train_y))
model3 = poly_regressor(30)
model3.train(train_x, train_y)
model3.show()
print(compute_error(model3, train_x, train_y))

test_x = [23, 31, 32, 38, 40, 45, 49, 50, 50, 51, 51, 53, 55]
test_y = [6.3, 7.2, 9.1, 10.5, 12.9, 15.5,
          15.9, 18.3, 19.7, 18.9, 19.3, 21.3, 22.1]
print("线性回归误差:", compute_error(model, test_x, test_y))
print("3次多项式误差:", compute_error(model2, test_x, test_y))
print("30次多项式误差:", compute_error(model3, test_x, test_y))
# endregion snippet
