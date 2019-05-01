import maya.cmds as cmds
import maya.mel 
import maya.utils as mu

def autoSave(*args):
	maya.mel.eval('NPautoSaveOptions')

def writeFolderFiles(*args):
	maya.mel.eval('writeFolderFiles')	

def openURLforAssetSignOff(*args):
	maya.mel.eval('openURLforAssetSignOff')

def openURLforLeadSignOff(*args):
	maya.mel.eval('openURLforLeadSignOff')

def rcPowerSearch(*args):
	maya.mel.eval('rcPowerSearch')

def finalizeSceneFile(*args):
	maya.mel.eval('finalizeSceneFile')

def poseManGlobal(*args):
	maya.mel.eval('poseManGlobal')

def findPolySurfaces(*args):
	maya.mel.eval('findPolySurfaces')

def reportDuplicateNodes(*args):
	maya.mel.eval('reportDuplicateNodes')

def asUtilities(*args):
	maya.mel.eval('asUtilities')

def asSelectorbiped(*args):
	maya.mel.eval('asSelectorbiped')

def FileTextureManager(*args):
	maya.mel.eval('FileTextureManager')

def assetMan(*args):
	maya.mel.eval('assetMan')

def abSymMesh(*args):
	maya.mel.eval('abSymMesh')

def rig101wireControllers(*args):
	maya.mel.eval('rig101wireControllers')

def hrTextureLoader(*args):
	maya.mel.eval('hrTextureLoader')

def ktEmbedRotateInfluenceJoints(*args):
	maya.mel.eval('ktEmbedRotateInfluenceJoints')

def freezeReferenceNormal(*args):
	maya.mel.eval('freezeReferenceNormal')

def rivet(*args):
	maya.mel.eval('rivet')

def deleteLocked(*args):
	maya.mel.eval('deleteLocked')

def deleteSelected(*args):
	maya.mel.eval('deleteSelected')

def assetCleanerRig(*args):
	maya.mel.eval('assetCleanerRig')

def userSetup():
	gMainWindow=maya.mel.eval('string $temp=$gMainWindow')
	showMyMenu=cmds.menu(parent=gMainWindow,tearOff=True,label='Rigging_Py')
	cmds.menuItem(label = 'Auto Save',command=('autoSave()'))
	cmds.menuItem(label = 'Write Folder Contents',command=('writeFolderFiles()'))
	cmds.menuItem(label = 'Artist(s) SignOff',command=('openURLforAssetSignOff()'))
	cmds.menuItem(label = 'Lead(s) SignOff',command=('openURLforLeadSignOff()'))
	cmds.menuItem(divider=True)
	cmds.menuItem(label = 'Pose Manager',command=('poseManGlobal()'))
	cmds.menuItem(label = 'Face Generator',command=('asSelectorMachine()'))
	cmds.menuItem(label = 'HighRes Texture Loader',command=('hrTextureLoader()'))
	cmds.menuItem(label = 'Find Poly Surfaces',command=('findPolySurfaces()'))
	cmds.menuItem(label = 'Report Duplicates',command=('reportDuplicateNodes()'))
	cmds.menuItem(label = 'Filalize Rig File',command=('finalizeSceneFile()'))
	cmds.menuItem(divider=True)
	cmds.menuItem(label = 'Asset Search',command=('rcPowerSearch()'))
	cmds.menuItem(label = 'Copy Mesh Attributes')
	cmds.menuItem(label = 'Selector:Utilities',command=('asUtilities()'))
	cmds.menuItem(label = 'Selector: Biped',command=('asSelectorbiped()'))
	cmds.menuItem(label = 'File TextureManager',command=('FileTextureManager()'))
	cmds.menuItem(divider=True)
	cmds.menuItem(label = 'AB SymMesh',command=('abSymMesh()'))
	cmds.menuItem(label = '101 WireControllers',command=('rig101wireControllers()'))
	cmds.menuItem(label = 'Rotate InfluenceJoints',command=('ktEmbedRotateInfluenceJoints()'))
	cmds.menuItem(label = 'Make scene Template',command=('freezeReferenceNormal()'))
	cmds.menuItem(label = 'Rivet Constraint',command=('rivet()'))
	cmds.menuItem(divider=True)
	cmds.menuItem(label = 'Delete Locked',command=('deleteLocked()'))
	cmds.menuItem(label = 'Delete Selected',command=('deleteSelected()'))
	cmds.menuItem(label = 'File Cleaner',command=('assetCleanerRig()'))

mu.executeDeferred('userSetup()')

