import bpy
from bpy.props import *

bl_info = {
    "name": "CreateSphereAddOn",
    "description": "This AddOn is 4th AddOn",
    "author": "dmiyamo3",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "support": "TESTING",
    "category": "Tutorial",
    "location": "",
    "warning": "",
    "wiki_url": "",
    "tracker_url":""
}

#
# TUTORIAL_OT_CreateSphere
#
class TUTORIAL_OT_CreateSphere(bpy.types.Operator):
  bl_idname = "tutorial.createsphere"
  bl_label = "CreateSphere"
  bl_options = {'REGISTER', 'UNDO'}
  
  #--- execute ---#
  def execute(self, context):
    self.report({'INFO'}, "Create Sphere")
    bpy.ops.mesh.primitive_ico_sphere_add()

    return {'FINISHED'}

#
# TUTORIAL_PT_CreateSpherePanel
#
class TUTORIAL_PT_CreateSpherePanel(bpy.types.Panel):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = "Tutrial4"
  bl_label = "PanelTitle4"

  #--- draw ---#
  def draw(self, context):
    layout = self.layout
    layout.operator(TUTORIAL_OT_CreateSphere.bl_idname, text = "Create")

#
# register classs
#
classes = [
  TUTORIAL_OT_CreateSphere,
  TUTORIAL_PT_CreateSpherePanel
]

#
# register
#
def register():
  for c in classes:
    bpy.utils.register_class(c)
    
#
# unregister()
#    
def unregister():
  for c in classes:
    bpy.utils.unregister_class(c)
    
#
# script entry
#    
if __name__ == "__main__":
  register()