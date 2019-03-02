"""
RigBox Reborn - Curve Tool

Author: Jennifer Conley
Date Modified: 7/03/12

Description:
    A custom GUI to easily create commonly used control icons for rig construction.
	- Includes 2D, 3D, and text based curves.

How to run:
import rr_sub_curve_creation
rr_sub_curve_creation.window_creation()
"""


import pymel.core as pm


window_name = 'rr_control_creation_window'
width = 300
title_color = (0.860652, 0.759494, 1)
bg_color = (.451,.451,.451)


def window_creation():    
    if (pm.window(window_name, q=True, ex=True)):
	    pm.deleteUI(window_name)
    if (pm.windowPref(window_name, ex=True)):
	    pm.windowPref(window_name, r=True)

    window_object = pm.window(window_name, t='Ctrl Curve Tool')
    gui_creation()
    window_object.show()
    
	
def gui_creation():
    global ctrl_tabLayout
    main_layout= pm.columnLayout(w=width, bgc=(.231,.231,.231))
    
    main_form = pm.formLayout(w=width, nd=100)
    rr_2D_shapes_title = title_creation('2D Shapes', main_form)
    rr_2D_controls_section = rr_2D_controls(main_form)
    
    rr_2D_arrows_title = half_title_creation('2D Arrows', main_form)
    rr_2D_arrows_section = rr_2D_arrows(main_form)
    rr_3D_title = half_title_creation('3D Shapes', main_form)
    rr_3D_section = rr_3D_controls(main_form)
    
    rr_text_title = title_creation('Text Shapes', main_form)
    rr_letter_section = rr_letter_controls(main_form)
    rr_text_section = rr_text_controls(main_form)
    
    
    pm.formLayout(main_form, e=True,
	attachForm=[(rr_letter_section, 'bottom', 5), (rr_text_section, 'bottom', 5), (rr_text_section, 'right', 5), (rr_letter_section, 'left', 5), (rr_text_title, 'left', 5), (rr_text_title, 'right', 5), (rr_3D_section, 'right', 5), (rr_3D_title, 'right', 5), (rr_2D_arrows_section, 'left', 5), (rr_2D_arrows_title, 'left', 5), (rr_2D_controls_section, 'right', 5), (rr_2D_controls_section, 'left', 5), (rr_2D_shapes_title, 'top', 5), (rr_2D_shapes_title, 'right', 5), (rr_2D_shapes_title, 'left', 5)],
	attachControl=[(rr_text_section, 'left', 0, rr_letter_section), (rr_text_section, 'top', 0, rr_text_title), (rr_letter_section, 'top', 0, rr_text_title), (rr_text_title, 'top', 0, rr_3D_section), (rr_3D_section, 'left', 0, rr_2D_arrows_section), (rr_3D_section, 'top', 0, rr_3D_title), (rr_3D_title, 'top', 0, rr_2D_controls_section), (rr_2D_arrows_section, 'top', 0, rr_2D_arrows_title), (rr_2D_arrows_title, 'top', 0, rr_2D_controls_section), (rr_2D_controls_section, 'top', 0, rr_2D_shapes_title)])
    
    
def title_creation(title, parent_layout):
    main = pm.columnLayout(w=width/2)
    
    pm.separator(w=width-15, h=5)
    pm.text(l=title, w=width-15, bgc=title_color)
    pm.separator(w=width-15, h=5)
    pm.setParent(parent_layout)
    
    return main


def half_title_creation(title, parent_layout):
    main = pm.columnLayout(w=width/2)
    
    pm.separator(w=(width-15)/2, h=5)
    pm.text(l=title, w=(width-15)/2, bgc=title_color)
    pm.separator(w=(width-15)/2, h=5)
    pm.setParent(parent_layout)
    
    return main


