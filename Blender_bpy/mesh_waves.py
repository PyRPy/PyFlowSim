# mesh curves
import bpy
import numpy as np
from math import sin

m = bpy.data.meshes.new('sin')

n = 100
m.vertices.add(n)
m.edges.add(n-1)

yVals = np.linspace(0, 10, 100)

for i, y in zip(range(n), yVals):
    m.vertices[i].co = (0, y, sin(y))

    if i < n-1:
        m.edges[i].vertices = (i, i+1)

o = bpy.data.objects.new('sin', m)

bpy.context.collection.objects.link(o)

# not working 
# https://github.com/Tlousky/blender_scripts/tree/master/pycon2016il
# https://blender.stackexchange.com/questions/145658/link-new-object-to-scene-with-python-in-2-8