import bpy

#body
bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.resize(value=(1.2, 0.8, 1.5))

#head
bpy.ops.mesh.primitive_monkey_add()
bpy.ops.transform.translate(value=(0, -0.3, 2))

#arms
bpy.ops.mesh.primitive_cylinder_add()
bpy.ops.transform.translate(value=(2, 0, 0))
bpy.ops.transform.resize(value=(0.5, 0.5, 1.5))
# bpy.ops.transform.rotate(value=-0.523599, axis=(0, 1, 0))
bpy.ops.transform.rotate(value=-0.523599, orient_axis='Y') # use orient_axis
bpy.ops.mesh.primitive_cylinder_add()
bpy.ops.transform.translate(value=(-2, 0, 0))
bpy.ops.transform.resize(value=(0.5, 0.5, 1.5))
# bpy.ops.transform.rotate(value=0.523599, axis=(0, 1, 0))
bpy.ops.transform.rotate(value=-0.523599, orient_axis='Y') # use orient_axis

#legs
bpy.ops.mesh.primitive_cylinder_add()
bpy.ops.transform.translate(value=(0.7, 0, -3.5))
bpy.ops.transform.resize(value=(0.5, 0.5, 2))
bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value":(-1.4, 0, 0)})

# http://blender.freemovies.co.uk/blenderfiles/scripts/intro1.py