def rr_2D_controls(parent_layout):
    main = pm.columnLayout(w=width)

    pm.rowColumnLayout(w=width, nc=2)
    pm.button(l='Circle', bgc=bg_color, w=142, c=ctrl_circle)
    pm.button(l='Square', bgc=bg_color, w=142, c=ctrl_square)
    pm.button(l='Move All', bgc=bg_color, w=142, c=ctrl_move_all)	
    pm.button(l='Sun', bgc=bg_color, w=142, c=ctrl_sun)
    pm.setParent(main)
    
    pm.rowColumnLayout(w=width, nc=4)
    pm.button(l='Frame', bgc=bg_color, w=71, c=ctrl_frame)
    pm.button(l='Triangle', bgc=bg_color, w=71, c=ctrl_tri)
    pm.button(l='Plus', bgc=bg_color, w=71, c=ctrl_plus)
    pm.button(l='Swirl', bgc=bg_color, w=71, c=ctrl_swirl)
    pm.setParent(parent_layout)
    
    return main


def rr_2D_arrows(parent_layout):
    main = pm.columnLayout(w=width/2)
    
    pm.rowColumnLayout(w=width/2, nc=2)	
    pm.button(l='Single', bgc=bg_color, w=71, c=ctrl_single)
    pm.button(l='Curved', bgc=bg_color, w=71, c=ctrl_sCurve)
    pm.button(l='Double', bgc=bg_color, w=71, c=ctrl_double)
    pm.button(l='Curved', bgc=bg_color, w=71, c=ctrl_dCurve)
    pm.setParent(main)
    
    pm.separator(w=(width-15)/2, h=5)
    
    pm.rowColumnLayout(w=width/2, nc=2)
    pm.button(l='Triple', bgc=bg_color, w=71, c=ctrl_triple)
    pm.button(l='Quad', bgc=bg_color, w=71, c=ctrl_quad)
    pm.setParent(parent_layout)
    
    return main


def rr_3D_controls(parent_layout):
    main = pm.columnLayout(w=width/2, p=parent_layout, rs=1)
    
    pm.rowColumnLayout(w=width/2, nc=2)
    pm.button(l='Cube', bgc=bg_color, w=66, c=ctrl_box)
    pm.button(l='Diamond', bgc=bg_color, w=66, c=ctrl_dia)
    pm.setParent(main)
    
    pm.rowColumnLayout(w=width/2, nc=3)
    pm.button(l='Ring', bgc=bg_color, w=45, c=ctrl_ring)
    pm.button(l='Cone', bgc=bg_color, w=44, c=ctrl_cone)
    pm.button(l='Orb', bgc=bg_color, w=44, c=ctrl_orb)
    pm.setParent(main)
    
    pm.rowColumnLayout(w=width/2, nc=3)
    pm.button(l='Lever', bgc=bg_color, w=45, c=ctrl_lever)
    pm.button(l='Jack', bgc=bg_color, w=44, c=ctrl_jake)
    pm.button(l='Point', bgc=bg_color, w=44, c=ctrl_pointer)
    pm.setParent(parent_layout)
    
    return main


def rr_letter_controls(parent_layout):
    main = pm.columnLayout(w=width/2, p=parent_layout)

    control_icon_list1 = ['E', 'K', 'L']
    pm.rowColumnLayout(w=width/2, nc=2)
    create_text_button(control_icon_list1, 70)
    pm.button(l='R', w=70, bgc=bg_color, c=pm.Callback(create_text_controls, 'R'))
    pm.setParent(main)
    
    control_icon_list2 = ['C', 'H', 'S']
    pm.rowColumnLayout(w=width/2, nc=4)
    pm.button(l='B', w=35, bgc=bg_color, c=pm.Callback(create_text_controls, 'B'))
    create_letter_button(control_icon_list2, 35)
    pm.setParent(parent_layout)
    
    return main


def rr_text_controls(parent_layout):
    main = pm.columnLayout(w=width/2, p=parent_layout)

    control_icon_list = ['Lf', 'Rt', 'Blends', 'Ik / Fk', 'COG', 'GUI']
    pm.rowColumnLayout(w=width/2, nc=2)
    create_text_button(control_icon_list, 66)
    pm.setParent(parent_layout)

    return main

    
def create_letter_button(text_list, size):
    for individual_item in text_list:
	pm.button(l=individual_item, w=size, bgc=bg_color, c=pm.Callback(create_letter_controls, individual_item))
	
	
