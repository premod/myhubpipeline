# script for getting intersecting vertices: http://maya-tricks.blogspot.com/2009/04/python.html
# modified and developed by Truong Cg Artist: gumroad.com/TruongCgArtist

import maya.cmds as cmds
import pymel.core as pm
import maya.mel as mel
import maya.OpenMaya as OpenMaya
from math import fmod
from math import pow,sqrt

propList = []
propList_tf = "prop_list_text_field"
mainBody = None
mainBody_tf = "main_body_text_field"
controlCheck = False
mainRigControl = None
mainRigControl_tf = "main_rig_control_text_field"
win_ID = "Attach_Props_To_Character_Surface_Tool"
customPivotVertexList = []
customPivotVertexList_tf = "custom_pivot_text_field"

def createFollicle(vertex, bodyMesh):
    geo = pm.PyNode(bodyMesh)
    uvMap = pm.polyListComponentConversion(vertex, fv=True, tuv=True)
    uvCoord = pm.polyEditUV(uvMap, q=True)

    fol = pm.createNode('transform', ss=True)
    folShape = pm.createNode('follicle', n=fol.name() + 'Shape', p=fol, ss=True)
    print fol
    print folShape
    pm.setAttr(folShape+".visibility", 0)
    if not pm.objExists("follicleGroup"):
        pm.group(n="follicleGroup", empty=True)
    pm.parent(fol, "follicleGroup")

    pm.connectAttr(geo + '.outMesh', folShape + '.inputMesh')
    pm.connectAttr(geo + '.worldMatrix[0]', folShape + '.inputWorldMatrix')
    pm.connectAttr(folShape + '.outRotate', fol + '.rotate')
    pm.connectAttr(folShape + '.outTranslate', fol + '.translate')
    fol.inheritsTransform.set(False)
    folShape.parameterU.set(uvCoord[0])
    folShape.parameterV.set(uvCoord[1])
    return str(fol)

def pyRayIntersect(mesh, point, direction=(0.0, 1.0, 0.0)):
    OpenMaya.MGlobal.selectByName(mesh,OpenMaya.MGlobal.kReplaceList)
    sList = OpenMaya.MSelectionList()
    # Assign current selection to the selection list object
    OpenMaya.MGlobal.getActiveSelectionList(sList)
    item = OpenMaya.MDagPath()
    sList.getDagPath(0, item)
    item.extendToShape()
    fnMesh = OpenMaya.MFnMesh(item)
    raySource = OpenMaya.MFloatPoint(point[0], point[1], point[2], 1.0)
    rayDir = OpenMaya.MFloatVector(direction[0], direction[1], direction[2])
    faceIds = None
    triIds = None
    idsSorted = False
    testBothDirections = False
    worldSpace = OpenMaya.MSpace.kWorld
    maxParam = 999999
    accelParams = None
    sortHits = True
    hitPoints = OpenMaya.MFloatPointArray()
    #hitRayParams = OM.MScriptUtil().asFloatPtr()
    hitRayParams = OpenMaya.MFloatArray()
    hitFaces = OpenMaya.MIntArray()
    hitTris = None
    hitBarys1 = None
    hitBarys2 = None
    tolerance = 0.0001
    hit = fnMesh.allIntersections(raySource, rayDir, faceIds, triIds, idsSorted, worldSpace, maxParam, testBothDirections, accelParams, sortHits, hitPoints, hitRayParams, hitFaces, hitTris, hitBarys1, hitBarys2, tolerance)
    result = int(fmod(len(hitFaces), 2))

    #clear selection as may cause problem if the function is called multiple times in succession
    #OM.MGlobal.clearSelectionList()
    return result

def testIntersect(bodyMesh, prop):
    container = bodyMesh
    checkInsideObj = prop
    allVtx = pm.ls(str(checkInsideObj) + '.vtx[*]', fl=1)
    allIn = []
    for eachVtx in allVtx:
        location = pm.pointPosition(eachVtx, w=1)
        test = pyRayIntersect(container, location, (0, 1, 0))
        if (test):
            allIn.append(eachVtx)
    pm.select(allIn)
    return allIn

def getCenterOfVertices(vertices):
    n = len(vertices)
    centerX = 0
    centerY = 0
    centerZ = 0
    for ver in vertices:
        pos = cmds.xform(ver, q=True, translation=True, ws=True)
        print pos
        centerX = centerX + pos[0]
        centerY = centerY + pos[1]
        centerZ = centerZ + pos[2]
    centerPos = [centerX/n, centerY/n, centerZ/n]
    return centerPos

