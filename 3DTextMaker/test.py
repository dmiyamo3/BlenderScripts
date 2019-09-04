def test():
    bpy.ops.object.mode_set(mode="OBJECT")
    bpy.ops.object.text_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.context.object.data.extrude = 0.01
    bpy.context.object.data.bevel_depth = 0.05
    bpy.context.object.data.offset = 0
    bpy.context.object.data.bevel_resolution = 4
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.text_insert(text="t")
    bpy.ops.font.text_insert(text="e")
    bpy.ops.font.text_insert(text="s")
    bpy.ops.font.text_insert(text="t")
    # メッシュだけ保存 filepathは出力したいフォルダの絶対パスに書き換える
    bpy.ops.export_scene.fbx(filepath="C:/.../test.fbx", check_existing=True, axis_up='Y', axis_forward='-Z', filter_glob="*.fbx", version='BIN7400', use_selection=False, global_scale=1.0, bake_space_transform=False, object_types={'MESH', 'EMPTY', 'OTHER', 'ARMATURE'}, use_mesh_modifiers=True, mesh_smooth_type='OFF', use_mesh_edges=False, use_tspace=False, use_custom_props=False, add_leaf_bones=True, primary_bone_axis='Y', secondary_bone_axis='X', use_armature_deform_only=False, bake_anim=True, bake_anim_use_all_bones=True, bake_anim_use_nla_strips=True, bake_anim_use_all_actions=True, bake_anim_step=1.0, bake_anim_simplify_factor=1.0, use_anim=True, use_anim_action_all=True, use_default_take=True, use_anim_optimize=True, anim_optimize_precision=6.0, path_mode='AUTO', embed_textures=False, batch_mode='OFF', use_batch_own_dir=True, use_metadata=True)