def create_text_button(text_list, size):
    for individual_item in text_list:
	pm.button(l=individual_item, w=size, bgc=bg_color, c=pm.Callback(create_text_controls, individual_item))
    

def create_letter_controls(var):
	pm.textCurves(ch=0, f='Times New Roman', t=var)
	pm.ungroup()
	pm.ungroup()
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot as been centered.'
	

def create_text_controls(var):
	pm.textCurves(ch=0, f='Times New Roman', t=var)
	pm.ungroup()
	pm.ungroup()
	print 'Curves have been ungrouped.'
	
	curves = pm.ls(sl=True)
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
	print 'Freezing transforms on curves.'
	
	pm.pickWalk(d='Down')
	shapes = pm.ls(sl=True)
	print 'Creating a list of curve shape nodes.'
	
	parent_shapes = shapes[1:]
	delete_curves = curves[1:]
	print 'Slicing lists for parenting and deleting purposes.'
	
	pm.select(parent_shapes, r=True)
	pm.select(curves[0], add=True)
	pm.parent(r=True, s=True)
	print 'Curve list has been parented into single curve.'
	
	pm.select(delete_curves, r=True)
	pm.delete()
	print 'Unused groups have been deleted.'
	
	pm.select(curves[0])
	pm.xform(cp=True)
	print ('End result curve have been selected and its pivot has been centered.')


def ctrl_circle(*args):
	pm.circle(c=[0, 0, 0], nr=[0, 1, 0], sw=360, r=1,
		d=3, ut=0, tol=.01, s=8, ch=1)
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	
	
def ctrl_square(*args):
	pm.mel.eval('curve -d 1 -p -1 -1 0 -p -1 1 0 -p 1 1 0 -p 1 -1 0 -p -1 -1 0 -k 0 -k 1 -k 2 -k 3 -k 4')
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	

def ctrl_frame(*args):
	pm.mel.eval('curve -d 1 -p -5 5 0 -p 5 5 0 -p 5 -5 0 -p -5 -5 0 -p -5 5 0 -p -4 4 0 -p 4 4 0 -p 5 5 0 -p 4 4 0 -p 4 -4 0 -p 5 -5 0 -p 4 -4 0 -p -4 -4 0 -p -5 -5 0 -p -4 -4 0 -p -4 4 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15')
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	

def ctrl_tri(*args):
	pm.mel.eval('curve -d 1 -p -4 0 4 -p 4 0 4 -p 0 0 -3 -p -4 0 4 -k 0 -k 1 -k 2 -k 3')
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	

def ctrl_plus(*args):
	pm.mel.eval('curve -d 1 -p 0.4 0 -0.4 -p 0.4 0 -2 -p -0.4 0 -2 -p -0.4 0 -0.4 -p -2 0 -0.4 -p -2 0 0.4 -p -0.4 0 0.4 -p -0.4 0 2 -p 0.4 0 2 -p 0.4 0 0.4 -p 2 0 0.4 -p 2 0 -0.4 -p 0.4 0 -0.4 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12')
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	

def ctrl_swirl(*args):
	pm.mel.eval('curve -d 3 -p 0.474561 0 -1.241626 -p 0.171579 0 -1.214307 -p -0.434384 0 -1.159672 -p -1.124061 0 -0.419971 -p -1.169741 0 0.305922 -p -0.792507 0 1.018176 -p -0.0412486 0 1.262687 -p 0.915809 0 1.006098 -p 1.258635 0 0.364883 -p 1.032378 0 -0.461231 -p 0.352527 0 -0.810017 -p -0.451954 0 -0.43765 -p -0.634527 0 0.208919 -p -0.0751226 0 0.696326 -p 0.292338 0 0.414161 -p 0.476068 0 0.273078 -k 0 -k 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 13 -k 13')
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	

def ctrl_single(*args):
	pm.mel.eval('curve -d 1 -p -1 0 0 -p 1 0 0 -p 1 1 0 -p 1 2 0 -p 1 3 0 -p 2 3 0 -p 0 5 0 -p -2 3 0 -p -1 3 0 -p -1 2 0 -p -1 1 0 -p -1 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11')
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	