def getClosestVert(propGeo, mainBodyGeo):
    geo = pm.PyNode(mainBodyGeo) # user input (from UI) needed!
    fPG = pm.PyNode(propGeo) # convert to PyNode
    pos = fPG.getRotatePivot(space='world')

    nodeDagPath = OpenMaya.MObject()
    try:
        selectionList = OpenMaya.MSelectionList()
        selectionList.add(geo.name())
        nodeDagPath = OpenMaya.MDagPath()
        selectionList.getDagPath(0, nodeDagPath)
    except:
        raise RuntimeError('OpenMaya.MDagPath() failed on %s' % geo.name())

    mfnMesh = OpenMaya.MFnMesh(nodeDagPath)

    pointA = OpenMaya.MPoint(pos.x, pos.y, pos.z)
    pointB = OpenMaya.MPoint()
    space = OpenMaya.MSpace.kWorld

    util = OpenMaya.MScriptUtil()
    util.createFromInt(0)
    idPointer = util.asIntPtr()

    mfnMesh.getClosestPoint(pointA, pointB, space, idPointer)
    idx = OpenMaya.MScriptUtil(idPointer).asInt()

    faceVerts = [geo.vtx[i] for i in geo.f[idx].getVertices()]
    closestVert = None
    minLength = None
    for v in faceVerts:
        thisLength = (pos - v.getPosition(space='world')).length()
        if minLength is None or thisLength < minLength:
            minLength = thisLength
            closestVert = v
    return str(closestVert)

def getMaxSize(propGeo):
    bBox= cmds.exactWorldBoundingBox(propGeo)
    lengthX = bBox[3]-bBox[0]
    lengthY = bBox[4]-bBox[1]
    lengthZ = bBox[5]-bBox[2]
    maxLength = max(lengthX, lengthY, lengthZ)
    return maxLength

def GetDistance(objA, objB):
    gObjA = cmds.xform(objA, q=True, t=True, ws=True)
    gObjB = cmds.xform(objB, q=True, t=True, ws=True)
    return sqrt(pow(gObjA[0] - gObjB[0], 2) + pow(gObjA[1] - gObjB[1], 2) + pow(gObjA[2] - gObjB[2], 2))

def findClosestVerToCurrentVer(currentVer, mainMesh):
    # find the closest vertex on main mesh to current vertex (on prop)
    pos = []
    pos = cmds.xform(currentVer, q=1, ws=1, t=1)
    print pos
    cpom = cmds.createNode('closestPointOnMesh')
    shape = cmds.listRelatives(mainMesh, s=True)[0]
    cmds.connectAttr('%s.outMesh' % shape, '%s.inMesh' % cpom)
    cmds.setAttr('%s.inPosition' % cpom, pos[0], pos[1], pos[2], type="double3")

    # vertex index
    vtxIndx = cmds.getAttr(cpom + ".closestVertexIndex")
    print vtxIndx
    closestVer = "{0}.vtx[{1}]".format(mainMesh, vtxIndx)
    print closestVer

    # delete node when done calculating
    cmds.delete(cpom)

    return closestVer

def closestVerToSurface(verList, mainMesh):
    minDistance = 9999999999999
    minClosestVer = None
    for ver in verList:
        closestVer = findClosestVerToCurrentVer(ver, mainMesh)
        distance = GetDistance(ver, closestVer)
        print(distance)
        if distance <= minDistance:
            minDistance = distance
            minClosestVer = ver

    if not minClosestVer:
        raise Exception("Cannot find the closest vertex")
    return minClosestVer

