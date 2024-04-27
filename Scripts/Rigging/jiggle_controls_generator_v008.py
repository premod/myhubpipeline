# Jiggle Control Generator by Truong Cg Artist
# gumroad.com/TruongCgArtist

import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm
import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim

originalMesh = None
originalMesh_tf = "original_mesh_text_field"
mainControl = None
mainControl_tf = "main_control_text_field"
bsStage = 0
mainBlendshape = None
mainBlendshape_tf = "main_blendshape_text_field"
controlName = None
controlName_tf = "control_name_text_field"
blendshapeTarget = None
blendshapeTargetMesh = None
follicleMesh = None
oriMeshSkin = None
jiggleJntList = []
rightVerList = []
leftVerList = []
jiggleConRadius = 1.0

print(originalMesh)

win_ID = "Jiggle_Controls_Generator"

def createJiggleGroupStructure():
    if not cmds.objExists("JiggleSetup"):
        cmds.select(clear=1)
        cmds.group(name="JiggleControlGrp", world=1, empty=1)
        cmds.group(name="JiggleSetup")
        cmds.select(clear=1)
        cmds.group(name="FollicleGrp", world=1, empty=1)
        cmds.parent("FollicleGrp", "JiggleSetup")
        cmds.group(name="JiggleJointsGrp", world=1, empty=1)
        cmds.parent("JiggleJointsGrp", "JiggleSetup")

        # need L, M, R for JiggleControlGrp & JiggleJointsGrp
        cmds.group(name="JiggleJointsMiddle", world=1, empty=1)
        cmds.parent("JiggleJointsMiddle", "JiggleJointsGrp")
        cmds.group(name="JiggleJointsLeft", world=1, empty=1)
        cmds.parent("JiggleJointsLeft", "JiggleJointsGrp")
        cmds.group(name="JiggleJointsRight", world=1, empty=1)
        cmds.parent("JiggleJointsRight", "JiggleJointsGrp")

        cmds.group(name="JiggleControlMiddle", world=1, empty=1)
        cmds.parent("JiggleControlMiddle", "JiggleControlGrp")
        cmds.group(name="JiggleControlLeft", world=1, empty=1)
        cmds.parent("JiggleControlLeft", "JiggleControlGrp")
        cmds.group(name="JiggleControlRight", world=1, empty=1)
        cmds.parent("JiggleControlRight", "JiggleControlGrp")

        cmds.hide("FollicleGrp")
        cmds.hide("JiggleJointsGrp")

        # Do not create base joint if already exists. Base joint has no control.
        if not cmds.objExists("base_jiggle_jnt"):
            cmds.select(clear=1)
            cmds.joint(name="base_jiggle_jnt")
            # base joint need to be hidden
            cmds.parent("base_jiggle_jnt", "JiggleJointsGrp")

def createBlendshapeTarget(blendshapeNode):
    global blendshapeTarget
    # check if the blendshape node having matching "_JiggleBlendshape"
    # if yes, this is the blendshape target
    # if not, create a new blendshape target _JiggleBlendshape 
    currentBlendshapeTargets = cmds.listAttr(blendshapeNode+'.w', m=1)
    if currentBlendshapeTargets:
        match = True in (("_JiggleBlendshape") in bst for bst in currentBlendshapeTargets)
        if match:
            for bst in currentBlendshapeTargets:
                if ("_JiggleBlendshape") in bst:
                    blendshapeTarget = bst

        else:
            # create new blendshape target under this blendshape node
            weightCount = cmds.blendShape(mainBlendshape, q=True, wc=True)
            cmds.blendShape(mainBlendshape, e=1, target=(originalMesh, weightCount + 1, blendshapeTarget, 1.0))
            cmds.blendShape(mainBlendshape, e=1, weight=[weightCount + 1, 1.0])

