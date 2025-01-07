from codes import *

# region snippet
setTarget(3)
time = 0.1
while get_ultrasound()[2] > 100:
    go(100, 100, time)
setTarget(4)
time = 0.1
while get_ultrasound()[2] < 800:
    go(-100, -100, time)
setTarget(6)
while get_color()[0][0] < 128:
    go(100, 100, 0.1)
setTarget(7)
while get_color()[0][0] < 128:
    go(100, 100, 0.1)
while get_color()[0][1] < 128:
    go(-100, -100, 0.1)
# endregion snippet
