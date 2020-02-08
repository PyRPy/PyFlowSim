import bpy

def delete_all():
    for item in bpy.context.scene.objects:
        bpy.context.scene.objects.unlink(item)
        
    for item in bpy.data.objects:
        bpy.data.objects.remove(item)
        
    for item in bpy.data.meshes:
        py.data.meshes.remove(item)
        
    for item i bpy.data.materials:
        bpy.data.materials.remove(item)
        
def add_cone():
    bpy.ops.mesh.primitive_cone_add()
    
if __name__ == "__main__":
    delete_all()
    add_cone()
            
# ref : 3D Modeling and Printing by Python
    