def checkAndCreateBST():
    global originalMesh
    global blendshapeTargetMesh
    global blendshapeTarget
    global mainBlendshape

    # create structure first
    createJiggleGroupStructure()

    # create blendshape mesh first
    blendshapeTargetMesh = originalMesh+"_JiggleBlendshape"

    # define blendshape target name, same name?
    blendshapeTarget = originalMesh+"_JiggleBlendshape"

    if not cmds.objExists(blendshapeTargetMesh):
        blendshapeTargetMesh = cmds.duplicate(originalMesh, name=blendshapeTargetMesh)[0]
        cmds.parent(blendshapeTargetMesh, "JiggleSetup")
        cmds.hide(blendshapeTargetMesh)

    # if there is user define blendshape node:
    ## find out if it has blendshape target yet
    ### if yes, find out if it has the matching blendshape target
    #### if matching, the matched target is the blendshape target
    #### if not matching, create a new blendshape target
    if mainBlendshape:
        createBlendshapeTarget(mainBlendshape)
    
    # if there is no user define blendshape node:
    ## find out if blendshape node(s) exist:
    ### if exist
    #### find under the blendshape node with the biggest weight count (the most used blendshape), if it has the matching blendshape target
    ##### if not matched: add new blendshape target to this (most used) blendshape
    ##### if matching: the existing target is the blendshape Target
    else:    
        my_history = cmds.listHistory(originalMesh)
        my_blendShape_nodes = cmds.ls(my_history, type='blendShape')
        print(my_blendShape_nodes)

        if my_blendShape_nodes:
            maxWeightCount = 0
            for blendshape in my_blendShape_nodes:
                print(blendshape)
                weightCount = cmds.blendShape(blendshape, q=True, wc=True)
                if weightCount >= maxWeightCount:
                    maxWeightCount = weightCount
                    mainBlendshape = blendshape
                    print("max weight count is "+str(maxWeightCount))
                    
            createBlendshapeTarget(mainBlendshape)
        ## if none blendshape nodes exist, 
        ### create new blendshape, then create a new blendshape target
        else:
            # create a new blendshape node
            bs = cmds.blendShape(blendshapeTarget, originalMesh, frontOfChain=1, topologyCheck=1, name="JiggleBlendshape")[0]
            # then create a new blendshape target, blendshape always on
            cmds.setAttr(bs+"."+blendshapeTarget, 1)

'''
def createBlendshapeTarget():
    global bsStage
    global mainBlendshape
    print(mainBlendshape)
    if mainBlendshape and not blendshapeTarget:
        bsStage = 1
    elif mainBlendshape and blendshapeTarget:
        bsStage = 2
    else:
        defineExistingBlendshape()

    # duplicate original mesh >> blendshape mesh. If blendshape mesh already exists, ignore.
    global blendshapeTarget
    global originalMesh

    if originalMesh:
        blendshapeTarget = originalMesh + "_JiggleBlendshape"

        createJiggleGroupStructure()

        # create blendshape mesh first
        if not cmds.objExists(blendshapeTarget):
            blendshapeTarget = cmds.duplicate(originalMesh, name=blendshapeTarget)[0]
            cmds.parent(blendshapeTarget, "JiggleSetup")
            # All blendshape node & target related to "Jiggle" should be deleted clean
            try:
                # delete Jiggle Blendshape node
                cmds.delete("JiggleBlendshape")
            except:
                print("No existing jiggle blendshape node")
            if bsStage == 2:
                # delete target named blendshapeTarget
                delBlendshapeTarget(blendshapeTarget)

        if bsStage == 0:
            # create a blendshape node
            bs = cmds.blendShape(blendshapeTarget, originalMesh, frontOfChain=1, topologyCheck=1, name="JiggleBlendshape")[0]
            # blendshape always on
            cmds.setAttr(bs+"."+blendshapeTarget, 1)
            bsStage = 2 # do nothing

        elif bsStage == 1:
            # create a target to existing blendshape
            weightCount = cmds.blendShape(mainBlendshape, q=True, wc=True)
            cmds.blendShape(mainBlendshape, e=1, target=(originalMesh, weightCount + 1, blendshapeTarget, 1.0))
            cmds.blendShape(mainBlendshape, e=1, weight=[weightCount + 1, 1.0])

        elif bsStage == 2:
            # do nothing
            pass
        cmds.hide(blendshapeTarget)
        return blendshapeTarget
'''


