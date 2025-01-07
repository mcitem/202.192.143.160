from codes import *

# region snippet
dt = 50
while inCurrentTask():
    if get_ultrasound()[0] - get_ultrasound()[1] > dt:
        go(20, 80, 1 / 6)
    elif get_ultrasound()[1] - get_ultrasound()[0] > dt:
        go(80, 20, 1 / 6)
    else:
        go(90, 90, 1 / 4)
# endregion snippet
