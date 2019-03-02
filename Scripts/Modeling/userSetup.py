import maya.cmds as cmds
import maya.mel 
import maya.utils as mu

def autoSave(*args):
	maya.mel.eval('NPautoSaveOptions')

def writeFolderFiles(*args):
	maya.mel.eval('writeFolderFiles')	

def openURLforAssetSignOff(*args):
	maya.mel.eval('openURLforAssetSignOff')

def fileNodeUpdate2009(*args):
	maya.mel.eval('fileNodeUpdate2009')

def findPolySurfaces(*args):
	maya.mel.eval('findPolySurfaces')

def reportDuplicateNodes(*args):
	maya.mel.eval('reportDuplicateNodes')

def changeToLambert(*args):
	maya.mel.eval('changeToLambert')

def refreshTextureNodes(*args):
	maya.mel.eval('refreshTextureNodes')

def FileTextureManager(*args):
	maya.mel.eval('FileTextureManager')

def assetMan(*args):
	maya.mel.eval('assetMan')

def abSymMesh(*args):
	maya.mel.eval('abSymMesh')

def riessImf_copyGUI(*args):
	maya.mel.eval('riessImf_copyGUI')

def hrTextureLoader(*args):
	maya.mel.eval('hrTextureLoader')

def exportMiProxy(*args):
	maya.mel.eval('exportMiProxy')

def freezeReferenceNormal(*args):
	maya.mel.eval('freezeReferenceNormal')

def deleteSmoothNode(*args):
	maya.mel.eval('deleteSmoothNode')

def assetCleanerMod(*args):
	maya.mel.eval('assetCleanerMod')

def modelingMenu():
	gMainWindow=maya.mel.eval('string $temp=$gMainWindow')
	showMyMenu=cmds.menu(parent=gMainWindow,tearOff=True,label='Studio56 Modeling')
	cmds.menuItem(label = 'Auto Save',command=('autoSave()'))
	cmds.menuItem(label = 'Write Folder Contents',command=('writeFolderFiles()'))
	cmds.menuItem(label = 'Artist(s) SignOff',command=('openURLforAssetSignOff()'))
	cmds.menuItem(divider=True)
	cmds.menuItem(label = '2009 FileNode Update',command=('fileNodeUpdate2009()'))
	cmds.menuItem(label = 'Find Poly Surfaces',command=('findPolySurfaces()'))
	cmds.menuItem(label = 'Report Duplicates',command=('reportDuplicateNodes()'))
	cmds.menuItem(label = 'Change To Lambert',command=('changeToLambert()'))
	cmds.menuItem(divider=True)
	cmds.menuItem(label = 'Refresh TextureNodes',command=('refreshTextureNodes()'))
	cmds.menuItem(label = 'Copy Mesh Attributes')
	cmds.menuItem(label = 'File TextureManager',command=('FileTextureManager()'))
	cmds.menuItem(divider=True)
	cmds.menuItem(label = 'Asset Manager',command=('assetMan()'))
	cmds.menuItem(label = 'AB SymMesh',command=('abSymMesh()'))
	cmds.menuItem(label = '.map Convertion',command=('riessImf_copyGUI()'))
	cmds.menuItem(label = 'HighRes Texture Loader',command=('hrTextureLoader()'))
	cmds.menuItem(label = 'Mentalray Proxy Export',command=('exportMiProxy()'))
	cmds.menuItem(divider=True)
	cmds.menuItem(label = 'Make Scene Template',command=('freezeReferenceNormal()'))
	cmds.menuItem(label = 'Delete SmoothNodes',command=('deleteSmoothNode()'))
	cmds.menuItem(label = 'File Cleaner',command=('assetCleanerMod()'))

mu.executeDeferred('modelingMenu()')