def attachProp(propList, bodyMesh):
    if not propList:
        raise Exception("No prop is defined")
    if not bodyMesh:
        raise Exception("No body mesh is defined")
    if not mainRigControl:
        raise Exception("No main rig control is defined")

    for prop in propList:
        if customPivotVertexList:
            centerPos = getCenterOfVertices(customPivotVertexList)
            cmds.xform(prop, pivots=centerPos, ws=True)
        else:
            # find intersecting vertices
            inVerList = testIntersect(mainBody, prop)
            if inVerList:
                # if the prop intersects with body mesh, use intersect vertices' center for pivot of the prop
                # how to find the closest vertice to the mainBody surface?

                # # this extra step is for avoiding Maya crash
                # selectedVertices = cmds.ls(sl=True)

                # centerPos = getCenterOfVertices(selectedVertices)
                # cmds.xform(prop, pivots=centerPos, ws=True)

                # this step of selecting inVerList is to avoid Maya crash
                selectedVertices = cmds.ls(sl=True, flatten=1)
                closestVerOnMainBody = closestVerToSurface(selectedVertices, mainBody)
                closestVerOnMainBodyPos = cmds.xform(closestVerOnMainBody, q=1, ws=1, t=1)
                cmds.xform(prop, pivots=closestVerOnMainBodyPos, ws=True)

            else:
                # center pivot the prop
                cmds.xform(prop, centerPivots=1)
                # find closest vertex on body mesh to the prop's center pivot
                nearestVerOnBodyMesh = getClosestVert(prop, bodyMesh)
                # create & place a body-locator at this vertex
                bodyLoc = cmds.spaceLocator(absolute=1, position=cmds.xform(nearestVerOnBodyMesh, q=1, translation=True))[0]
                # find closest vertex on prop to this body-locator
                nearestVerOnProp = getClosestVert(bodyLoc, prop)
                # delete body-locator
                cmds.delete(bodyLoc)
                # set prop pivot to the closest vertex on prop
                cmds.xform(prop, pivots=cmds.xform(nearestVerOnProp, q=1, translation=True), ws=True)

        # find the closest vertex to this pivot
        nearestVertex = getClosestVert(prop, bodyMesh)
        cmds.select(nearestVertex, r=True)
        # create follicle at this vertex
        folName = createFollicle(nearestVertex, mainBody)

        if controlCheck == True:
            cmds.select(clear=True)
            # create offset group
            propGrp = cmds.group(name=prop+"_offset", empty=True)
            # get bounding box size of prop for radius of control
            # >>> HOW ABOUT GETTING THE SIZE OF INTERSECTING VERTICES FOR CONTROL SIZE
            propSize = getMaxSize(prop)
            # create controls
            propCtrl = cmds.circle(ch=0, name=prop+"_con", radius=propSize/2*1.2)
            # turn on overrides, then set curve color
            propCtrlShape = cmds.listRelatives(propCtrl, shapes=True)[0]
            cmds.setAttr(propCtrlShape + ".overrideEnabled", 1)
            cmds.setAttr(propCtrlShape + '.overrideColor', 20)

            cmds.parent(propCtrl, propGrp)

            # constraint the offset group to the prop pivot, then delete constraint
            cmds.pointConstraint(prop, propGrp, mo=False)
            cmds.delete(propGrp, constraints=1)
            # parent the offset group under the follicle
            cmds.parent(propGrp, folName)
            cmds.xform(propGrp, absolute=1, rotation=[0, 0, 0], scale=[1, 1, 1])
            cmds.parentConstraint(propCtrl, prop, mo=True)
        else:
            # parent constraint the prop to this follicle
            cmds.parentConstraint(folName, prop, mo=True)
        cmds.scaleConstraint(mainRigControl, prop)
        # this one makes the script run slower but visually pleasing
        cmds.refresh()

def find_most_influential_jnt(bodySkin, closestVert):
    # queries all joints influencing the current vertex with value above given threshold
    influences = cmds.skinPercent(bodySkin, closestVert, q=True, ignoreBelow=0.2, t=None)
    print influences
    inf_values_dict = {}
    for systemJnt in influences:
        inf_values_dict[systemJnt] = cmds.skinPercent(bodySkin, closestVert, q=True, t=systemJnt)

    sorted_inf_values = sorted(inf_values_dict.items(), key=lambda x: x[-1], reverse=True)
    # returns a list of tuples of each joint and its influence value
    # sorted by the influence value (key to sort is the result of lambda function: x[-1]: value of each key in dict)
    print sorted_inf_values
    # get the first item in the list
    most_influential_jnt = sorted_inf_values[0][0] # index 2 times to get the system joint name
    return most_influential_jnt

def createJoints():
    # query the main body's skincluster name
    bodySkin = mel.eval('findRelatedSkinCluster ' + mainBody)
    print bodySkin
    if not bodySkin:
        raise Exception("Body skinCluster is not found, you must create skinCluster for body mesh first")
    # find follicleGroup >> if not exist >> raise error
    if not cmds.objExists("follicleGroup"):
        raise Exception("Please run Attach Props first")
    for prop in propList:
        # list connection of prop, to find who parent constraint them (prop parent) >> if find nothing >> raise error
        parentConList = cmds.listRelatives(prop, children=True, type='constraint')
        if not parentConList:
            raise Exception("This prop has no constraint")
        parentCon = parentConList[0]
        # get parent: follicle/ control which drive the prop
        prop_parent = cmds.parentConstraint(parentCon, q=1, targetList=1)
        # delete the constraints since we wont need it, skincluster will drive the prop
        cmds.delete(prop, constraints=1)
        # create joints at prop positions (prop joint
        cmds.select(clear=True)
        prop_jnt = cmds.joint(name=prop+"_fol_jnt")
        # get closest Vertex on Body from prop
        nearest_ver = getClosestVert(prop, mainBody)
        # find its biggest influence (main joint in the system)
        main_jnt = find_most_influential_jnt(bodySkin, nearest_ver)
        # parent prop joint under this main joint
        cmds.parent(prop_jnt, main_jnt)
        # parent constraint (propParent, propJnt), with no offset, otherwise props will go crazy
        cmds.parentConstraint(prop_parent, prop_jnt, mo=False)
        # scale constraint (Main, propJnt)
        cmds.scaleConstraint(mainRigControl, prop_jnt, mo=True)
        # bind skin propJoint to prop
        cmds.skinCluster(prop_jnt, prop, skinMethod=0, toSelectedBones=1)

