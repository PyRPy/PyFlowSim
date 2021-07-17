import bpy
from random import randint

# 50 cubes at different locations
for i in range(50):
    bpy.ops.mesh.primitive_cube_add(location = [randint(-10, 10) for axis in 'xyz'])

# reference:
# https://pycon.org.il/2016/static/sessions/tamir-lousky.pdf
