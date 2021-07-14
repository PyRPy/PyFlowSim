import bpy
import random

for i in range(0, 10):
    randomCoord = (random.randrange(-2, 3),
                    random.randrange(-2, 3),
                    random.randrange(-2, 3))
                    
    rot = random.randrange(0, 360)

    bpy.ops.mesh.primitive_cube_add()
    bpy.ops.transform.translate(value = randomCoord)
    #bpy.ops.transform.rotate(value=rot, axis=(0,1,0))
    
# Reference: Bbug ­ Belgian Blender User group