from codes import *

# region snippet
def getLineLoc():
    colors = get_color()  # 4 * [R,G,B,L]
    res = -1
    res_max = 0
    for i in range(4):
        if colors[i][0] > res_max:
            res_max = colors[i][0]
            res = i
    return res

while get_color()[0][2] < 128:
    res = getLineLoc()
    if res == 0:
        go(-20, 40, 1 / 10)
    elif res == 1:
        go(30, 50, 1 / 10)
    elif res == 2:
        go(50, 30, 1 / 10)
    elif res == 3:
        go(40, -20, 1 / 10)
# endregion snippet
