



bl_info = {
    "name": "ZBEAR's Drag N' Drop Importer",
    "description": "Drag N' Drop, Import 3D Files to ViewPort",
    "author": "ZBEAR, www.zbear.co.kr, zorzybear@gmail.com",
    "version": (2, 93),
    "blender": (2, 93, 0),
    "location": "Blender Top Header / Python Console",
    "doc_url": "---",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "Import-Export",
    }



import bpy


#before drop button operator class - button1
class OBJECT_OT_zbear_hard_rock_guitar_solo_albums(bpy.types.Operator):
    bl_idname = "object.zbear_hard_rock_guitar_solo_albums"
    bl_label = "ZBEAR's Drag N' Drop"

    #bl_space_type = "CONSOLE"
    #bl_region_type = "HEADER"
    
    @classmethod
    def hard_rock_function(self):
        
        bpy.ops.console.execute()
        bpy.ops.console.execute()        
        area = bpy.context.window_manager.windows[-1].screen.areas[0]
        for space in area.spaces:
            if space.type == 'CONSOLE':
                space.font_size = 22        
        #Good.. Really so Hard Rocking Printing Out
        bpy.ops.console.insert(text=
        "print(\"\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n obj fbx hdr bvh dae stl kpl svg gltf x3d\\n\\n\\n\\n\\n\\n :: ZBEAR's Hard Rock Guitar Solo Album Released!! \\n Let's go to listen to the ZBEAR's Hard Rock Music Albums Before We do something with Blender. \\n Let's go!! with Blender we hand in hand~~ \\n ZBEAR on YouTube, on iTunes, on Spotify, on Melon, Google, Naver, --- \\n Your Naived Head need to be Banged!! Hurry Up!! \\n Then...... Okay,- well~, \\n\\n Now you~.. \\n\\n So..\\n \")")
        bpy.ops.console.execute()

        bpy.ops.console.insert(text='Drop_your_Hard_Rocked_3D_File_to_This_Window=r')
        
                
        return {"FINISHED"}
    
    def execute(self, context):
                
        self.hard_rock_function()
        
        return {"FINISHED"}



