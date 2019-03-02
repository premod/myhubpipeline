"""
RigBox Reborn - Sub: Add Attributes Tool

Author: Jennifer Conley
Date Modified: 7/03/12

Description:
    A custom GUI to easily add common attributes to objects.
    
    Allows for additonal, custom attributes, to be added to objects
    without having to navigate to other windows.
    
How to run:
import rr_sub_add_attributes
rr_sub_add_attributes.window_creation()
"""


import pymel.core as pm


windowName = 'rr_addAttrs_tool'
width = 300
title_color = (0.860652, 0.759494, 1)
bg_color = (.451,.451,.451)


def window_creation():
    if (pm.window(windowName, q=True, ex=True)):
	    pm.deleteUI(windowName)   
    if (pm.windowPref(windowName, ex=True)):
	    pm.windowPref(windowName, r=True)

    window_object = pm.window(windowName, t='Add Attribute Tool', w=width)
    gui_creation()
    window_object.show()
               
	       
def gui_creation():
    main = pm.columnLayout(w=width, bgc=(.231,.231,.231))
    main_form = pm.formLayout(nd=100, w=width)
    
    preset_options_column = pm.columnLayout(w=width)
    title_creation('Preset Options')
    preset_options()
    pm.setParent(main_form)
    
    custom_options_column = pm.columnLayout(w=width)
    title_creation('Custom Options')
    custom_options()
    pm.setParent(main_form)
    
    pm.formLayout(main_form, e=True,
	attachForm=[(custom_options_column, 'left', 5), (custom_options_column, 'right', 5), (custom_options_column, 'bottom', 5), (preset_options_column, 'left', 5), (preset_options_column, 'right', 5), (preset_options_column, 'top', 5)],
	attachControl=[(custom_options_column, 'top', 2, preset_options_column)])

    
def title_creation(title):
    pm.columnLayout(w=width)
    pm.separator(w=width-15, h=5)
    pm.text(l=title, w=width-15, bgc=title_color)
    pm.separator(w=width-15, h=5)
    
    
def preset_options():
    main = pm.columnLayout(w=width)
    
    pm.rowColumnLayout(nc=2, w=width)
    pm.button(w=141, bgc=bg_color, l='Ik Foot', c=ik_foot_attrs)
    pm.button(w=141, bgc=bg_color, l='Foot Switch', c=foot_switch_attrs)
    pm.button(w=141, bgc=bg_color, l='Ik Hand', c=ik_hand_attrs)
    pm.button(w=141, bgc=bg_color, l='Hand Switch', c=hand_switch_attrs)
    pm.setParent(main)
    
    pm.rowColumnLayout(nc=3, w=width)
    pm.button(w=94, bgc=bg_color, l='Cog', c=cog_attrs)
    pm.button(w=94, bgc=bg_color, l='Head', c=head_attrs)
    pm.button(w=94, bgc=bg_color, l='Eye', c=eye_attrs)
    pm.setParent(main)
    
    
def custom_options():
    global attributeType_radioGrp, attribute_nameField, attribute_minField, attribute_maxField
    main = pm.columnLayout()
    attributeType_radioGrp = pm.radioButtonGrp(cc=field_display, sl=1, nrb=4, cw4=(75,75,75,75), la4=('Float', 'Integer', 'Boolean', 'Sep'))
    
    pm.separator(w=width-15, h=10)
    pm.rowColumnLayout(nc=4, w=width)
    attribute_nameField = pm.textField(w=71, ann = 'Attribute Name', tx='Name')
    attribute_minField = pm.floatField(w=71, ann='Attribute Min', v=-360, pre=1)
    attribute_maxField = pm.floatField(w=71, ann='Attribute Max', v=360, pre=1)
    pm.button(l='Create', bgc=bg_color, w=71, c=create_attr)
    pm.setParent(main)
    

