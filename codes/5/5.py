from codes import *

# region snippet
points = detect_keypoints(img_wzj)
img_with_points = draw_points(img_wzj, points)
fig() + image(img_with_points)
mouth_left = points[48]
mouth_right = points[54]
left_eyebrow = points[19]
right_eyebrow = points[24]

cust_points = [mouth_left, mouth_right, left_eyebrow, right_eyebrow]
img_with_points = draw_points(img_wzj, cust_points)
fig() + image(img_with_points)
warp_params = [
    [left_eyebrow, (0, -5), 35],
    [right_eyebrow, (0, -5), 35],
    [mouth_left, (-5, -5), 40],
    [mouth_right, (5, -5), 40]
]

sticker = make_sticker(img_wzj, warp_params)
fig() + gif(sticker)
# endregion snippet
