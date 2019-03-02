""""
Rigbox Reborn - Sub: Double Group Script

Author: Jennifer Conley
Date Modified: 7/03/12

Description:
    A script to quickly orient control icons to the orientation of a selected joint.
    
    Able to function for one joint, or a hierarchy of joints.
    
    The curve must be selected first, then the joint. This selection order was
    choosen because it replicates actual parenting inside of Maya.
    
How to run:
import rr_sub_double_group
rr_sub_double_group.window_creation()
"""


import pymel.core as pm


window_name = 'rr_double_group_win'
width=300


def window_creation():
    if (pm.window(window_name, q=True, ex=True)):
	    pm.deleteUI(window_name)
    if (pm.windowPref(window_name, ex=True)):
	    pm.windowPref(window_name, r=True)
	    
    window_object = pm.window(window_name, w=width, t='Double Group Creation')
    gui_creation()
    window_object.show()
     
                   
def gui_creation():
    global grouping_method_optionMenu
    global hierarchy_creation_optionMenu
    global constraint_method_optionMenu
    
    main = pm.columnLayout(w=width, bgc=(.231,.231,.231))
    main_form = pm.formLayout(nd=100, w=width)
    
    create_grouping_title = pm.columnLayout()
    pm.separator(w=width-15, h=5)
    pm.text(l='Select a curve, then a joint.', w=width-15)
    pm.text(l="Click 'Apply' once tool options have been set.", w=width-15)
    pm.separator(w=width-15, h=5)
    pm.setParent(main_form)

    grouping_method_optionMenu  = pm.optionMenu(bgc=(.451,.451,.451))
    pm.menuItem(l='Single')
    pm.menuItem(l='Chain')
    
    hierarchy_creation_optionMenu = pm.optionMenu(bgc=(.451,.451,.451))
    pm.menuItem(l='Hierarchy')
    pm.menuItem(l='Default')
    
    constraint_method_optionMenu = pm.optionMenu(bgc=(.451,.451,.451))
    pm.menuItem(l='Constrain')
    pm.menuItem(l='None')
    
    apply_button_column = pm.columnLayout()
    pm.separator(w=width-15)
    pm.button(l='Apply', w=width-15, bgc=(.451,.451,.451), c=create_grouping)
    pm.separator(w=width-15)
    
    pm.formLayout(main_form, e=True,
	attachForm=[(apply_button_column, 'bottom', 5), (apply_button_column, 'left', 5), (apply_button_column, 'right', 5), (constraint_method_optionMenu, 'right', 5), (grouping_method_optionMenu, 'left', 5), (create_grouping_title, 'right', 5), (create_grouping_title, 'left', 5), (create_grouping_title, 'top', 5)],
	attachControl=[(apply_button_column, 'top', 5, constraint_method_optionMenu), (hierarchy_creation_optionMenu, 'top', 2, create_grouping_title), (constraint_method_optionMenu, 'top', 2,create_grouping_title), (grouping_method_optionMenu, 'top', 2,create_grouping_title)],
	attachPosition=[(hierarchy_creation_optionMenu, 'left', 2, 32), (constraint_method_optionMenu, 'left', 2, 70)])
 
    
def create_grouping(*args):
    global base_curve_list, root_group_list
	
    selection = pm.ls(sl=True)
    base_curve_list = []
    root_group_list = []

    if (grouping_method_optionMenu.getSelect()) == 1:
	create_single_group(selection)
	
    else:
	create_multiple_group(selection)    


def create_single_group(selection):
    pad_groups_list = []

    
    pad_groups_list = create_pads(pad_groups_list, selection)
    pm.select(selection[0])
    freeze_transforms()
    rename_pad_groups(selection[0], pad_groups_list)
    create_orient_constraint(selection[0], selection[1])


def create_multiple_group(selection):
    pm.select(selection[1], hi=True)
    joint_chain = pm.ls(sl=True)
    joint_chain.pop(-1)
    


    for each in joint_chain:
	if each == joint_chain[0]:
	    curve = selection[0]
	    base_curve_list.append(curve)
	    pad_groups_list = []
	    
	    pm.select(curve, r=True)
	    pm.select(each, tgl=True)
	    objects = pm.ls(sl=True)
	    pad_groups_list = create_pads(pad_groups_list, objects)
	    
	    pm.select(curve)
            freeze_transforms()
            rename_pad_groups(curve, pad_groups_list)
	    create_orient_constraint(curve, each)
	    
	else:
	    curve = curve[0]
            base_curve_list.append(curve)
            pad_groups_list = []
            
            pm.select(curve, r=True)
	    pm.select(each, tgl=True)
	    objects = pm.ls(sl=True)
             
            pad_groups_list = create_pads(pad_groups_list, objects)
            pm.select(curve)
            zero_out_transforms()
            rename_pad_groups(curve, pad_groups_list)
	    create_orient_constraint(curve, each)
	    
	pm.duplicate(curve)
        curve = pm.ls(sl=True)
	
    pm.delete(curve)
    create_group_hierarchy(root_group_list, base_curve_list)

    
def create_pads(pad_groups_list, objects):
    control_rotation_pivot = pm.xform(objects[1], q=True, ws=True, rp=True)
    pm.parent()
    pad_groups_list.append(pm.group())
    pm.xform(ws=True, rp=control_rotation_pivot)
    pad_groups_list.append(pm.group())
    pm.xform(ws=True, rp=control_rotation_pivot)
    pm.parent(w=True)
    print 'pads created'
    return pad_groups_list


def rename_pad_groups(curve, pad_groups_list):
    
    for index, each in enumerate(pad_groups_list):
        each = pm.rename(each, curve + '_GRP_0' + str(index+1))
        new_name = each.replace('CTRL', 'ctrl')
        pm.rename(each, new_name)
    root_group_list.append(pad_groups_list[1])
    print 'groups renamed'


def freeze_transforms():
    pm.makeIdentity(apply=True, t=True, r=True, s=True, n=False)
    print 'transforms frozen'
  
    
def zero_out_transforms():
    pm.xform(t=(0,0,0), ro=(0,0,0))

    
def create_orient_constraint(curve, joint):
    if (constraint_method_optionMenu.getSelect())==1:
	pm.orientConstraint(curve, joint)
    print 'constraint created'
    
    
def create_group_hierarchy(root_group_list, base_curve_list):
    if (hierarchy_creation_optionMenu.getSelect()) == 1:
	base_curve_list.pop(-1)
	base_curve_list.reverse()
	root_group_list.pop(0)
	root_group_list.reverse()
	
	for index, each in enumerate(root_group_list):
	    pm.select(root_group_list[index], r=True)
	    pm.select(base_curve_list[index], tgl=True)
	    pm.parent()
	    pm.select(cl=True)
    
    
    