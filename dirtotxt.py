import os

def ListFilesToTxt(dir,file,end):
	files = os.listdir(dir)
	for name in files:
		if name.endswith(end):
			pid = int(os.path.basename(name)[:3])

			file.write(os.path.basename(dir)+'/'+name+' '+str(pid)+"\n")
                  

def Test():
	dir=[]
	dir.append("/home/lw/dgd_person_reid_old/reiddata2/P2/cam1")
	dir.append("/home/lw/dgd_person_reid_old/reiddata2/P2/cam2")
	outfile=[]
	outfile.append("/home/lw/dgd_person_reid_old/reiddata2/P2/P2_gallery.txt")
	outfile.append("/home/lw/dgd_person_reid_old/reiddata2/P2/P2_probe.txt")
	for i in range(2):
	  files = open(outfile[i],"w+")
	  end=".png"
	  ListFilesToTxt(dir[i],files,end)
	  files.close()

Test()

