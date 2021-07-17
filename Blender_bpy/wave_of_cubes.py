# draw a wave of cubes
# https://pycon.org.il/2016/static/sessions/tamir-lousky.pdf

import bpy
from math import sin

for i in range(50):
    x, y, z = 0, i, sin(i)
    bpy.ops.mesh.primitive_cube_add(location = (x, y, z))
    
