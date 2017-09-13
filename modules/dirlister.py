import os 
def run(**args):
	print '[*] in firlist modules'
	files=os.listdir(".")
	return str(files)