class OBJECT_OT_zbear_unfinished_fight1(bpy.types.Operator):
    bl_idname = "object.zbear_unfinished_fight1"
    bl_label = "Import N' Drop"

    #bl_space_type = "CONSOLE"
    #bl_region_type = "HEADER"
    
    def execute(self, context):
        
        bpy.ops.console.execute()

        bpy.ops.console.insert(text="Drop_your_Hard_Rocked_3D_File_to_This_Window = repr(Drop_your_Hard_Rocked_3D_File_to_This_Window)")
        bpy.ops.console.execute()
        bpy.ops.console.insert(text=r'Drop_your_Hard_Rocked_3D_File_to_This_Window = Drop_your_Hard_Rocked_3D_File_to_This_Window.replace("\\\\", "\\")')
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        bpy.ops.console.insert(text=r'Drop_your_Hard_Rocked_3D_File_to_This_Window = Drop_your_Hard_Rocked_3D_File_to_This_Window.replace("\'","")')
        
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="import os")
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="filename, extension = os.path.splitext(Drop_your_Hard_Rocked_3D_File_to_This_Window)")
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="dirname = os.path.dirname(Drop_your_Hard_Rocked_3D_File_to_This_Window)")
        bpy.ops.console.execute()
        
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="if extension == '.obj' :")
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="    obj_mtl_dualpath = Drop_your_Hard_Rocked_3D_File_to_This_Window + ';' + dirname + filename + '.mtl'")
        bpy.ops.console.execute()
        
        
        
        bpy.ops.console.insert(text="    bpy.ops.import_scene.obj(filepath=Drop_your_Hard_Rocked_3D_File_to_This_Window, filter_glob=obj_mtl_dualpath)")
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        
        
        
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="if extension == '.fbx' :")
        bpy.ops.console.execute()

        bpy.ops.console.insert(text="    bpy.ops.import_scene.fbx(filepath=Drop_your_Hard_Rocked_3D_File_to_This_Window, directory=dirname, filter_glob='*.fbx')")       
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        
        
        bpy.ops.console.execute()       
        bpy.ops.console.insert(text="if extension == '.bvh' :")
        bpy.ops.console.execute()
        

        bpy.ops.console.insert(text="    bpy.ops.import_anim.bvh(filepath=Drop_your_Hard_Rocked_3D_File_to_This_Window)")    
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        
        
        bpy.ops.console.execute()       
        bpy.ops.console.insert(text="if (extension == '.ase') or (extension == '.ASE') :")
        bpy.ops.console.execute()
        

    
        bpy.ops.console.insert(text="    bpy.ops.import_ase.read(filepath=Drop_your_Hard_Rocked_3D_File_to_This_Window)")
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        
        
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="if (extension == '.jpg') or (extension == '.JPG') or (extension == '.png') or (extension == '.PNG') or (extension == '.jpeg') or (extension == '.JPEG') or (extension == '.tga') or (extension == '.TGA') or (extension == '.bmp') or (extension == '.BMP') :")
        bpy.ops.console.execute()
        

        
        bpy.ops.console.insert(text="    bpy.ops.import_image.to_plane(filepath=Drop_your_Hard_Rocked_3D_File_to_This_Window)")
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        
        
        
        bpy.ops.console.execute()        
        bpy.ops.console.insert(text="if (extension == '.stl') or (extension == '.STL'):")
        bpy.ops.console.execute()
        

        
        bpy.ops.console.insert(text="    bpy.ops.import_mesh.stl(filepath=Drop_your_Hard_Rocked_3D_File_to_This_Window , directory=dirname)")
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        
        
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="if (extension == '.kpl') or (extension == '.gpl'):")
        bpy.ops.console.execute()
        
        bpy.ops.console.insert(text="    bpy.ops.import_krita.read(filepath=Drop_your_Hard_Rocked_3D_File_to_This_Window)")
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        
        
        
        bpy.ops.console.execute()        
        bpy.ops.console.insert(text="if (extension == '.gltf') or (extension == '.GLTF'):")
        bpy.ops.console.execute()
        
        bpy.ops.console.insert(text="    bpy.ops.import_scene.gltf(filepath=Drop_your_Hard_Rocked_3D_File_to_This_Window)")
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        
        
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="if (extension == '.x3d') or (extension == '.X3D'):")
        bpy.ops.console.execute()
        
        bpy.ops.console.insert(text="    bpy.ops.import_scene.x3d(filepath=Drop_your_Hard_Rocked_3D_File_to_This_Window)")
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        
        
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="if (extension == '.svg') or (extension == '.SVG'):")
        bpy.ops.console.execute()
        

        
        bpy.ops.console.insert(text="    bpy.ops.import_curve.svg(filepath=Drop_your_Hard_Rocked_3D_File_to_This_Window)")
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        bpy.ops.console.execute()
   
   
        
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="if (extension == '.hdr') or (extension == '.HDR'):")
        bpy.ops.console.execute()
        
        bpy.ops.console.insert(text="    scn = bpy.context.scene")
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="    node_tree = scn.world.node_tree")
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="    tree_nodes = node_tree.nodes")
        bpy.ops.console.execute()        
        bpy.ops.console.insert(text="    tree_nodes.clear()")
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="    node_background = tree_nodes.new(type='ShaderNodeBackground')")
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="    node_environment = tree_nodes.new('ShaderNodeTexEnvironment')")
        bpy.ops.console.execute()
        
        bpy.ops.console.insert(text="    node_environment.image = bpy.data.images.load(filepath=Drop_your_Hard_Rocked_3D_File_to_This_Window)")
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="    node_environment.location = -300,0")
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="    node_output = tree_nodes.new(type='ShaderNodeOutputWorld')")
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="    node_output.location = 200,0")
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="    links = node_tree.links")
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="    link = links.new(node_environment.outputs['Color'], node_background.inputs['Color'])")
        bpy.ops.console.execute()
        bpy.ops.console.insert(text="    link = links.new(node_background.outputs['Background'], node_output.inputs['Surface'])")
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        
        
        bpy.ops.console.execute()       
        bpy.ops.console.insert(text="if (extension == '.dae') or (extension == '.DAE'):")
        bpy.ops.console.execute()
        
        bpy.ops.console.insert(text="    bpy.ops.wm.collada_import(filepath =Drop_your_Hard_Rocked_3D_File_to_This_Window)")
        bpy.ops.console.execute()
        bpy.ops.console.execute()
        bpy.ops.console.execute()        
        
        #
        #bpy.ops.console.execute()
        
        bpy.ops.console.insert(text="print(\"\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n === ZBEAR's Hard Rock 3D File Importer ===\\n If you fail to import, check:\\n 1. Isn't the version of your file too high for Blander to import?\\n 2. Isn't custom setting excessively included?\\n If Case 1, adjust the version to less than the version allowed by Blander and bring it back.\\n If Case 2, you don't use this add-on, but use the original import function of the blender, which includes formal detailed options.\\n === ZBEAR's Hard Rock 3D File Importer ===\")")
        
        
        
        #Good.. Really so Hard Rocking Printing Out

        bpy.ops.console.execute()
        
        bpy.ops.console.insert(text='Drop_your_Hard_Rocked_3D_File_to_This_Window=r')
        
                      
 
 #bpy.ops.console.insert(text="print(\" === ZBEAR's Hard Rock 3D File Importer ===\\n If you fail to import, check:\\n 1. Isn't the version of your file too high for Blander to import?\\n 2. Isn't custom setting excessively included?\\n If Case 1, adjust the version to less than the version allowed by Blander and bring it back.\\n\")")
        #bpy.ops.console.execute()
        #area = bpy.context.window_manager.windows[-1].screen.areas[0]
        #area.header_text_set(None)
        
        #bpy.types.CONSOLE_HT_header.remove(draw)
        
        return {"FINISHED"}