def deleteSetup():
    # remove skin history
    for prop in propList:
        propSkin = mel.eval('findRelatedSkinCluster ' + prop)
        if propSkin:
            cmds.skinCluster(prop, unbind=True, edit=True)
    # delete joints
    folJntList = cmds.ls("*_{}".format("fol_jnt"))
    if folJntList:
        cmds.delete(folJntList)
    # delete constraint
    if cmds.objExists("follicleGroup"):
        cmds.delete("follicleGroup")
    cmds.delete(propList, constraints=1)

def load_selected_as(sel, text_field):
    strTF = ''.join(sel)
    text_field = cmds.textField(text_field, e=True, tx=strTF)

def show_UI(winID):
    if cmds.window(winID, exists=True):
        cmds.deleteUI(winID)
    cmds.window(winID)
    create_UI(winID)
    cmds.showWindow(winID)

def setPropList():
    global propList
    propList = cmds.ls(sl=True)
    if not propList:
        raise Exception("Please select some props")
    load_selected_as(propList, propList_tf)
    print propList

def setMainBody():
    global mainBody
    mainBody = cmds.ls(sl=True)[0]
    if not mainBody:
        raise Exception("Please select the main character body")
    load_selected_as(mainBody, mainBody_tf)
    print mainBody

def setMainRigControl():
    global mainRigControl
    mainRigControl = cmds.ls(sl=True)[0]
    if not mainRigControl:
        raise Exception("Please select the main rig control")
    load_selected_as(mainRigControl, mainRigControl_tf)
    print mainRigControl

def checkBoxOn():
    global controlCheck
    controlCheck = True
    return controlCheck

def checkBoxOff():
    global controlCheck
    controlCheck = False
    return controlCheck

def setCustomPivot():
    global customPivotVertexList
    customPivotVertexList = cmds.ls(sl=True, flatten=True)
    load_selected_as(customPivotVertexList, customPivotVertexList_tf)
    print customPivotVertexList

def create_UI(winID):
    window_size = (400, 320)
    cmds.window(winID, e=True, wh=window_size)

    txt_field_width = 370

    main_lo = cmds.columnLayout(p=winID)

    cmds.text("\n Select Props: ")
    set_props_lo = cmds.rowLayout(p=main_lo, nc=2, cw2=(txt_field_width, 25))
    cmds.textField(propList_tf, w=txt_field_width, ed=False)
    set_faces_btn = cmds.button(label=">>", p=set_props_lo, c='setPropList()', width=25)

    cmds.text("\n Select Main Body: ", p=main_lo)
    set_main_body_lo = cmds.rowLayout(p=main_lo, nc=2, cw2=(txt_field_width, 25))
    cmds.textField(mainBody_tf, w=txt_field_width, ed=False)
    set_vertices_btn = cmds.button(label=">>", p=set_main_body_lo, c='setMainBody()', width=25)

    cmds.text("\n Select Main Rig Control (for scale constraint): ", p=main_lo)
    set_main_rig_lo = cmds.rowLayout(p=main_lo, nc=2, cw2=(txt_field_width, 25))
    cmds.textField(mainRigControl_tf, w=txt_field_width, ed=False)
    set_vertices_btn = cmds.button(label=">>", p=set_main_rig_lo, c='setMainRigControl()', width=25)

    cmds.text("\n Optional: select vertex(s) for custom pivot (for single prop case only): ", p=main_lo)
    set_pivot_lo = cmds.rowLayout(p=main_lo, nc=2, cw2=(txt_field_width, 25))
    cmds.textField(customPivotVertexList_tf, w=txt_field_width, ed=False)
    set_vertices_btn = cmds.button(label=">>", p=set_pivot_lo, c='setCustomPivot()', width=25)

    sep1 = cmds.separator(w=window_size[0], h=20, p=main_lo)
    ctrlBox1 = cmds.checkBox(label='Create Prop Controls', value=False, onCommand='checkBoxOn()', offCommand='checkBoxOff()', p=main_lo)

    sep2 = cmds.separator(w=window_size[0], h=20, p=main_lo)

    attach_prop_lo = cmds.rowLayout(p=main_lo, nc=3)
    attach_btn = cmds.button(label="Attach Props", p=attach_prop_lo, c='attachProp(propList, mainBody)', width=130, align="left")
    createJnt_btn = cmds.button(label="Create Joints (for Game)", p=attach_prop_lo, c='createJoints()', width=130, align="left")
    delete_btn = cmds.button(label="Delete Setup", p=attach_prop_lo, c='deleteSetup()', width=130, align="left")

show_UI(win_ID)