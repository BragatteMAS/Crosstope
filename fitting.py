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
os.chdir("/home/bragatte/Documentos/Fitting")
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
			
#Script para colocar o pMHC na posição padrão do banco de dados CrossTope.
#Toda vez que for rodar o script precisa criar uma pasta com:
	#script propriamente dito "fitting.py"
	#arquivo.txt para ser o molde da posição (coordenadas previamente definidas = "D2V-NS4a140_148"
	#.pdb que queres colocar na posição esperada, podem ser colocados vários...revisar se foi para posição correta.
#No script precisa ser modificada a linha 13, alterando para o nome da pasta que estiver os arquivos.
# Linha de comando para rodar: python fitting.py
