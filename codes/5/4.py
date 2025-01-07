from codes import *

# region snippet
def warp1(x, y):
    p = 0.4
    r = (x**2 + y**2)**0.5
    xp = x * (1 - p * r) / (1 - p)
    yp = y * (1 - p * r) / (1 - p)
    return xp, yp

img_anchor_warp = global_len_warp(img_anchor, warp1)
fig() + image(img_anchor)
fig() + image(img_anchor_warp)

def warp1(x, y):
    p = 0.4
    r = (x**2 + y**2)**0.5
    xp = x * (1 - p * r) / (1 - p)
    yp = y * (1 - p * r) / (1 - p)
    return xp, yp

img_warp_boy = global_len_warp(img_boy, warp1)
fig() + image(img_boy)
fig() + image(img_warp_boy)

def warp1_ex(x, y):
    p = 0.2
    r = (x**2 + y**2)**0.5
    xp = x * (1 - p * r) / (1 - p)
    yp = y * (1 - p * r) / (1 - p)
    return xp, yp

img_warp_boy_ex = global_len_warp(img_boy, warp1_ex)
fig() + image(img_boy)
fig() + image(img_warp_boy_ex)

def warp2(x, y):
    xp = sin(x) * x**2
    yp = sin(y) * y**2
    return xp, yp

img_warp_anchor_ex2 = global_len_warp(img_anchor, warp2)
fig() + image(img_warp_anchor_ex2)

def warp2(x, y):
    xp = sin(x) * x**2
    yp = sin(y) * y**2
    return xp, yp

img_warp_boy2 = global_len_warp(img_boy, warp2)
fig() + image(img_warp_boy2)

def warp_ex(x, y):
    xp = sin(x) * x
    yp = sin(y) * y
    return xp, yp

img_warp_boy_insane = global_len_warp(img_boy, warp_ex)
fig() + image(img_warp_boy_insane)
warp_params = [(125, 125), (0, 80), 120]
img_warp_local_anchor = local_warp_image(img_anchor, warp_params)
warp_params = [(125, 125), (0, 80), 60]
img_warp_local_anchor2 = local_warp_image(img_anchor, warp_params)
fig() + image(img_warp_local_anchor)
fig() + image(img_warp_local_anchor2)
warp_params = [(100, 100), (0, 20), 50]
img_warp_local_boy = local_warp_image(img_boy, warp_params)
fig() + image(img_warp_local_boy)
# endregion snippet
