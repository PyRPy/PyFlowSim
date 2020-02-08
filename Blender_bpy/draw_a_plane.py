import bpy
bpy.ops.object.select_all(action='TOGGLE')
bpy.ops.object.delete(use_global=False)

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(1, 0, 0), constraint_axis=(True, False, False))

bpy.ops.transform.resize(value=(10, 1, 1), constraint_axis=(True, False, False))
bpy.ops.transform.resize(value=(1, 10, 1), constraint_axis=(False, True, False))
bpy.ops.transform.resize(value=(1, 1, 0.1), constraint_axis=(False, False, True))