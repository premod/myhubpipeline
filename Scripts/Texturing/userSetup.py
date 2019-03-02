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

def RenameShader(*args):
	maya.mel.eval('RenameShader')

def polyUVMoveComm(*args):
	maya.mel.eval('polyUVMoveComm')

def FileTextureManager(*args):
	maya.mel.eval('FileTextureManager')

def assetMan(*args):
	maya.mel.eval('assetMan')

def KBI_Materials_Attributes_Transfer(*args):
	maya.mel.eval('KBI_Materials_Attributes_Transfer')

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

def assetCleanerTex(*args):
	maya.mel.eval('assetCleanerTex')

def texturingMenu():
	gMainWindow=maya.mel.eval('string $temp=$gMainWindow')
	showMyMenu=cmds.menu(parent=gMainWindow,tearOff=True,label='Studio56 Texturing')
	cmds.menuItem(label = 'Auto Save',command=('autoSave()'))
	cmds.menuItem(label = 'Write Folder Contents',command=('writeFolderFiles()'))
	cmds.menuItem(label = 'Artist(s) SignOff',command=('openURLforAssetSignOff()'))
	cmds.menuItem(divider=True)
	cmds.menuItem(label = '2009 FileNode Update',command=('fileNodeUpdate2009()'))
	cmds.menuItem(label = 'Find Poly Surfaces',command=('findPolySurfaces()'))
	cmds.menuItem(label = 'Report Duplicates',command=('reportDuplicateNodes()'))
	cmds.menuItem(divider=True)
	cmds.menuItem(label = 'Rename Shader',command=('RenameShader()'))
	cmds.menuItem(label = 'Poly ShiftUV',command=('polyUVMoveComm()'))
	cmds.menuItem(label = 'Mentalray Proxy Export',command=('exportMiProxy()'))
	cmds.menuItem(label = 'Material Attribute Transfer',command=('KBI_Materials_Attributes_Transfer()'))
	cmds.menuItem(divider=True)
	cmds.menuItem(label = 'Asset Manager',command=('assetMan()'))
	cmds.menuItem(label = 'AB SymMesh',command=('abSymMesh()'))
	cmds.menuItem(label = 'Copy Mesh Attributes')
	cmds.menuItem(label = '.map Convertion',command=('riessImf_copyGUI()'))
	cmds.menuItem(label = 'Refresh Texture Nodes',command=('refreshTextureNodes()'))
	cmds.menuItem(label = 'File TextureManager',command=('FileTextureManager()'))
	cmds.menuItem(label = 'HighRes Texture Loader',command=('hrTextureLoader()'))
	cmds.menuItem(divider=True)
	cmds.menuItem(label = 'Make Scene Template',command=('freezeReferenceNormal()'))
	cmds.menuItem(label = 'Delete SmoothNodes',command=('deleteSmoothNode()'))
	cmds.menuItem(label = 'File Cleaner',command=('assetCleanerTex()'))

mu.executeDeferred('texturingMenu()')

