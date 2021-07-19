# animation variables
total_frames = 100
keyframe_interval = 10

# define a one hundred frame timeline
bpy.context.scene.frame_end = total_frames
bpy.context.scene.frame_start = 0

# add keyframes
for frame in range(0, total_frames + 1, keyframe_interval):
    bpy.context.scene.frame_set(frame)
    cone = bpy.data.objects['Cone']
    cone.location.x = frame / 25
    cone.keyframe_insert(data_path='location')