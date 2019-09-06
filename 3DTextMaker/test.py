import os
import bpy

# dirnameは出力先のフォルダの絶対パスに書き換えてください
# fontpathはフォントファイルの絶対パスに書き換えてください
# textは自由に記入してください（ファイル名に使用できない記号などは現状使えません）
dirname = "C:/.../output"
fontpath = "C:/Windows/Fonts/meiryo.ttc"
text = "3DTextMaker試作 @ DMiyamo3"
text = text.replace(' ', '')

def test(i, text, isSave = True, isBevel = False, isRemesh = False):
    bpy.ops.object.text_add(view_align=False, enter_editmode=False, location=(0, 0, 0))
    txt = bpy.data.objects['Text']
    txt.data.body = text
    fnt = bpy.data.fonts.load(fontpath)
    txt.data.font = fnt

    # extrude
    bpy.context.object.data.extrude = 0.05

    # offset
    bpy.context.object.data.offset = 0

    # bevel
    if isBevel:
        bpy.context.object.data.bevel_depth = 0.05
        bpy.context.object.data.bevel_resolution = 4

    # remesh
    if isRemesh:
        bpy.ops.object.modifier_add(type='REMESH')
        bpy.context.object.modifiers["Remesh"].mode = 'BLOCKS'
        bpy.context.object.modifiers["Remesh"].octree_depth = 4
        bpy.context.object.modifiers["Remesh"].scale = 0.99
        bpy.context.object.modifiers["Remesh"].use_remove_disconnected = False

    # save fbx
    if isSave:
        filename = os.path.join(dirname,str(i) + "_" + text + ".fbx")
        bpy.ops.export_scene.fbx(filepath=filename, use_selection=True)
        bpy.ops.object.delete()

# main
for i,c in enumerate(text):
    test(i, c)

# test 確認用
# test(text)
