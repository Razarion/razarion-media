import bpy
 
selObj = []
 
for obj in bpy.context.selected_objects:
 selObj.append(obj.name)
 
bpy.ops.object.select_all(action='TOGGLE')
 
i=0
while i < len(selObj):
 bpy.context.scene.objects.active = bpy.context.scene.objects[selObj[i]]
 bpy.ops.object.mode_set(mode="EDIT")
 bpy.ops.mesh.select_all(action='TOGGLE')
 bpy.ops.mesh.select_all(action='TOGGLE')
 # bpy.ops.uv.smart_project(angle_limit=66.0, island_margin=0.0, user_area_weight=0.0)
 f="C:\\dev\\projects\\razarion\\razarion-media\\gimp\\exportedUv\\uv_" + bpy.data.objects[selObj[i]].name
 bpy.ops.uv.export_layout(filepath=f, mode='PNG', size=(512, 512), opacity=0)
 bpy.ops.object.mode_set(mode="OBJECT")
 bpy.ops.object.select_all(action='TOGGLE')
 i+=1
