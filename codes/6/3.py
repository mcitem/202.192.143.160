
from codes import *


# region snippet1
face_photos = data.get('faces')
photo = face_photos[109]
fig() + plot(photo)
# endregion snippet1


# region snippet2
photo_d = detect_faces(photo)
fig() + plot(photo_d)
# endregion snippet2


# region snippet3
faces = crop_aligned_faces(photo_d)
fig(2, 1) + [plot(faces[0]), plot(faces[1])]
# endregion snippet3


# region snippet4
feature1 = extract_face_feature(faces[0])
feature2 = extract_face_feature(faces[1])
# endregion snippet4


# region snippet5
fig(2, 1) + [plot(feature1, type='featvec'), plot(feature2, type='featvec')]
# endregion snippet5