def ctrl_double(*args):
	pm.mel.eval('curve -d 1 -p 0 1 0 -p 1 1 0 -p 2 1 0 -p 3 1 0 -p 3 2 0 -p 4 1 0 -p 5 0 0 -p 4 -1 0 -p 3 -2 0 -p 3 -1 0 -p 2 -1 0 -p 1 -1 0 -p 0 -1 0 -p -1 -1 0 -p -2 -1 0 -p -3 -1 0 -p -3 -2 0 -p -4 -1 0 -p -5 0 0 -p -4 1 0 -p -3 2 0 -p -3 1 0 -p -2 1 0 -p -1 1 0 -p 0 1 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24')
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	
		
def ctrl_triple(*args):
	pm.mel.eval('curve -d 1 -p -1 1 0 -p -3 1 0 -p -3 2 0 -p -5 0 0 -p -3 -2 0 -p -3 -1 0 -p -1 -1 0 -p 1 -1 0 -p 3 -1 0 -p 3 -2 0 -p 5 0 0 -p 3 2 0 -p 3 1 0 -p 1 1 0 -p 1 3 0 -p 2 3 0 -p 0 5 0 -p -2 3 0 -p -1 3 0 -p -1 1 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19')
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	
	
def ctrl_quad(*args):
	pm.mel.eval('curve -d 1 -p 1 0 1 -p 3 0 1 -p 3 0 2 -p 5 0 0 -p 3 0 -2 -p 3 0 -1 -p 1 0 -1 -p 1 0 -3 -p 2 0 -3 -p 0 0 -5 -p -2 0 -3 -p -1 0 -3 -p -1 0 -1 -p -3 0 -1 -p -3 0 -2 -p -5 0 0 -p -3 0 2 -p -3 0 1 -p -1 0 1 -p -1 0 3 -p -2 0 3 -p 0 0 5 -p 2 0 3 -p 1 0 3 -p 1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24')
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	

def ctrl_oct(*args):
	pm.mel.eval('curve -d 1 -p -1.8975 0 0 -p -1.4025 0 0.37125 -p -1.4025 0 0.12375 -p -0.380966 0 0.157801 -p -1.079222 0 0.904213 -p -1.254231 0 0.729204 -p -1.341735 0 1.341735 -p -0.729204 0 1.254231 -p -0.904213 0 1.079222 -p -0.157801 0 0.380966 -p -0.12375 0 1.4025 -p -0.37125 0 1.4025 -p 0 0 1.8975 -p 0.37125 0 1.4025 -p 0.12375 0 1.4025 -p 0.157801 0 0.380966 -p 0.904213 0 1.079222 -p 0.729204 0 1.254231 -p 1.341735 0 1.341735 -p 1.254231 0 0.729204 -p 1.079222 0 0.904213 -p 0.380966 0 0.157801 -p 1.4025 0 0.12375 -p 1.4025 0 0.37125 -p 1.8975 0 0 -p 1.4025 0 -0.37125 -p 1.4025 0 -0.12375 -p 0.380966 0 -0.157801 -p 1.079222 0 -0.904213 -p 1.254231 0 -0.729204 -p 1.341735 0 -1.341735 -p 0.729204 0 -1.254231 -p 0.904213 0 -1.079222 -p 0.157801 0 -0.380966 -p 0.12375 0 -1.4025 -p 0.37125 0 -1.4025 -p 0 0 -1.8975 -p -0.37125 0 -1.4025 -p -0.12375 0 -1.4025 -p -0.157801 0 -0.380966 -p -0.904213 0 -1.079222 -p -0.729204 0 -1.254231 -p -1.341735 0 -1.341735 -p -1.254231 0 -0.729204 -p -1.079222 0 -0.904213 -p -0.380966 0 -0.157801 -p -1.4025 0 -0.12375 -p -1.4025 0 -0.37125 -p -1.8975 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48')
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	

