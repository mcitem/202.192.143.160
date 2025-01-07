from codes import *

# region snippet
dt = 50
while get_color()[0][2] < 128:
    if get_ultrasound()[0] - get_ultrasound()[1] > dt:
        go(20, 80, 1 / 12)
    elif get_ultrasound()[1] - get_ultrasound()[0] > dt:
        go(80, 20, 1 / 12)
    else:
        go(90, 90, 1 / 12)
# endregion snippet