# do this before delete the blendshapeTarget
def delBlendshapeTarget(name):
    cmds.select(clear=1)
    my_history = cmds.listHistory(originalMesh)
    my_blendShape_nodes = cmds.ls(my_history, type='blendShape')
    print(my_blendShape_nodes)

    for blendShapeNode in my_blendShape_nodes:
        print(blendShapeNode)
        blendTargets = cmds.listAttr(blendShapeNode + '.w', m = True)
        print(blendTargets)
        for i in range(len(blendTargets)):
            if blendTargets[i] == name:
                print(i)
                print(blendTargets[i])
                try:
                    cmds.blendShape(blendShapeNode, edit=True, remove=True, t=(originalMesh, i, blendTargets[i], 1.0))
                    # cmds.removeMultiInstance(blendShapeNode + ".weight[%s]" % i, b=True)
                    # cmds.removeMultiInstance(blendShapeNode + ".inputTarget[0].inputTargetGroup[%s]" % i, b=True)
                except:
                    print("Target cannot be deleted. Blendshape mesh need to be present.")


def getSkinCluster(mesh):
    skinClusters = [
        h
        for h in cmds.listHistory(mesh) or []
        if cmds.nodeType(h) == "skinCluster"
    ]

    if skinClusters:
        return skinClusters[0]
    else:
        raise Exception("Mesh has no Skin Cluster")

# duplicate original mesh >> follicle mesh. If follicle mesh already exists, ignore.
def createFollicleMesh():
    global originalMesh
    global follicleMesh
    if not cmds.objExists(originalMesh + "_JiggleFollicle"):
        # duplicate the selected mesh into follicleMesh
        follicleMesh = cmds.duplicate(originalMesh, rr=True, name=originalMesh + "_JiggleFollicle")[0]
        print(follicleMesh)

        # delete history/ skin cluster
        cmds.delete(follicleMesh, ch=1)

        originalMeshSC = getSkinCluster(originalMesh)

        # get deform joints of the selected mesh
        deformJntsAll = cmds.skinCluster(originalMeshSC, inf=True, q=True)
        print(deformJntsAll)

        deformJnts = []
        # filter out what is not joint
        for item in deformJntsAll:
            if cmds.nodeType(item) == 'joint':
                deformJnts.append(item)

        if deformJnts:
            # skin the deform jnts to the follicle mesh, classical linear skinning, to selected bones only
            dupSC = cmds.skinCluster(deformJnts, follicleMesh, sm=0, tsb=True)[0]
            print(dupSC)

            # find skinCluster in the original mesh
            meshSkin = mel.eval('findRelatedSkinCluster ' + originalMesh)

            # copy skin from original mesh to follicle mesh
            cmds.copySkinWeights(ss=meshSkin, ds=dupSC, nm=True, surfaceAssociation='closestPoint')
            cmds.select(clear=True)

            cmds.parent(follicleMesh, "JiggleSetup")
        else:
            print("cannot find deform joints")
    else:
        print("follicle mesh already exists")
        follicleMesh = originalMesh + "_JiggleFollicle"

        # find skinCluster in the original mesh (it might changed, so we need to copy skin again)
        meshSkin = mel.eval('findRelatedSkinCluster ' + originalMesh)

        # find skinCluster in the follicle mesh
        folSkin = mel.eval('findRelatedSkinCluster ' + follicleMesh)

        # copy skin from original mesh to follicle mesh
        cmds.copySkinWeights(ss=meshSkin, ds=folSkin, nm=True, surfaceAssociation='closestPoint')
        cmds.select(clear=True)

    cmds.hide(follicleMesh)
    return follicleMesh

def getBBoxSize():
    global originalMesh
    global jiggleConRadius
    # use model size for control size
    shape = cmds.listRelatives(originalMesh, s=True)[0]
    print(shape)
    maxBBoxY = cmds.getAttr(shape + ".boundingBoxMax")[0][1]
    print(maxBBoxY)
    minBBoxY = cmds.getAttr(shape+".boundingBoxMin")[0][1]
    print(minBBoxY)
    size = maxBBoxY - minBBoxY
    print(size)
    jiggleConRadius = size/50 # maybe 1/50 character's height is control size
    print(jiggleConRadius)
    return jiggleConRadius

def getVertexNormal(ver):
    list = cmds.polyNormalPerVertex(ver, q=1, xyz=1)
    s = len(list) / 3
    result = [0, 0, 0]
    while len(list):
        result = [result[0] + list.pop(0), result[1] + list.pop(0), result[2] + list.pop(0)]
    result = [result[0] / s, result[1] / s, result[2] / s]
    # angle between locator & vertex normal
    rotationResult = cmds.angleBetween(v1=(0.0, 1.0, 0.0), v2=result, euler=1)
    return rotationResult

