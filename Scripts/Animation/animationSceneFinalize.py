import maya.cmds as cmds

def sceneClaenUp(*args):
	unKnown=cmds.ls(typ='unknown')

def animationSceneFinalizeWin():
	if cmds.window ("finalizeWin", exists = 1):
		cmds.deleteUI ("finalizeWin", window=1)
	cmds.window("finalizeWin",t='Scene Finalize Window')	
	cmds.columnLayout(adj=True)
	cmds.text (l='Scene Finalization',fn="boldLabelFont")
	cmds.text (l='')
	cmds.button (l='Scene CleanUp', command=sceneClaenUp)
	cmds.button (l='Finalize Scene File', command=finalizeSceneFile)
	cmds.showWindow()

def finalizeSceneFile(*args):
	
	cmds.window(t='Scene Finalization')
	cmds.rowColumnLayout(numberOfColumns=2,columnAttach=(1,"right",0),columnWidth=[(1,105),(2,250)])
	cmds.text(l='')
	cmds.text(l='')
	fileName = cmds.file(q=True,sn=True)
	cmds.text(l='File Name:')
	cmds.textField(fi=fileName)
	cmds.text(l='')
	cmds.text(l='')
	cmds.text(l='Persp Cams:')
	persp = cmds.listCameras( p=True )
	cmds.textScrollList ("pCams",numberOfRows=4)
	for p in (persp):
		cmds.textScrollList ("pCams",edit=True,a=p )

	cmds.text(l='')
	cmds.text(l='')
	cmds.text(l='Ortho Cams:')
	ortho = cmds.listCameras(o=True)
	cmds.textScrollList ("oCams",numberOfRows=4)
	for o in (ortho):
		cmds.textScrollList ("oCams",edit=True,a=o )

	cmds.text(l='')
	cmds.text(l='')
	cmds.text(l='Frame Range:')
	min = cmds.playbackOptions(q=True,min=True)
	max = cmds.playbackOptions(q=True,max=True)
	result = str(min)+" : "+str(max)	
	cmds.textField("fRange",tx=result)
	
	cmds.text(l='')
	cmds.text(l='')
	cmds.text("fps",l='FPS:')
	cmds.textField()

	cmds.text(l='')
	cmds.text(l='')
	cmds.text(l='Device Aspect Ratio:')
	deviceRation = cmds.getAttr('defaultResolution.deviceAspectRatio')
	cmds.textField("dRatio",tx = deviceRation)

	cmds.text(l='')
	cmds.text(l='')
	cmds.text(l='Pixel Aspect Ratio:')
	pixelRation =	cmds.getAttr("defaultResolution.pixelAspect");
	cmds.textField("pRatio",tx=pixelRation)

	cmds.text(l='')
	cmds.text(l='')
	cmds.text(l='Resolution:')
	list = cmds.listConnections("defaultRenderGlobals.resolution")
	width = cmds.getAttr(list[0]+".width");
	height = cmds.getAttr(list[0]+".height")
	result = str(width)+" : "+str(height) 
	cmds.textField(tx=result)

	cmds.text(l='')
	cmds.text(l='')
	cmds.text(l='Ref Loaded:')
	cmds.textScrollList("loadRefs",numberOfRows=6)
	selList = cmds.ls(rf=True);
	currPath = cmds.file(q=True,r=True)
	for i in currPath:
		cmds.textScrollList("loadRefs",edit=True,a=i)
	
	cmds.text(l='')
	cmds.text(l='')
	cmds.text(l='Ref Not Loaded:')
	camName = cmds.textScrollList (numberOfRows=6)
	cmds.showWindow()
animationSceneFinalizeWin()


