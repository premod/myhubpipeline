"""
RigBox Reborn - Main: Curves Tool

Author: Jennifer Conley
Date Modified: 7/03/12

Description:
    This is a main tool comprised of smaller, sub-scripts.
    The Curves Tool script contains commonly used features such as:
        - Control icon creation
	- Colorizing options
	- Preset and custom attribut creation
	- Control clean up options

How to run:
import rr_main_curves
rr_main_curves.window_creation()
"""


import pymel.core as pm


import rr_sub_add_attributes
import rr_sub_color_options
import rr_sub_curve_creation
import rr_sub_double_group
import rr_sub_lock_hide


window_name = 'rr_control_window'
width = 300
bg_color = (0.655297, 0.405063, 1 )


def window_creation():
    global window_object
    
    if (pm.window(window_name, q=True, ex=True)):
	    pm.deleteUI(window_name) 
    if (pm.windowPref(window_name, ex=True)):
	    pm.windowPref(window_name, r=True)
 
    window_object = pm.window(window_name, t='Ctrl Curve Tool')
    gui_creation()
    window_object.show()
	
	
def gui_creation():
    main = pm.columnLayout()
    
    pm.frameLayout(l='Creation', w=width, cll=True, cl=True, bgc=bg_color, cc=pm.Callback(curveWin_resize, -350))
    rr_sub_curve_creation.gui_creation()
    pm.setParent(main)
    
    pm.frameLayout(l='Grouping', w=width, cll=True, cl=True, bgc=bg_color, cc=pm.Callback(curveWin_resize, -150))
    rr_sub_double_group.gui_creation()
    pm.setParent(main)
    
    pm.frameLayout(l='Coloring', w=width, cll=True, cl=True, bgc=bg_color, cc=pm.Callback(curveWin_resize, -150))
    rr_sub_color_options.gui_creation()
    pm.setParent(main)

    pm.frameLayout(l='Attributes', w=width, cll=True, cl=True, bgc=bg_color, cc=pm.Callback(curveWin_resize, -210))
    rr_sub_add_attributes.gui_creation()
    pm.setParent(main)

    pm.frameLayout(l='Lock and Hide', w=width, cll=True, cl=True, bgc=bg_color, cc=pm.Callback(curveWin_resize, -150))
    rr_sub_lock_hide.gui_creation()
    pm.setParent(main)


def curveWin_resize(difference):
    current_height = window_object.getHeight()
    height = current_height + difference
    window_object.setHeight(height)