def snapVertex(jiggleOffsetGrp, ver):
    verPos = cmds.xform(ver, q=1, translation=1, ws=1)
    cmds.xform(jiggleOffsetGrp, translation=verPos)
    verRot = getVertexNormal(ver)
    cmds.xform(jiggleOffsetGrp, rotation=verRot, euler=1)

def getVerNum(verName):
    # get vertice number. For example: body_m.vtx[3326] >> 3326
    num_and_bracket = verName.split("[")[1]
    num = num_and_bracket.split("]")[0]
    print(num)
    return num

def yellowcon(s):
    # make control yellow color
    cmds.setAttr(s+'.overrideEnabled', 1)
    cmds.setAttr(s+'.overrideColor', 17)

# look like I didn't use this one
def alignTransform(base, target):
    cmds.delete(cmds.parentConstraint(base, target))

def findOriginalMeshSkin():
    global originalMesh
    global oriMeshSkin
    oriMeshSkin = mel.eval('findRelatedSkinCluster ' + originalMesh)
    print(oriMeshSkin)
    if not oriMeshSkin:
        raise Exception("Original mesh skinCluster is not found, you must create skinCluster for selected mesh first")
    return oriMeshSkin

def renameFollicleVertex(ver):
    global originalMesh
    global follicleMesh
    folVer = ver.replace(originalMesh, follicleMesh)
    print(folVer)
    return folVer

def createFollicle(folVer, follicleMesh):
    geo = pm.PyNode(follicleMesh)
    uvMap = pm.polyListComponentConversion(folVer, fv=True, tuv=True)
    uvCoord = pm.polyEditUV(uvMap, q=True)

    folName = "follicle_"+getVerNum(folVer)

    fol = pm.createNode('transform', ss=True, name=folName)
    folShape = pm.createNode('follicle', n=fol.name() + 'Shape', p=fol, ss=True)
    print(fol)
    print(folShape)
    pm.setAttr(folShape+".visibility", 0)
    # parent follicle under JiggleSetup >> FollicleGrp
    pm.parent(fol, "FollicleGrp")

    pm.connectAttr(geo + '.outMesh', folShape + '.inputMesh')
    pm.connectAttr(geo + '.worldMatrix[0]', folShape + '.inputWorldMatrix')
    pm.connectAttr(folShape + '.outRotate', fol + '.rotate')
    pm.connectAttr(folShape + '.outTranslate', fol + '.translate')
    fol.inheritsTransform.set(False)
    folShape.parameterU.set(uvCoord[0])
    folShape.parameterV.set(uvCoord[1])
    return str(fol)

def buildJointStructure(jiggle_name, ver, position):
    global jiggleJntList

    cmds.select(clear=1)
    # check duplicate name
    if cmds.objExists(jiggle_name + "_jiggle_jnt"+position):
        cmds.error( "Duplicated Names, please rename the input name" )

    jiggle_joint = cmds.joint(name=jiggle_name + "_jiggle_jnt"+position)

    jiggleJntList.append(jiggle_joint)
    print("This is joint list")
    print(jiggleJntList)

    cmds.select(jiggle_joint, replace=1)
    jiggle_joint_offset_grp = cmds.group(jiggle_joint, name=jiggle_name + "_jiggle_jnt_offset"+position)

    jiggle_control = cmds.circle(name=jiggle_name + "_jiggle_con"+position, normal=[0,1,0], radius=jiggleConRadius)[0]
    yellowcon(jiggle_control)
    cmds.parent(jiggle_joint_offset_grp, jiggle_control)

    jiggle_con_offset_grp = cmds.group(jiggle_control, name=jiggle_name + "_jiggle_con_offset"+position)

    snapVertex(jiggle_con_offset_grp, ver)
    # parent offset_grp under JiggleControlsGrp. JiggleSetup >> JiggleControlsGrp
    # after having the correct postion, parent _jiggle_jnt_offset under JiggleJointsGrp
    if position == "_M":
        cmds.parent(jiggle_joint_offset_grp, "JiggleJointsMiddle")
        cmds.parent(jiggle_con_offset_grp, "JiggleControlMiddle")
    elif position == "_L":
        cmds.parent(jiggle_joint_offset_grp, "JiggleJointsLeft")
        cmds.parent(jiggle_con_offset_grp, "JiggleControlLeft")
    elif position == "_R":
        cmds.parent(jiggle_joint_offset_grp, "JiggleJointsRight")
        cmds.parent(jiggle_con_offset_grp, "JiggleControlRight")

    # Connect all channel of jiggle joint to jiggle control
    cmds.connectAttr(jiggle_control + ".translate", jiggle_joint + ".translate")
    cmds.connectAttr(jiggle_control + ".rotate", jiggle_joint + ".rotate")
    cmds.connectAttr(jiggle_control + ".scale", jiggle_joint + ".scale")

    # Scale constraint jiggle offset group to Main control
    cmds.scaleConstraint(mainControl, jiggle_con_offset_grp, maintainOffset=1)
    # change vertex name from vertex on original mesh to vertex on follicle mesh
    folVer = renameFollicleVertex(ver)
    # create follicle from selected vertex on FOLLICLE mesh.
    folliceNode = createFollicle(folVer, follicleMesh)
    # parent constraint jiggle joints offset groups to these follicles: follicle >> jiggle joint offset grp >> control >> jiggle joint
    cmds.parentConstraint(folliceNode, jiggle_con_offset_grp, maintainOffset=1)

