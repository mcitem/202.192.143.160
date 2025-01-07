from codes import *

# region snippet
def turn_right():
    go(100, -100, 0.65)
    go(10, -10, 0.3)

for i in range(4):
    go(100, 100, 2.45)
    turn_right()
# endregion snippet
