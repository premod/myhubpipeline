import maya.cmds as cmds
def readLines():
	fol = cmds.getFileList( folder='D:/Files/TEST/' )
	for each in fol:
		name = cmds.getFileList(folder= ('D:/Files/TEST/'+each+'/'),fs='*.ma'  )
		for a in name:
			path = ('D:/Files/TEST/'+each+'/'+a)
			f = open(path,'w')
			f.write('//Maya ASCII 2009 scene')
			f.write('\nrequires maya "2009";')
			f.write('\ncurrentUnit -l centimeter -a degree -t pal;')
			f.close()
readLines()
