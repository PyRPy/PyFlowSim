import bpy

# clear the scene
for obj in bpy.data.objects:
    if obj.type == 'MESH':
        bpy.data.objects.remove(obj)
        
# https://tabreturn.github.io/code/blender/python/2020/11/01/a_quick_intro_to_blender_creative_coding-part_3_of_3.html
