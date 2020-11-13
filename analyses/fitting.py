#!/usr/bin/env python
import glob,os,sys,shutil
#import __main__
# pymol environment
moddir='/usr/share/pymol'
sys.path.insert(0, moddir)
os.environ['PYMOL_PATH'] = os.path.join(moddir, '')
# pymol launching
import pymol
pymol.pymol_argv = ['pymol','-qc'] + sys.argv[1:]
pymol.finish_launching()
#def test():
os.chdir("/home/bragatte/Documentos/Fitting") # here edit the path
cmd = pymol.cmd

for file in glob.glob("*.pdb"):
	#print(file)
	#if file.endswith(".pdb"):
	os.rename(file, "alvo.pdb") #ok
	cmd.load ("alvo.pdb")
	cmd.load ("D2V-NS4a140_148.txt")	
	cmd.do ("align alvo, D2V-NS4a140_148")
	#cmd.save ("alvo_fit", "alvo", 0)
	cmd.save ("alvo_fit.pdb", "alvo", -1)
	os.rename("alvo_fit.pdb", file)	
	os.system("rm alvo.pdb")
	cmd.reinitialize()
			
#Script to replace pMHC in the default position of the CrossTope database.
#Every time you run the script you need to create a folder with:
	#script "fitting.py"
	#file ".txt" to be the position template (previously defined coordinates = "D2V-NS4a140_148"
	#.pdb you want to place in the expected position.
	#Multiple pdbs could be replaced at the same run script ... check if it went to the correct position.
#In the script, line 13 MUST be modified, changing to the name of the folder containing the files.
# Command line to run: python fitting.py