def ctrl_sCurve(*args):
	pm.mel.eval('curve -d 1 -p -0.251045 0 1.015808 -p -0.761834 0 0.979696 -p -0.486547 0 0.930468 -p -0.570736 0 0.886448 -p -0.72786 0 0.774834 -p -0.909301 0 0.550655 -p -1.023899 0 0.285854 -p -1.063053 0 9.80765e-009 -p -0.961797 0 8.87346e-009 -p -0.926399 0 0.258619 -p -0.822676 0 0.498232 -p -0.658578 0 0.701014 -p -0.516355 0 0.802034 -p -0.440202 0 0.841857 -p -0.498915 0 0.567734 -p -0.251045 0 1.015808 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15')
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	
		
def ctrl_dCurve(*args):
	pm.mel.eval('curve -d 1 -p -0.251045 0 -1.015808 -p -0.761834 0 -0.979696 -p -0.486547 0 -0.930468 -p -0.570736 0 -0.886448 -p -0.72786 0 -0.774834 -p -0.909301 0 -0.550655 -p -1.023899 0 -0.285854 -p -1.063053 0 9.80765e-009 -p -1.023899 0 0.285854 -p -0.909301 0 0.550655 -p -0.72786 0 0.774834 -p -0.570736 0 0.886448 -p -0.486547 0 0.930468 -p -0.761834 0 0.979696 -p -0.251045 0 1.015808 -p -0.498915 0 0.567734 -p -0.440202 0 0.841857 -p -0.516355 0 0.802034 -p -0.658578 0 0.701014 -p -0.822676 0 0.498232 -p -0.926399 0 0.258619 -p -0.961797 0 8.87346e-009 -p -0.926399 0 -0.258619 -p -0.822676 0 -0.498232 -p -0.658578 0 -0.701014 -p -0.516355 0 -0.802034 -p -0.440202 0 -0.841857 -p -0.498915 0 -0.567734 -p -0.251045 0 -1.015808 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28')	
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	
		
def ctrl_180(*args):
	pm.mel.eval('circle -c 0 0 0 -nr 0 1 0 -sw -180 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 0')	
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	

def ctrl_270(*args):
	pm.mel.eval('curve -d 3 -p -0.707107 0 -0.707107 -p -0.570265 0 -0.843948 -p -0.205819 0 -1.040044 -p 0.405223 0 -0.978634 -p 0.881027 0 -0.588697 -p 1.059487 0 0 -p 0.881027 0 0.588697 -p 0.405223 0 0.978634 -p -0.205819 0 1.040044 -p -0.570265 0 0.843948 -p -0.707107 0 0.707107 -k 0 -k 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 8 -k 8')	
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	
	
def ctrl_sun(*args):
	ctrl = pm.mel.eval('curve -d 3 -p 7.06316e-009 0 -1 -p 0.104714 0 -0.990425 -p 0.314142 0 -0.971274 -p 0.597534 0 -0.821244 -p 0.822435 0 -0.597853 -p 0.96683 0 -0.314057 -p 1.016585 0 -2.28604e-005 -p 0.96683 0 0.314148 -p 0.822435 0 0.597532 -p 0.597534 0 0.822435 -p 0.314142 0 0.96683 -p 1.22886e-008 0 1.016585 -p -0.314142 0 0.96683 -p -0.597534 0 0.822435 -p -0.822435 0 0.597532 -p -0.96683 0 0.314148 -p -1.016585 0 -2.29279e-005 -p -0.96683 0 -0.314057 -p -0.822435 0 -0.597853 -p -0.597534 0 -0.821244 -p -0.314142 0 -0.971274 -p -0.104714 0 -0.990425 -p 7.06316e-009 0 -1 -k 0 -k 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 20 -k 20')
	pm.select((ctrl + '.ep[1]'), (ctrl + '.ep[3]'), (ctrl + '.ep[5]'), (ctrl + '.ep[7]'), (ctrl + '.ep[9]'), (ctrl + '.ep[11]'), (ctrl + '.ep[13]'), (ctrl + '.ep[15]'), (ctrl + '.ep[17]'), (ctrl + '.ep[19]'), r=True)
	pm.scale(0.732056, 0.732056, 0.732056, p=[0, 0, 0], r=True)
	pm.select(ctrl)
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	
		
