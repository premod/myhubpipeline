"""
RigBox Reborn - Sub: Lock and Hide Tool

Author: Jennifer Conley
Date Modified: 7/03/12

Description:
    A custom GUI to easily lock and hide unused transform channels of a control icon.
    
    Able to use preset options for FK and IK controls.

How to run:
import rr_sub_lock_hide
rr_sub_lock_hide.window_creation()
"""


import pymel.core as pm


window_name = 'lock_and_hide_window'
bg_color = (.451,.451,.451)
width = 300
cbw = 20
checkBoxGrps = []


def window_creation():
    if (pm.window(window_name, q=True, ex=True)):
	pm.deleteUI(window_name)
    if (pm.windowPref(window_name, ex=True)):
	pm.windowPref(window_name, r=True)
	    
    window_object = pm.window(window_name, w=width, t='Lock and Hide')
    gui_creation()
    window_object.show()
    
	
def gui_creation():
    global controlType_radioGrp
    
    main_col = pm.columnLayout(w=width, bgc=(.231,.231,.231), co=('both', 50))
    pm.rowColumnLayout(nc=5, cw=[(1,89),(2,cbw),(3,cbw),(4,cbw+4),(5,cbw+2)])
    pm.text(l='', w=cbw)
    pm.text(l='X', w=cbw)
    pm.text(l='Y', w=cbw)
    pm.text(l='Z', w=cbw)
    pm.text(l='All', w=cbw)
    pm.setParent(main_col)
    
    pm.rowColumnLayout(nc=2, cw=[(1,90),(2,80)])
    pm.text(l='Translation:')
    checkBoxGrps.append(pm.checkBoxGrp(ncb=4, cw4=(cbw, cbw, cbw, cbw), cc4=pm.Callback(rr_allBoxes, [0])))
    pm.text(l='Rotation:')
    checkBoxGrps.append(pm.checkBoxGrp(ncb=4, cw4=(cbw, cbw, cbw, cbw), cc4=pm.Callback(rr_allBoxes, [1])))
    pm.text(l='Scale: ')
    checkBoxGrps.append(pm.checkBoxGrp(ncb=4, cw4=(cbw, cbw, cbw, cbw), cc4=pm.Callback(rr_allBoxes, [2])))
    pm.text(l='Visibility:')
    checkBoxGrps.append(pm.checkBoxGrp(cw=(1,cbw)))
    pm.setParent(main_col)
    
    pm.separator(w=175, h=5)
    
    pm.rowColumnLayout(nc=2, cw=[(1,75),(2,100)])
    pm.button(l='Lock / Hide', bgc=bg_color, c=pm.Callback(rr_lockHide, 0))
    pm.button(l='Show', bgc=bg_color, c=pm.Callback(rr_lockHide, 1))
    pm.setParent(main_col)
    
    pm.separator(w=175, h=5)
    pm.text(l='Selection Type', w=175)
    controlType_radioGrp = pm.radioButtonGrp(la4=['Ik', 'Fk', 'All', 'None'], nrb=4, cw4=(40,40,40,40), sl=4, cc=rr_preset_ctrlType)
    pm.setParent(main_col)
 
    
def rr_preset_ctrlType(*args):
    #Creates a selection based on what control type is specified
    ctrl_type = controlType_radioGrp.getSelect()
    
    if ctrl_type == 1:
	# Select checkboxes for an Ik control.
	checkBoxGrps[0].setValue4(False)
	checkBoxGrps[1].setValue4(True)
	checkBoxGrps[2].setValue4(True)
	checkBoxGrps[3].setValue1(True)
	
	rr_allBoxes([0,1,2])

	
    elif ctrl_type ==2:
	# Select checkboxes for an Fk control.
	checkBoxGrps[0].setValue4(True)
	checkBoxGrps[1].setValue4(False)
	checkBoxGrps[2].setValue4(True)
	checkBoxGrps[3].setValue1(True)
	    
	rr_allBoxes([0,1,2])

    elif ctrl_type ==3:
	# Select all checkboxes.
	checkBoxGrps[0].setValue4(True)
	checkBoxGrps[1].setValue4(True)
	checkBoxGrps[2].setValue4(True)
	checkBoxGrps[3].setValue1(True)

	rr_allBoxes([0,1,2])

    elif ctrl_type == 4:
	# Unselect all checkboxes
	checkBoxGrps[0].setValue4(False)
	checkBoxGrps[1].setValue4(False)
	checkBoxGrps[2].setValue4(False)
	checkBoxGrps[3].setValue1(False)

	rr_allBoxes([0,1,2])


def rr_allBoxes(grpNum):
    # Toggles checkboxes based on the 'All' checkbox option.
    
    for each in grpNum:
	box_state = checkBoxGrps[each].getValue4()

	if box_state == True:
	    checkBoxGrps[each].setValue1(1)
	    checkBoxGrps[each].setValue2(1)
	    checkBoxGrps[each].setValue3(1)
	else:
	    checkBoxGrps[each].setValue1(0)
	    checkBoxGrps[each].setValue2(0)
	    checkBoxGrps[each].setValue3(0)

	
def rr_lockHide(toggle_state):
    # Lock and Hide selected attributes.
    
    # Create a list from the current selection.
    selection = pm.ls(sl=True)

    # Get the state for all of the checkboxes.
    checkbox_state = []

    # State of Visibility checkbox
    checkbox_state.append(checkBoxGrps[3].getValue1())
    
    # State of Translate, Rotate, and Scale checkboxes.
    for each in checkBoxGrps:
	if each != checkBoxGrps[3]:
	    checkbox_state.append(each.getValue1())
	    checkbox_state.append(each.getValue2())
	    checkbox_state.append(each.getValue3())
	    
    # Attribute list which corrisponds to the checkbox states gathered.	
    attribute_list = ['.v', '.tx', '.ty', '.tz', '.rx', '.ry', '.rz', '.sx', '.sy', '.sz']
    
    for object in selection:
	# Preform the operation for every object in the selection.
	
	for index, each in enumerate(checkbox_state):
	    # Perform for each checkbox (transform and axis)
	    
	    if each == True:
		# If the check box is true, find out which button was clicked.
		
		if toggle_state == 0:
		    # If the Lock button was clicked, lock and hide the True checkboxes
		    pm.setAttr(object + attribute_list[index], l=True, k=False)
		
		else:
		    # If the Show button was clicked, show the True checkboxes
		    pm.setAttr(object + attribute_list[index], l=False, k=True)
