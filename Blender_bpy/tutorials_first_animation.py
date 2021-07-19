import bpy
bpy.ops.mesh.primitive_cone_add()
bpy.ops.mesh.primitive_cone_add(location=(-3, 0, 0))

# animation setup
total_frames = 100
keyframe_interval = 10

# timeline
bpy.context.scene.frame_end = total_frames
bpy.context.scene.frame_start = 0

# add keyframes
for frame in range(0, total_frames + 1, keyframe_interval):
    bpy.context.scene.frame_set(frame)
    cone = bpy.data.objects['Cone']
    cone.location.x = frame / 25
    cone.keyframe_insert(data_path = 'location')
    
# https://tabreturn.github.io/code/blender/python/2020/11/01/a_quick_intro_to_blender_creative_coding-part_3_of_3.html
    