def ctrl_move_all(*args):
	base_circle = pm.mel.eval('circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1.5 -d 3 -ut 0 -tol 0.01 -s 8 -ch 0')
	arrow_list = []
	arrow1 = pm.mel.eval('curve -d 1 -p 1.75625 0 0.115973 -p 1.75625 0 -0.170979 -p 2.114939 0 -0.170979 -p 2.114939 0 -0.314454 -p 2.473628 0 -0.0275029 -p 2.114939 0 0.259448 -p 2.114939 0 0.115973 -p 1.75625 0 0.115973 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7')
	arrow2 = pm.mel.eval('curve -d 1 -p 0.143476 0 -1.783753 -p 0.143476 0 -2.142442 -p 0.286951 0 -2.142442 -p 0 0 -2.501131 -p -0.286951 0 -2.142442 -p -0.143476 0 -2.142442 -p -0.143476 0 -1.783753 -p 0.143476 0 -1.783753 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7')
	arrow3 = pm.mel.eval('curve -d 1 -p -1.75625 0 -0.170979 -p -2.114939 0 -0.170979 -p -2.114939 0 -0.314454 -p -2.473628 0 -0.0275029 -p -2.114939 0 0.259448 -p -2.114939 0 0.115973 -p -1.75625 0 0.115973 -p -1.75625 0 -0.170979 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7')
	arrow4 = pm.mel.eval('curve -d 1 -p -0.143476 0 1.728747 -p -0.143476 0 2.087436 -p -0.286951 0 2.087436 -p 0 0 2.446125 -p 0.286951 0 2.087436 -p 0.143476 0 2.087436 -p 0.143476 0 1.728747 -p -0.143476 0 1.728747 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7')
	arrow_list.append(arrow1)
	arrow_list.append(arrow2)
	arrow_list.append(arrow3)
	arrow_list.append(arrow4)
	print 'Curves have been created and positioned.'
	
	pm.select(arrow_list)
	pm.pickWalk(d='Down')
	pm.select(base_circle, add=True)
	pm.parent(r=True, s=True)
	print 'Curve list has been parented into single curve.'
	
	pm.delete(arrow_list)
	print 'Unused groups have been deleted.'
	
	pm.select(base_circle)
	pm.xform(cp=True)
	print ('End result curve have been selected and its pivot has been centered.')
	

def ctrl_box(*args):
	pm.mel.eval('curve -d 1 -p 0.5 0.5 0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15')
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	
		
def ctrl_dia(*args):
	pm.mel.eval('curve -d 1 -p 0 0.699773 0 -p 0.707107 -0.00175397 0 -p 9.27258e-08 -0.00733389 -0.707107 -p 0 0.699773 0 -p 9.27258e-08 -0.00733389 -0.707107 -p -0.707107 -0.00175397 6.18172e-08 -p 0 0.699773 0 -p -0.707107 -0.00733389 -6.18172e-08 -p -3.09086e-08 -0.00733389 0.707107 -p 0 0.699773 0 -p -3.09086e-08 -0.00733389 0.707107 -p 0.707107 -0.00175397 0 -p 0 -0.708861 0 -p -3.09086e-08 -0.00733389 0.707107 -p 0 -0.708861 0 -p -0.707107 -0.00733389 -6.18172e-08 -p 0 -0.708861 0 -p 9.27258e-08 -0.00733389 -0.707107 -p 0 -0.708861 0 -p 0.707107 -0.00733389 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19')
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	

