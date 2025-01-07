from codes import *


# region snippet
height, weight = load('hw.train')
fig() + scatter(height, weight)
net = MLP([1, 4, 4, 1])
fig() + structure(net)
net.train(height, weight)
t_height, t_weight = load('hw.test')
pred = net.predict(data=t_height)
fig() + scatter(t_height, pred) + scatter(t_height, t_weight)
error = net.compute_error(pred, t_weight)
print("Test error = %f" % error)
t_height, t_weight = load('hw.test')
pred = net.predict(data=t_height)
fig() + scatter(t_height, pred) + scatter(t_height, t_weight)
error = net.compute_error(pred, t_weight)
print("Test error = %f" % error)
# endregion snippet
