import maya.cmds as cmds

def charRenderPasses(*arg):
	maya.mel.eval('charRenderPasses()')

def setRenderPasses(*arg):
	maya.mel.eval('setPassesWin()')

def renderPassesWin(*args):
	if cmds.window ("charPassesWin", exists = 1):
		cmds.deleteUI ("charPassesWin", window=1)
	cmds.window("charPassesWin",t='Render Passes',s=False)
	cmds.columnLayout(adj=True)
	cmds.text(l='Render Passes Window') 
	cmds.text(l='')
	cmds.button(l='Create Character Passes',c='charRenderPasses()')
	cmds.button(l='Create Set Passes',c='setRenderPasses()') 
	cmds.window("charPassesWin",e=True,w=205,h=112)		
	cmds.showWindow()