def ctrl_ring(*args):
	pm.mel.eval('curve -d 1 -p -1 0.0916408 0 -p -0.707107 0.0916408 0.707107 -p 0 0.0916408 1 -p 0.707107 0.0916408 0.707107 -p 1 0.0916408 0 -p 0.707107 0.0916408 -0.707107 -p 0 0.0916408 -1 -p -0.707107 0.0916408 -0.707107 -p -1 0.0916408 0 -p -1 -0.0916408 0 -p -0.707107 -0.0916408 -0.707107 -p -0.707107 0.0916408 -0.707107 -p -0.707107 -0.0916408 -0.707107 -p 0 -0.0916408 -1 -p 0 0.0916408 -1 -p 0 -0.0916408 -1 -p 0.707107 -0.0916408 -0.707107 -p 0.707107 0.0916408 -0.707107 -p 0.707107 -0.0916408 -0.707107 -p 1 -0.0916408 0 -p 1 0.0916408 0 -p 1 -0.0916408 0 -p 0.707107 -0.0916408 0.707107 -p 0.707107 0.0916408 0.707107 -p 0.707107 -0.0916408 0.707107 -p 0 -0.0916408 1 -p 0 0.0916408 1 -p 0 -0.0916408 1 -p -0.707107 -0.0916408 0.707107 -p -0.707107 0.0916408 0.707107 -p -0.707107 -0.0916408 0.707107 -p -1 -0.0916408 0 -p -1 0.0916408 0 -p -1 -0.0916408 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33')
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	

def ctrl_cone(*args):
	pm.mel.eval('curve -d 1 -p 0.5 -1 0.866025 -p -0.5 -1 0.866025 -p 0 1 0 -p 0.5 -1 0.866025 -p 1 -1 0 -p 0 1 0 -p 0.5 -1 -0.866025 -p 1 -1 0 -p 0 1 0 -p -0.5 -1 -0.866026 -p 0.5 -1 -0.866025 -p 0 1 0 -p -1 -1 -1.5885e-007 -p -0.5 -1 -0.866026 -p 0 1 0 -p -0.5 -1 0.866025 -p -1 -1 -1.5885e-007 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16')
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	
	
def ctrl_orb(*args):
	pm.mel.eval('circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 1')
	base_circle = pm.ls(sl=True)
	
	pm.duplicate(rr=True)
	dup1 = pm.ls(sl=True)
	pm.setAttr(dup1[0] + '.rotateX', 90)
	
	pm.duplicate(rr=True)
	dup2 = pm.ls(sl=True)
	pm.setAttr(dup2[0] + '.rotateY', 90)

	pm.duplicate(rr=True)
	dup3 = pm.ls(sl=True)
	pm.setAttr(dup3[0] + '.rotateY', 45)
	print 'Curves have been created and positioned.'
	
	pm.select(base_circle, dup1, dup2, dup3)
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
	print 'Freezing transforms on curves.'

	pm.select(dup1, dup2, dup3, r=True)
	curves = pm.ls(sl=True)
	pm.pickWalk(d='Down')
	pm.select(base_circle, add=True)
	pm.parent(r=True, s=True)
	print 'Curve list has been parented into single curve.'
	
	pm.delete(curves)
	print 'Unused groups have been deleted.'
	
	pm.select(base_circle)
	pm.xform(cp=True)
	print ('End result curve have been selected and its pivot has been centered.')
	

def ctrl_lever(*args):
	pm.mel.eval('curve -d 1 -p 0 -1 0 -p 0 -2 0 -p 0 -3 0 -p 0 -4 0 -p 0 -5 0 -k 0 -k 1 -k 2 -k 3 -k 4')
	line = pm.ls(sl=True)
	print 'Line curve has been created.'
	
	pm.mel.eval('circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 1')
	base_circle = pm.ls(sl=True)
	
	
	pm.duplicate(rr=True)
	circle_dup1 = pm.ls(sl=True)
	pm.setAttr(circle_dup1[0] + '.rotateX', 90)
	
	pm.duplicate(rr=True)
	circle_dup2 = pm.ls(sl=True)
	pm.setAttr(circle_dup2[0] + '.rotateY', 90)
		
	pm.duplicate(rr=True)
	circle_dup3 = pm.ls(sl=True)
	pm.setAttr(circle_dup3[0] + '.rotateY', 45)
	print 'Circle curves have been created.'
	
	pm.select(line, base_circle, circle_dup1, circle_dup2, circle_dup3, r=True)
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
	print 'Freezing transforms on curves.'
	
	pm.select(line, circle_dup1, circle_dup2, circle_dup3)
	curves = pm.ls(sl=True)
	pm.pickWalk(d='Down')
	shapes = pm.ls(sl=True)
	
	pm.select(shapes, base_circle, r=True)
	pm.parent(r=True, s=True)
	print 'Curve list has been parented into single curve.'
	
	pm.delete(curves)
	print 'Unused groups have been deleted.'
	
	pm.select(base_circle, r=True)
	pm.xform(cp=True)
	print 'End result curve have been selected and its pivot has been centered.'
	
	
