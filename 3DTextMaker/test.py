import bpy

# filenameは出力先の絶対パスに書き換える
# fontpathはフォントの絶対パスに書き換える
# textは自由に記入してください ※改行は\n(バックスラッシュ + n)
filename = "C:/.../test.fbx"
fontpath = "C:/Windows/Fonts/meiryo.ttc"
text = "3DTextMaker試作\n@DMiyamo3"

def test(extrude = 0.05, bevel_depth = 0.05, offset = 0, bevel_resolution = 4):
    bpy.ops.object.text_add(view_align=False, enter_editmode=False, location=(0, 0, 0))
    bpy.context.object.data.extrude = extrude
    bpy.context.object.data.bevel_depth = bevel_depth
    bpy.context.object.data.offset = offset
    bpy.context.object.data.bevel_resolution = bevel_resolution

    txt = bpy.data.objects['Text']
    txt.data.body = text
    fnt = bpy.data.fonts.load(fontpath)
    txt.data.font = fnt

    bpy.ops.export_scene.fbx(filepath=filename, use_selection=True)

    bpy.ops.object.delete()
    
test()