from codes import *

# region snippet
fig() + image(img_raw)
img_bgr = image_copy(img_raw)
tmp = image_copy(img_bgr[:, :, 0])
img_bgr[:, :, 0] = img_bgr[:, :, 2]
img_bgr[:, :, 2] = tmp
fig() + image(img_bgr)
img_warm = image_copy(img_raw)
img_warm = image_int2float(img_warm)
img_warm[:, :, 2] = img_warm[:, :, 2] / 2
img_warm = image_float2int(img_warm)
fig() + image(img_warm)
mat = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
]
img_bgr = image_copy(img_raw)
img_bgr = map_color_space(img_bgr, mat)
fig() + image(img_bgr)
mat = [
    [0.393, 0.769, 0.189],
    [0.349, 0.686, 0.168],
    [0.272, 0.534, 0.131]
]
img_retro = image_copy(img_raw)
img_retro = image_int2float(img_retro)
img_retro = map_color_space(img_retro, mat)
img_retro = bound(img_retro, 0, 255)
img_retro = image_float2int(img_retro)
fig() + image(img_retro)
rgb2lms_mat = [
    [17.8824, 43.5161, 4.11935],
    [3.45565, 27.1554, 3.86714],
    [0.0299566, 0.184309, 1.46709]
]
lms2rgb_mat = [
    [8.09444479e-02, -1.30504409e-01, 1.16721066e-01],
    [-1.02485335e-02, 5.40193266e-02, -1.13614708e-01],
    [-3.65296938e-04, -4.12161469e-03, 6.93511405e-01]
]
lms_mix_mat = [
    [0, 2.02344, -2.52581],
    [0, 1, 0],
    [0, 0, 1]
]
img_cb = image_copy(img_raw)
img_cb = image_int2float(img_cb)
img_cb = map_color_space(img_cb, rgb2lms_mat)
img_cb = map_color_space(img_cb, lms_mix_mat)
img_cb = map_color_space(img_cb, lms2rgb_mat)
img_cb = bound(img_cb, 0, 255)
img_cb = image_float2int(img_cb)
fig() + image(img_raw)
fig() + image(img_cb)
img_woodcut = image_copy(img_wzj)
img_woodcut = rgb2gray(img_woodcut)
img_woodcut = binary_threshold(img_woodcut, 170, 0, 255)
fig() + image(img_woodcut, cmap='gray')
# endregion snippet