def userDefinedControlName():
    global controlName
    global controlName_tf
    controlName = cmds.textFieldGrp(controlName_tf, q=1, text=1)
    print(controlName)

def jiggleSetupProcess(position, verList):
    global jiggleJntList
    global blendshapeTarget
    global controlName
    # run to check control name
    userDefinedControlName()

    # clear joint list very time rebuild
    jiggleJntList=[]
    for ver in verList:
        # create joint based on ver name and postion
        if not controlName:
            jiggle_name = "jg"+getVerNum(ver)
        else:
            jiggle_name = controlName
        print(jiggle_name)
        buildJointStructure(jiggle_name, ver, position)

    # skin base joint & jiggle joints to blendshape mesh. Do this afterward, after all joints are created
    # need to check blendshape mesh already has skincluster or not
    bsMeshSkin = mel.eval('findRelatedSkinCluster ' + blendshapeTarget)
    if not bsMeshSkin:
        jiggleJntList.append("base_jiggle_jnt")
        folSC = cmds.skinCluster(jiggleJntList, blendshapeTarget, sm=0, tsb=True)[0]
    else:
        try:
            # If blendshape mesh already has skincluster, add influence for jiggle joints instead (skip base joint).
            folSC = cmds.skinCluster(bsMeshSkin, e=1, useGeometry=0, lockWeights=1, weight=0, addInfluence=jiggleJntList)
        except:
            print("Current joints are already added")
    # clear selection
    cmds.select(clear=1)

def generateMiddleJiggleSetup():
    # with middle vertices, simply build verList from current selection
    verList = cmds.ls(sl=1, flatten=1)

    findOriginalMeshSkin()
    createJiggleGroupStructure()
    checkAndCreateBST()
    createFollicleMesh()
    getBBoxSize()

    jiggleSetupProcess("_M", verList)


def findOppositeVer(ver):
    global rightVerList
    global leftVerList
    global originalMesh

    pos = cmds.xform(ver, q=1, ws=1, t=1)
    print(pos)

    oppositePos = [-pos[0], pos[1], pos[2]]
    print(oppositePos)
    cpom = cmds.createNode('closestPointOnMesh')
    shape = cmds.listRelatives(originalMesh, s=True)[0]
    cmds.connectAttr('%s.outMesh' % shape, '%s.inMesh' % cpom)
    cmds.setAttr('%s.inPosition' % cpom, oppositePos[0], oppositePos[1], oppositePos[2], type="double3")

    # vertex index
    vtxIndx = cmds.getAttr(cpom + ".closestVertexIndex")
    print(vtxIndx)
    oppositeVer = "{0}.vtx[{1}]".format(originalMesh, vtxIndx)
    print(oppositeVer)

    if pos[0] < 0:
        rightVerList.append(ver)
        leftVerList.append(oppositeVer)
        print(rightVerList)
        print(leftVerList)
    elif pos[0] > 0:
        leftVerList.append(ver)
        rightVerList.append(oppositeVer)
        print(rightVerList)
        print(leftVerList)
    else:
        raise Exception("Selected vertex is in the middle!")

    # delete node when done calculating
    cmds.delete(cpom)

    return rightVerList, leftVerList


