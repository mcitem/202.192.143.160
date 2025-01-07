from codes import *

# region snippet
def groundglass_code(img, k=3):
    res = image_copy(img)
    H, W = get_image_size(img)
    for i in range(H):
        for j in range(W):
            offset_i = random_int(-k, k)
            offset_j = random_int(-k, k)
            src_i = i + offset_i
            src_j = j + offset_j
            src_i = bound(src_i, 0, H - 1)
            src_j = bound(src_j, 0, W - 1)
            res[i, j, :] = img[src_i, src_j, :]
    return res

img_groundglass = groundglass(img_sand, 3)
fig() + image(img_sand)
fig() + image(img_groundglass)
img_groundglass_ex = groundglass(img_sand, 8)
fig() + image(img_sand)
fig() + image(img_groundglass_ex)

def oil_painting_code(img, num_bin=2, region_size=4):
    H, W = get_image_size(img)
    res = image_copy(img)
    bin_assignment = compute_bin_assignment(img, num_bin)
    for i in range(0, H):
        for j in range(0, W):
            bb = get_bounding_box(i, j, region_size, H, W)
            y1, y2, x1, x2 = bb

            img_region = img[y1:y2, x1:x2, :]
            bin_assignment_region = bin_assignment[y1:y2, x1:x2]
            region_r, region_g, region_b = get_most_frequent_color(
                img_region, bin_assignment_region)

            res[y1:y2, x1:x2, 0] = region_r
            res[y1:y2, x1:x2, 1] = region_g
            res[y1:y2, x1:x2, 2] = region_b
    return res

img_painting = oil_painting(img_sand, 3, 4)
fig() + image(img_sand)
fig() + image(img_painting)

img_painting = oil_painting(img_sand, 20, 4)
fig() + image(img_sand)
fig() + image(img_painting)
# endregion snippet
