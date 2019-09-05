import os
import bpy

# dirnameは出力先のフォルダの絶対パスに書き換えてください
# fontpathはフォントファイルの絶対パスに書き換えてください
# textは自由に記入してください（ファイル名に使用できない記号などは現状使えません）
dirname = "C:/.../output"
fontpath = "C:/Windows/Fonts/meiryo.ttc"
text = "3DTextMaker試作@DMiyamo3"

def test(i, text, extrude = 0.05, bevel_depth = 0.05, offset = 0, bevel_resolution = 4):
    bpy.ops.object.text_add(view_align=False, enter_editmode=False, location=(0, 0, 0))
    bpy.context.object.data.extrude = extrude
    bpy.context.object.data.bevel_depth = bevel_depth
    bpy.context.object.data.offset = offset
    bpy.context.object.data.bevel_resolution = bevel_resolution

    txt = bpy.data.objects['Text']
    txt.data.body = text
    fnt = bpy.data.fonts.load(fontpath)
    txt.data.font = fnt

    filename = os.path.join(dirname,str(i) + "_" + text + ".fbx")
    bpy.ops.export_scene.fbx(filepath=filename, use_selection=True)

    bpy.ops.object.delete()
    
for i,c in enumerate(text):
    test(i, c)