def cog_attrs(*args):
    selection = pm.ls(sl=True)
	
    for individual_object in selection:
	pm.addAttr(individual_object, ln='Adv_Back', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Adv_Back', cb=True)

	pm.addAttr(individual_object, ln='Back_Ctrls', at='enum', en='Fk_Ctrls:Ik_Ctrls:Both:None', k=True)

	pm.addAttr(individual_object, ln='Other', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Other', cb=True)
	
	pm.addAttr(individual_object, ln='Res', at='enum', en='Low:Proxy:High', k=True)
	pm.addAttr(individual_object, ln='Auto_Hips', at='bool', k=True)


def eye_attrs(*args):
    selection = pm.ls(sl=True)

    for individual_object in selection:
	pm.addAttr(individual_object, ln='CtrlVis', at='enum', en='----------------')
	pm.setAttr(individual_object + '.CtrlVis', cb=True)

	pm.addAttr(individual_object, ln='IndivCtrls', at='bool', k=True)


def head_attrs(*args):
    selection = pm.ls(sl=True)
    
    for individual_object in selection:
	pm.addAttr(individual_object, ln='Ctrl_Visibility', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Ctrl_Visibility', cb=True)

	pm.addAttr(individual_object, ln='Face_Gui', at='bool', k=True)
	pm.addAttr(individual_object, ln='Eye_Ctrls', at='bool', k=True)


def ik_foot_attrs(*args):
    selection = pm.ls(sl=True)

    for individual_object in selection:
	pm.addAttr(individual_object, ln='Foot_SDKs', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Foot_SDKs', cb=True)

	pm.addAttr(individual_object, ln='Foot_Roll', at='double', min=-10, max=10, dv=0, k=True)
	pm.addAttr(individual_object, ln='Bank', at='double', min=-360, max=360, dv=0, k=True)	

	pm.addAttr(individual_object, ln='Raises', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Raises', cb=True)

	pm.addAttr(individual_object, ln='Toe_Raise', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Ball_Raise', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Heel_Raise', at='double', min=-360, max=360, dv=0, k=True)

	pm.addAttr(individual_object, ln='Grinds', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Grinds', cb=True)

	pm.addAttr(individual_object, ln='Toe_Grind', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Ball_Grind', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Heel_Grind', at='double', min=-360, max=360, dv=0, k=True)

	pm.addAttr(individual_object, ln='Knee_PV', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Knee_PV', cb=True)

	pm.addAttr(individual_object, ln='Knee', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Offset', at='double', min=-360, max=360, dv=0, k=True)

	pm.addAttr(individual_object, ln='Space_Switching', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Space_Switching', cb=True)

	pm.addAttr(individual_object, ln='Cog', at='double', min=0, max=10, dv=0, k=True)
	pm.addAttr(individual_object, ln='Locator', at='double', min=0, max=10, dv=0, k=True)


def ik_hand_attrs(*args):
    selection = pm.ls(sl=True)
    attributes = ['Head', 'Back', 'Hips', 'Locator']

    for individual_object in selection:
	pm.addAttr(individual_object, ln='Space_Switching', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Space_Switching', cb=True)
	for individual_attribute in attributes:
	    pm.addAttr(individual_object, ln=individual_attribute, at='double', min=0, max=10, dv=0, k=True)


def foot_switch_attrs(*args):
    selection = pm.ls(sl=True)

    for individual_object in selection:
	pm.addAttr(individual_object, ln='Ik_Fk_Switch', at='double', min=0, max=10, dv=0, k=True)

	pm.addAttr(individual_object, ln='Indiv_Ctrls', at='bool', k=True)
	
	pm.addAttr(individual_object, ln='ToeSDKs', at='enum', en='----------------')
	pm.setAttr(individual_object + '.ToeSDKs', cb=True)

	pm.addAttr(individual_object, ln='All_Curl', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='All_Spread', at='double', min=-360, max=360, dv=0, k=True)

	pm.addAttr(individual_object, ln='Big_Curl', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Big_Curl', cb=True)

	pm.addAttr(individual_object, ln='Big_Root', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Big_Mid', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Big_End', at='double', min=-360, max=360, dv=0, k=True)

	pm.addAttr(individual_object, ln='Index_Curl', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Index_Curl', cb=True)

	pm.addAttr(individual_object, ln='Index_Root', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Index_Mid', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Index_End', at='double', min=-360, max=360, dv=0, k=True)

	pm.addAttr(individual_object, ln='Mid_Curl', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Mid_Curl', cb=True)

	pm.addAttr(individual_object, ln='Mid_Root', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Mid_Mid', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Mid_End', at='double', min=-360, max=360, dv=0, k=True)

	pm.addAttr(individual_object, ln='Fourth_Curl', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Fourth_Curl', cb=True)

	pm.addAttr(individual_object, ln='Fourth_Root', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Fourth_Mid', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Fourth_End', at='double', min=-360, max=360, dv=0, k=True)

	pm.addAttr(individual_object, ln='Pinky_Curl', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Pinky_Curl', cb=True)

	pm.addAttr(individual_object, ln='Pinky_Root', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Pinky_Mid', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Pinky_End', at='double', min=-360, max=360, dv=0, k=True)

	pm.addAttr(individual_object, ln='Spreads', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Spreads', cb=True)

	pm.addAttr(individual_object, ln='Big_Spread', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Index_Spread', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Mid_Spread', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Fourth_Spread', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Pinky_Spread', at='double', min=-360, max=360, dv=0, k=True)	


def hand_switch_attrs(*args):
    selection = pm.ls(sl=True)
    
    for individual_object in selection:
	pm.addAttr(individual_object, ln='Ik_Fk_Switch', at='double', min=0, max=10, dv=0, k=True)
	
	pm.addAttr(individual_object, ln='Indiv_Ctrls', at='bool', k=True)
	
	pm.addAttr(individual_object, ln='Finger_SDKs', at='enum', en='----------:Blue')
	pm.setAttr(individual_object + '.Finger_SDKs', cb=True)
	
	pm.addAttr(individual_object, ln='All_Curl', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='All_Spread', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='All_Flat', at='double', min=-360, max=360, dv=0, k=True)
	
	pm.addAttr(individual_object, ln='Thumb_Curl', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Thumb_Curl', cb=True)
	
	pm.addAttr(individual_object, ln='Thumb_Drop', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Thumb_Root', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Thumb_Mid', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Thumb_End', at='double', min=-360, max=360, dv=0, k=True)

	pm.addAttr(individual_object, ln='Index_Curl', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Index_Curl', cb=True)
	
	pm.addAttr(individual_object, ln='Index_Root', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Index_Mid', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Index_End', at='double', min=-360, max=360, dv=0, k=True)

	pm.addAttr(individual_object, ln='Mid_Curl', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Mid_Curl', cb=True)
	
	pm.addAttr(individual_object, ln='Mid_Root', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Mid_Mid', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Mid_End', at='double', min=-360, max=360, dv=0, k=True)

	pm.addAttr(individual_object, ln='Ring_Curl', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Ring_Curl', cb=True)
	
	pm.addAttr(individual_object, ln='Ring_Root', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Ring_Mid', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Ring_End', at='double', min=-360, max=360, dv=0, k=True)
	
	pm.addAttr(individual_object, ln='Pinky_Curl', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Pinky_Curl', cb=True)
	
	pm.addAttr(individual_object, ln='Pinky_Root', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Pinky_Mid', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Pinky_End', at='double', min=-360, max=360, dv=0, k=True)
	
	pm.addAttr(individual_object, ln='Spreads', at='enum', en='----------------')
	pm.setAttr(individual_object + '.Spreads', cb=True)
	
	pm.addAttr(individual_object, ln='Thumb_Spread', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Index_Spread', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Mid_Spread', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Ring_Spread', at='double', min=-360, max=360, dv=0, k=True)
	pm.addAttr(individual_object, ln='Pinky_Spread', at='double', min=-360, max=360, dv=0, k=True)


def create_attr(*args):
    attr_value = attributeType_radioGrp.getSelect()
    name = attribute_nameField.getText()
    min_value = attribute_minField.getValue()
    max_value = attribute_maxField.getValue()

    selection = pm.ls(sl=True)

    for individual_object in selection:
	if attr_value == 1:
	    pm.addAttr(individual_object, ln=name, at='double', min=min_value, max=max_value, k=True)
	    
	elif attr_value == 2:
	    pm.addAttr(individual_object, ln=name, at='long', min=min_value, max=max_value, k=True)

	elif attr_value == 3:
	    pm.addAttr(individual_object, ln=name, at='bool', k=True)
	    
	else:
	    pm.addAttr(individual_object, ln=name, at='enum', en='----------------')
	    pm.setAttr(individual_object + '.' + name, cb=True)
	
    print "Custom attribute '" + name + "' has been added to selected objects."
 
        
def field_display(*args):
    attr_value = attributeType_radioGrp.getSelect()
    
    if attr_value == 1:
	attribute_minField.setEnable(True)
	attribute_maxField.setEnable(True)
	
    elif attr_value == 2:
	attribute_minField.setEnable(True)
	attribute_maxField.setEnable(True)
	
    elif attr_value == 3:
	attribute_minField.setEnable(False)
	attribute_maxField.setEnable(False)
	
    else:
	attribute_minField.setEnable(False)
	attribute_maxField.setEnable(False)

    print 'Attribut Creation GUI has been updated.'
        


