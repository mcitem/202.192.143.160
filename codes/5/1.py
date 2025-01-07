from codes import *

# region snippet
fig() + image(img_gray, cmap='gray')
print(type(img_gray))
print(img_gray.shape)
printMat2D(img_gray)
val = img_gray[18, 16]
print(val)
img_gray_copy = image_copy(img_gray)
img_gray_copy[18, 16] = 255
fig() + image(img_gray_copy, cmap='gray')
img_gray_copy = image_copy(img_gray)
img_gray_copy[18:25, 16] = 255
fig() + image(img_gray_copy, cmap='gray')
img_gray_copy = image_copy(img_gray)
img_gray_copy[18:25, 16:25] = 255
fig() + image(img_gray_copy, cmap='gray')
img_gray_copy = image_copy(img_gray)
img_gray_copy[10:, :] = 255
fig() + image(img_gray_copy, cmap='gray')
# 8
fig() + image(img_shibe)
print(img_shibe.shape)
fig() + image(img_shibe)
print(img_shibe.shape)
r = img_shibe[:, :, 0]
g = img_shibe[:, :, 1]
b = img_shibe[:, :, 2]
fig(1, 3) + [image(r, cmap='Reds'), image(g, cmap='Greens'), image(b, cmap='Blues')]
# endregion snippet
