import maya.cmds as cmds
import maya.mel 
import maya.utils as mu

def autoSave(*args):
	maya.mel.eval('NPautoSaveOptions')

def writeFolderFiles(*args):
	maya.mel.eval('writeFolderFiles')	

def importFromRef(*args):
	maya.mel.eval('importFromRef')

def mrMemoryHeap(*args):
	maya.mel.eval('mrMemoryHeap')

def KBI_Materials_Attributes_Transfer(*args):
	maya.mel.eval('KBI_Materials_Attributes_Transfer')

def lightingTools(*args):
	maya.mel.eval('lightingTools')

def hrTextureLoader(*args):
	maya.mel.eval('hrTextureLoader')

def hrTextureAssigner(*args):
	maya.mel.eval('hrTextureAssigner')

def RenameShader(*args):
	maya.mel.eval('RenameShader')

def rimLightImport(*args):
	maya.mel.eval('rimLightImport')

def freezeReferenceNormal(*args):
	maya.mel.eval('freezeReferenceNormal')

def EFA(*args):
	maya.mel.eval('EFA')

def deleteEmptyUVSets(*args):
	maya.mel.eval('deleteEmptyUVSets')

def FileTextureManager(*args):
	maya.mel.eval('FileTextureManager')

def riessImf_copyGUI(*args):
	maya.mel.eval('riessImf_copyGUI')

def removeSetup(*args):
	maya.mel.eval('removeSetup')

def assetCleanerLit(*args):
	maya.mel.eval('assetCleanerLit')

def lightingMenu():
	gMainWindow=maya.mel.eval('string $temp=$gMainWindow')
	showMyMenu=cmds.menu(parent=gMainWindow,tearOff=True,label='Studio56 Lighting')
	cmds.menuItem(label = 'Auto Save',command=('autoSave()'))
	cmds.menuItem(label = 'Write Folder Contents',command=('writeFolderFiles()'))
	cmds.menuItem(label = 'Import Objects from Ref',command=('importFromRef()'))
	cmds.menuItem(label = 'Fix Mr MemoryHeap Size',command=('mrMemoryHeap()'))
	cmds.menuItem(divider=True)
	cmds.menuItem(label = 'KBI_Material Attribute Transfer',command=('KBI_Materials_Attributes_Transfer()'))
	cmds.menuItem(label = 'Lighting Tools',command=('lightingTools()'))
	cmds.menuItem(label = 'HighRes Texture Loader',command=('hrTextureLoader()'))
	cmds.menuItem(label = 'HighRes Texture Assigner',command=('hrTextureAssigner()'))
	cmds.menuItem(divider=True)
	cmds.menuItem(label = 'Render Passes',command='renderPassesWin()')
	cmds.menuItem(label = 'Rename Shader',command=('RenameShader()'))
	cmds.menuItem(label = 'Rim Light',command=('rimLightImport()'))
	cmds.menuItem(divider=True)
	cmds.menuItem(label = 'Make Scene Template',command=('freezeReferenceNormal()'))
	cmds.menuItem(label = 'EFA',command=('EFA()'))
	cmds.menuItem(label = 'Empty UV Sets',command=('deleteEmptyUVSets()'))
	cmds.menuItem(label = 'File TextureManager',command=('FileTextureManager()'))
	cmds.menuItem(divider=True)
	cmds.menuItem(label = '.map Conversion',command=('riessImf_copyGUI()'))
	cmds.menuItem(label = 'Remove Setup',command=('removeSetup()'))
	cmds.menuItem(label = 'File Cleaner',command=('assetCleanerLit()'))
mu.executeDeferred('lightingMenu()')

maya.mel.eval('optionVar -sv workingUnitTimeDefault pal')
maya.mel.eval('currentUnit -t pal')

maya.mel.eval('welcomeWindow()')
maya.mel.eval('loadCustomPlugins()')
maya.mel.eval('addSetup()')

maya.mel.eval('anzUI_setupAtLaunch()');
maya.mel.eval('ui_global()')
maya.mel.eval('ui_anzovin()')
maya.mel.eval('ui_poses()')
maya.mel.eval('anzUI_initialize()')



