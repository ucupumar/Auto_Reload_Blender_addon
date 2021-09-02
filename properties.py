import bpy


from .timer_function import update_timer_function


# update function for update_needed property
def update_function_updateneeded(self, context):
    if self.autoreload_update_needed:
        bpy.ops.autoreload.dialog_popups(
                            'INVOKE_DEFAULT',
                            message = self.autoreload_update_message,
                            operator = "bpm.open_url",
                            operator_text = "New addon version available",
                            operator_icon = "URL",
                            operator_url = self.autoreload_update_download_url
                            )


class AUTORELOAD_PR_properties(bpy.types.PropertyGroup) :

    # missings
    autoreload_missing_images : bpy.props.BoolProperty(name='Missing Images')
    autoreload_missing_libraries : bpy.props.BoolProperty(name='Missing Libraries')

    # inspectors
    autoreload_active_image_index : bpy.props.IntProperty(name='Image Index')
    autoreload_active_library_index : bpy.props.IntProperty(name='Library Index')
    
    # timer
    autoreload_is_timer : bpy.props.BoolProperty(
                            name='Image Timer',
                            description="Start Timer to fetch modified Images every n seconds.",
                            update=update_timer_function,
                            )

    # update
    autoreload_update_needed : bpy.props.BoolProperty(
                                name='Update Needed',
                                update=update_function_updateneeded,
                                )
    autoreload_update_message : bpy.props.StringProperty(name='Update Message')
    autoreload_update_download_url : bpy.props.StringProperty(name='Update Download URL')


### REGISTER ---

def register():
    bpy.utils.register_class(AUTORELOAD_PR_properties)

    bpy.types.WindowManager.autoreload_properties = \
        bpy.props.PointerProperty(type = AUTORELOAD_PR_properties, name="Auto Reload Properties")

    bpy.types.Image.autoreload_modification_time = \
        bpy.props.StringProperty(name='File Modification Date', default='')
    bpy.types.Library.autoreload_modification_time = \
        bpy.props.StringProperty(name='File Modification Date', default='')
    bpy.types.Library.autoreload_to_reload = \
        bpy.props.BoolProperty(name='Library to reload')

    # bpy.types.WindowManager.autoreload_missing_images = \
    #     bpy.props.BoolProperty(name='Missing Images')
    # bpy.types.WindowManager.autoreload_missing_libraries = \
    #     bpy.props.BoolProperty(name='Missing Libraries')

    # # image inspector
    # bpy.types.WindowManager.autoreload_active_image_index = \
    #     bpy.props.IntProperty(name='Inspector Index')

    # # timer
    # bpy.types.WindowManager.autoreload_is_timer = \
    #     bpy.props.BoolProperty(
    #         name='Image Timer',
    #         description="Start Timer to fetch modified Images every n seconds.",
    #         update=update_timer_function,
    #         )
    
    # # update
    # bpy.types.WindowManager.autoreload_update_needed = \
    #     bpy.props.BoolProperty(
    #         name='Update Needed',
    #         update=update_function_updateneeded)
    # bpy.types.WindowManager.autoreload_update_message = \
    #     bpy.props.StringProperty(name='Update Message')
    # bpy.types.WindowManager.autoreload_update_download_url = \
    #     bpy.props.StringProperty(name='Update Download URL')

def unregister():
    if bpy.context.window_manager.autoreload_properties.autoreload_is_timer:
        bpy.context.window_manager.autoreload_properties.autoreload_is_timer = False

    del bpy.types.WindowManager.autoreload_properties

    bpy.utils.unregister_class(AUTORELOAD_PR_properties)

    del bpy.types.Image.autoreload_modification_time
    del bpy.types.Library.autoreload_modification_time
    del bpy.types.Library.autoreload_to_reload

    # del bpy.types.WindowManager.autoreload_missing_images
    # del bpy.types.WindowManager.autoreload_missing_libraries

    # # image inspector
    # del bpy.types.WindowManager.autoreload_active_image_index

    # # timer
    # if bpy.context.window_manager.autoreload_is_timer:
    #     bpy.context.window_manager.autoreload_is_timer = False
    # del bpy.types.WindowManager.autoreload_is_timer

    # # update
    # del bpy.types.WindowManager.autoreload_update_needed
    # del bpy.types.WindowManager.autoreload_update_message
    # del bpy.types.WindowManager.autoreload_update_download_url