def generateSideJiggleSetup():
    global rightVerList
    global leftVerList
    rightVerList=[]
    leftVerList=[]
    verList = cmds.ls(sl=1, flatten=1)
    for ver in verList:
        print(ver)
        findOppositeVer(ver)

    findOriginalMeshSkin()
    createJiggleGroupStructure()
    checkAndCreateBST()
    createFollicleMesh()
    getBBoxSize()

    # create list of vertices on Right side >> generate jiggle setup
    jiggleSetupProcess("_R", rightVerList)
    # create list of vertices on Left side >> generate jiggle settup
    jiggleSetupProcess("_L", leftVerList)
    # issue: cannot mirror skin weight in ngskin due to different joint name from side to side
    # current solution: use Edit influence associations in ngskin for this. Or use Closest joint & one to one in Mirror skin

    # issue 2: orientation of controls from 2 sides are not working well together

# paint button for paint skin weight on blendshape mesh, show joints & jiggle blendshape mesh, hide original mesh + isolate. Then paint.
# should work when loading bodyMesh in case close and open the tool again.
def showForPaintingSkinWeight():
    global blendshapeTarget

    cmds.hide(originalMesh)
    cmds.showHidden(blendshapeTarget)
    cmds.showHidden("JiggleJointsGrp")
    # isolate Jiggle Joints Grp and Blendshape Mesh
    # make sure to click/ be active at viewport window (perspective camera)
    # query current camera
    panelList = cmds.getPanel(type='modelPanel')
    panel = cmds.getPanel(wf=True)
    print(panel)

    if panel not in panelList:
        raise Exception("The current panel is not viewport")

    # select Jiggle Joints Grp and Blendshape Mesh
    cmds.select("JiggleJointsGrp", blendshapeTarget, "JiggleControlGrp", replace=1)
    isoCrnt = cmds.isolateSelect(panel, q=True, s=True)
    mel.eval('enableIsolateSelect %s %d' % (panel, not isoCrnt))
    cmds.select(blendshapeTarget, replace=1)

# done button for hide them all again
def hideAfterPainting():
    cmds.showHidden(originalMesh)
    cmds.hide(blendshapeTarget)
    cmds.hide("JiggleJointsGrp")
    panelList = cmds.getPanel(type='modelPanel')
    panel = cmds.getPanel(wf=True)
    print(panel)
    if panel not in panelList:
        raise Exception("The current panel is not viewport")
    cmds.isolateSelect(panel, state=0)
    cmds.select(clear=1)

# Delete selected jiggle: delete jiggle group, delete joint "jiggle_".
# Be careful, skin weight will be messed up.
def deleteSelectedJiggleSetup():
    # select jiggle control
    jiggleControlList = cmds.ls(sl=1)
    print(jiggleControlList)
    for con in jiggleControlList:
        rawName = con.split("_con")[0]
        side = con.split("_con")[1]
        print(rawName)
        cmds.delete(rawName+"_con_offset"+side)
        cmds.delete(rawName+"_jnt_offset"+side)

# Delete entire setup:  delete blendshape target or delete blendshape, delete JiggleSetup.
def deleteJiggleSetup():
    if cmds.objExists("JiggleBlendshape"):
        print("JiggleBlendshape exists")
        cmds.delete("JiggleBlendshape")
    try:
        delBlendshapeTarget(blendshapeTarget)
    except:
        print("No target matched name to be deleted")
    if cmds.objExists("JiggleSetup"):
        cmds.delete("JiggleSetup")

def load_selected_as(sel, text_field):
    strTF = ''.join(sel)
    text_field = cmds.textField(text_field, e=True, tx=strTF)

def show_UI(winID):
    if cmds.window(winID, exists=True):
        cmds.deleteUI(winID)
    cmds.window(winID)
    create_UI(winID)
    cmds.showWindow(winID)

def userDefinedBlendshape():
    global mainBlendshape
    global mainBlendshape_tf
    mainBlendshape = cmds.ls(sl=True)[0]
    if not mainBlendshape:
        raise Exception("Please right click the blendshape, hit Select, then hit >>")
    load_selected_as(mainBlendshape, mainBlendshape_tf)
    print(mainBlendshape)

