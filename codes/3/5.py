from codes import *
# region snippet
visualize_data2D(train_x_s, train_y)
visualize_data3D(train_x_m, train_y)
model = linear_classifier()
model.train(train_x_m, train_y)
pred_y = model.predict(test_x_m)
acc = accuracy(pred_y, test_y)
print(acc)
model2 = linear_classifier()
model2.train(train_x_s, train_y)
pred_y = model2.predict(test_x_s)
acc = accuracy(pred_y, test_y)
print(acc)
# endregion snippet
