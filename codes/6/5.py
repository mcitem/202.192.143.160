
from codes import *


# region snippet1
ucf = data.get('ucf-small', subset='train')
video, label = ucf[1]
fig() + plot(video)
# endregion snippet1


# region snippet2
frame0 = video[5]
frame1 = video[6]
fig(2, 1) + [plot(frame0), plot(frame1)]
# endregion snippet2


# region snippet3
flow = optical_flow(frame0, frame1)
# endregion snippet3


# region snippet4
frame_flow = image_add_flow(frame0, flow)
fig() + plot(frame_flow)
# endregion snippet4


# region snippet5
flow_x, flow_y = split_flow(flow)
fig(2, 1) + [plot(flow_x), plot(flow_y)]
# endregion snippet5


# region snippet6
flowvideo = optical_flow_video(video)
flow0 = flowvideo[0]
video_arrow = video_add_flow(video, flowvideo)
fig() + plot(video_arrow)
# endregion snippet6