def setOriginalMesh():
    global originalMesh
    originalMesh = cmds.ls(sl=True)[0]
    if not originalMesh:
        raise Exception("Please select the main character body")
    if ":" in originalMesh:
        raise Exception("namespace exists in your model, please (import reference then) delete namespace")
    load_selected_as(originalMesh, originalMesh_tf)
    print(originalMesh)

def setMainRigControl():
    global mainControl
    mainControl = cmds.ls(sl=True)[0]
    if not mainControl:
        raise Exception("Please select the main rig control")
    load_selected_as(mainControl, mainControl_tf)
    print(mainControl)

def create_UI(winID):
    global controlName_tf
    window_size = (300, 470)
    cmds.window(winID, e=True, wh=window_size, title="Jiggle Controls Generator by Truong")

    txt_field_width = 269

    main_lo = cmds.columnLayout(p=winID)

    cmds.text("\n Select Mesh (must have skin cluster): ", p=main_lo)
    set_original_mesh_lo = cmds.rowLayout(p=main_lo, nc=2, cw2=(txt_field_width, 25))
    cmds.textField(originalMesh_tf, w=txt_field_width, ed=False)
    set_original_mesh_btn = cmds.button(label=">>", p=set_original_mesh_lo, c='setOriginalMesh()', width=25)

    cmds.text("\n Select Main Rig Control (for scale constraint): ", p=main_lo)
    set_main_rig_lo = cmds.rowLayout(p=main_lo, nc=2, cw2=(txt_field_width, 25))
    cmds.textField(mainControl_tf, w=txt_field_width, ed=False)
    set_main_control_btn = cmds.button(label=">>", p=set_main_rig_lo, c='setMainRigControl()', width=25)

    cmds.text("\n User defined blendshape (optional): ", p=main_lo)
    set_bs_lo = cmds.rowLayout(p=main_lo, nc=2, cw2=(txt_field_width, 25))
    cmds.textField(mainBlendshape_tf, w=txt_field_width, ed=False)
    set_bs_btn = cmds.button(label=">>", p=set_bs_lo, c='userDefinedBlendshape()', width=25)

    cmds.text("\n Name of the control? optional, plz rename each time", p=main_lo)
    set_cn_lo = cmds.rowLayout(p=main_lo, nc=2, cw2=(txt_field_width, 25))
    controlName_tf = cmds.textFieldGrp(w=txt_field_width, ed=True)

    sep1 = cmds.separator(w=window_size[0], h=10, p=main_lo)

    cmds.text("\n Select vertex(s), then: ", p=main_lo)
    generate_jiggle_lo = cmds.rowLayout(p=main_lo, nc=2)
    middle_jiggle_btn = cmds.button(label="Create Middle Jiggle", p=generate_jiggle_lo, c='generateMiddleJiggleSetup()', width=147, align="center")
    side_jiggle_btn = cmds.button(label="Create Mirror Jiggle", p=generate_jiggle_lo, c='generateSideJiggleSetup()', width=147, align="center")

    sep2 = cmds.separator(w=window_size[0], h=10, p=main_lo)
    cmds.text("\n Paint Skin weight on Blendshape mesh: ", p=main_lo)
    pain_skin_lo = cmds.rowLayout(p=main_lo, nc=2)
    show_btn = cmds.button(label="Show Jiggle Blendshape", p=pain_skin_lo, c='showForPaintingSkinWeight()', width=147, align="center")
    hide_btn = cmds.button(label="Hide Jiggle Blendshape", p=pain_skin_lo, c='hideAfterPainting()', width=147, align="center")

    sep3 = cmds.separator(w=window_size[0], h=10, p=main_lo)
    cmds.text("\n Delete setup: ", p=main_lo)
    delete_lo = cmds.rowLayout(p=main_lo, nc=2)
    del_sel_btn = cmds.button(label="Delete Selected Control", p=delete_lo, c='deleteSelectedJiggleSetup()', width=147, align="center")
    del_all_btn = cmds.button(label="Delete All Jiggle Setup", p=delete_lo, c='deleteJiggleSetup()', width=147, align="center")


show_UI(win_ID)