def ctrl_jake(*args):
	pm.mel.eval('curve -d 1 -p 0 0 0 -p 0.75 0 0 -p 1 0.25 0 -p 1.25 0 0 -p 1 -0.25 0 -p 0.75 0 0 -p 1 0 0.25 -p 1.25 0 0 -p 1 0 -0.25 -p 1 0.25 0 -p 1 0 0.25 -p 1 -0.25 0 -p 1 0 -0.25 -p 0.75 0 0 -p 0 0 0 -p -0.75 0 0 -p -1 0.25 0 -p -1.25 0 0 -p -1 -0.25 0 -p -0.75 0 0 -p -1 0 0.25 -p -1.25 0 0 -p -1 0 -0.25 -p -1 0.25 0 -p -1 0 0.25 -p -1 -0.25 0 -p -1 0 -0.25 -p -0.75 0 0 -p 0 0 0 -p 0 0.75 0 -p 0 1 -0.25 -p 0 1.25 0 -p 0 1 0.25 -p 0 0.75 0 -p -0.25 1 0 -p 0 1.25 0 -p 0.25 1 0 -p 0 1 0.25 -p -0.25 1 0 -p 0 1 -0.25 -p 0.25 1 0 -p 0 0.75 0 -p 0 0 0 -p 0 -0.75 0 -p 0 -1 -0.25 -p 0 -1.25 0 -p 0 -1 0.25 -p 0 -0.75 0 -p -0.25 -1 0 -p 0 -1.25 0 -p 0.25 -1 0 -p 0 -1 -0.25 -p -0.25 -1 0 -p 0 -1 0.25 -p 0.25 -1 0 -p 0 -0.75 0 -p 0 0 0 -p 0 0 -0.75 -p 0 0.25 -1 -p 0 0 -1.25 -p 0 -0.25 -1 -p 0 0 -0.75 -p -0.25 0 -1 -p 0 0 -1.25 -p 0.25 0 -1 -p 0 0.25 -1 -p -0.25 0 -1 -p 0 -0.25 -1 -p 0.25 0 -1 -p 0 0 -0.75 -p 0 0 0 -p 0 0 0.75 -p 0 0.25 1 -p 0 0 1.25 -p 0 -0.25 1 -p 0 0 0.75 -p -0.25 0 1 -p 0 0 1.25 -p 0.25 0 1 -p 0 0.25 1 -p -0.25 0 1 -p 0 -0.25 1 -p 0.25 0 1 -p 0 0 0.75 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 -k 70 -k 71 -k 72 -k 73 -k 74 -k 75 -k 76 -k 77 -k 78 -k 79 -k 80 -k 81 -k 82 -k 83')
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'
	
		
def ctrl_pointer(*args):
	pm.mel.eval('curve -d 1 -p -1 0 0 -p 1 0 0 -p 1 1 0 -p 1 2 0 -p 1 3 0 -p 2 3 0 -p 0 5 0 -p -2 3 0 -p -1 3 0 -p -1 2 0 -p -1 1 0 -p -1 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11')
	ctrl = pm.ls(sl=True)
	pm.duplicate(rr=True)
	ctrl2 = pm.ls(sl=True)
	pm.setAttr(ctrl2[0] + '.rotateY', 90)
	print 'Curves have been positioned.'
	
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
	print 'Freezing transforms on curves.'
	
	pm.select(ctrl, r=True)
	pm.pickWalk(d='Down')
	pm.select(ctrl2, add=True)
	pm.parent(r=True, s=True)
	print 'Curves have been parented into single curve.'
	
	pm.delete(ctrl)
	print 'Unsuded groups have been deleted.'
	
	pm.select(ctrl2)
	pm.xform(cp=True)
	print 'Curve has been selected and its pivot has been centered.'






