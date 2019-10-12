import os
import bpy
from bpy.props import *
# import tkinter
# from tkinter import filedialog

bl_info = {
    "name": "3DTextMakerAddOn",
    "description": "This AddOn divides the input text for each character and outputs it as an FBX file",
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

def makesplittext(i, text, fontpath):
    bpy.ops.object.text_add(enter_editmode=False, location=(0, 0, 0))
    txt = bpy.context.object
    txt.name = str(i) + "_" + text
    txt.data.body = text

    if fontpath == "":
        fontpath = "C:/Windows/Fonts/meiryo.ttc"
    fnt = bpy.data.fonts.load(fontpath)
    txt.data.font = fnt

    # extrude
    bpy.context.object.data.extrude = 0.05

    # offset
    bpy.context.object.data.offset = 0

def savetext(i,text, dirname):
    # save fbx
    # dirname = dirdialog()
    filename = os.path.join(dirname, str(i) + "_" + text + ".fbx")
    bpy.ops.export_scene.fbx(filepath=filename, use_selection=True)

### tkinterがblenderと競合(?)して使えないのでファイルダイアログは一旦保留
# def dirdialog():
#     root = tkinter.Tk()
#     root.withdraw()

#     dirname = filedialog.askdirectory(initialdir = dir)

#     return dirname
###


#
# TUTORIAL_OT_3DTextMaker
#
class TUTORIAL_OT_3DTextMaker(bpy.types.Operator):
    bl_idname = "tutorial.3dtextmaker"
    bl_label = "3DTextMaker"
    bl_options = {'REGISTER', 'UNDO'}

    #--- properties ---#
    text: StringProperty(default = "", options = {"HIDDEN"})
    fontpath: StringProperty(default = "", options = {"HIDDEN"})

    #--- execute ---#
    def execute(self, context):
        for i,c in enumerate(self.text):
            makesplittext(i, c, self.fontpath)

        for i,c in enumerate(bpy.context.scene.text):
            bpy.data.objects[str(i) + "_" + c].location.x = i * 1.0

        return {'FINISHED'}

#
# TUTORIAL_OT_SaveText
#
class TUTORIAL_OT_SaveText(bpy.types.Operator):
    bl_idname = "tutorial.savetext"
    bl_label = "savetext"
    bl_options = {'REGISTER', 'UNDO'}

    #--- properties ---#
    dirname: StringProperty(default = "", options ={"HIDDEN"})

    #--- execute ---#
    def execute(self, context):
        for obj in bpy.context.selected_objects:
            obj.select_set(False)

        for i,c in enumerate(bpy.context.scene.text):
            bpy.data.objects[str(i) + "_" + c].select_set(True)
            savetext(i, c, self.dirname)
            bpy.data.objects[str(i) + "_" + c].select_set(False)

        return {'FINISHED'}


#
# TUTORIAL_PT_3DTextMakerPanel
#
class TUTORIAL_PT_3DTextMakerPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "3DTextMaker"
    bl_label = "3DTextMaker"

    #--- draw ---#
    def draw(self, context):
        layout = self.layout

        layout.prop(context.scene, "fontpath")

        layout.prop(context.scene, "text")

        on_prop = layout.operator(TUTORIAL_OT_3DTextMaker.bl_idname, text = "Create")
        on_prop.text = context.scene.text
        on_prop.fontpath = context.scene.fontpath

        layout.prop(context.scene, "dirname")

        on_prop_save = layout.operator(TUTORIAL_OT_SaveText.bl_idname, text = "Save")
        on_prop_save.dirname = context.scene.dirname

#
# register classs
#
classes = [
    TUTORIAL_OT_3DTextMaker,
    TUTORIAL_OT_SaveText,
    TUTORIAL_PT_3DTextMakerPanel
]

def register():
    for c in classes:
        bpy.utils.register_class(c)

    # Panel用変数の登録
    bpy.types.Scene.text = StringProperty(default = "")
    bpy.types.Scene.dirname = StringProperty(default = "")
    bpy.types.Scene.fontpath = StringProperty(default = "")

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

    # Panel用変数の登録解除
    del bpy.types.Scene.text
    del bpy.types.Scene.dirname
    del bpy.types.Scene.fontpath


if __name__ == "__main__":
    register()