#top bar operator class
class OBJECT_OT_zbear_unfinished_fight2(bpy.types.Operator):
    bl_idname = "object.zbear_unfinished_fight2"
    bl_label = "ZBEAR's Drag N' Drop Importer"

    #bl_space_type = "CONSOLE"
    #bl_region_type = "HEADER"
    
    @classmethod
    def hard_rock_function(self, context):
        
        #bpy.ops.console.insert(text="classme??")
        #bpy.types.OBJECT_OT_zbear_hard_rock_guitar_solo_albums.hard_rock_function()\

      #  for area in bpy.context.window_manager.windows[-1].screen.areas:
       #     print(area)
            
    #    print("-------------")
        #area = bpy.context.window_manager.windows[-1].screen.areas[0]
      #  for area in bpy.context.window_manager.windows[-1].screen.areas:
       #     print(area)
            
        #for space in area.spaces:
            #if space.type == 'CONSOLE':
#                space.font_size = 22
                #print(space.type)
                #print(space.id_data)
                #print(space.font_size)
                #space.font_size =22

        return {"FINISHED"}
    
    def execute(self, context):
        
        
        render = bpy.context.scene.render
        originalX = render.resolution_x
        originalY = render.resolution_y
        originalP = render.resolution_percentage


        render.resolution_x = 640
        render.resolution_y = 480
        render.resolution_percentage = 100

        # Modify preferences (to guaranty new window)
        prefs = bpy.context.preferences
        prefs.view.render_display_type = "WINDOW"

        # Call image editor window
        bpy.ops.render.view_show("INVOKE_DEFAULT")
        

        # Change area type
        area = bpy.context.window_manager.windows[-1].screen.areas[0]
        area.type = "CONSOLE"        

        #bpy.ops.console.insert(text="if (extension == '.dae') or (extension == '.DAE'):")
        #bpy.types.CONSOLE_HT_header.append(draw)
        
        
        #for region in area.regions:
        #    if region.type == 'WINDOW' : 
        #        ctx = bpy.context.copy()           
        #        ctx['area'] = area
        #        ctx['region'] = region
        #        bpy.ops.console.insert(text="yeahho")       
        

        render.resolution_x = originalX 
        render.resolution_y = originalY
        render.resolution_percentage = originalP
        
        
        self.hard_rock_function(context)

        #row.operator("reweight.reweightprocess") 
        
        #bpy.ops.zbear.hard_rock_guitar_solo_albums()  #err
        #self.operator(ZBEAR_OT_hard_rock_guitar_solo_albums.bl_idname)
        #bpy.ops.zbear.hard_rock_guitar
        
        
        
        return {"FINISHED"}




def draw(self, context):
    self.layout.operator(OBJECT_OT_zbear_hard_rock_guitar_solo_albums.bl_idname)
    self.layout.operator(OBJECT_OT_zbear_unfinished_fight1.bl_idname)

    
def draw2(self, context):
    self.layout.operator(OBJECT_OT_zbear_unfinished_fight2.bl_idname)


classes = (OBJECT_OT_zbear_hard_rock_guitar_solo_albums, OBJECT_OT_zbear_unfinished_fight1, OBJECT_OT_zbear_unfinished_fight2,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.CONSOLE_HT_header.append(draw)
    bpy.types.TOPBAR_HT_upper_bar.append(draw2)


def unregister():
    
    bpy.types.TOPBAR_HT_upper_bar.remove(draw2)
    bpy.types.CONSOLE_HT_header.remove(draw)
    
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
    






