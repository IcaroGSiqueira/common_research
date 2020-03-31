import os

threads = 4 # numero de processos em parelelo

gitpull = 1

server = 0 # local = 0 ; servidor = 1

confs = ["encoder_randomaccess_main.cfg","encoder_lowdelay_main.cfg","encoder_intra_main.cfg"]

conf = "encoder_randomaccess_main.cfg"

#[37,32,27,22]

qps = [22,27,32,37]

gitpath = "pesquisa_ucpel"
gitscript = "git_upl"

shpath = "pesquisa_ucpel/codes/run-sh/hm"
filename = "run_hm.sh"

if server == 1:	
	homepath = "/home/grellert"
	yuvpath = "/videos"
	outpath = "pesquisa_ucpel/output_HM/server"
	binpath = "hm/bin" #partindo da homepath
	confpath = "hm/cfg"
else:
	homepath = "/home/icaro"
	yuvpath = "/home/icaro/origCfP"
	outpath = "pesquisa_ucpel/output_HM/local"
	binpath = "hm/bin" #partindo da homepath
	confpath = "hm/cfg"
	
if gprof == 0:
	bina = "TAppEncoderStatic"
	inf = ""
else:
	bina = "TAppEncoderStaticd"
	inf = "gprof"

file = open("%s/%s/%s"%(homepath,shpath,filename),"w")

i=0
if threads != 1:

	file = open("%s/%s/%s"%(homepath,shpath,filename),"r")
	lines = file.readlines()
	tam = len(lines)
	nqp = len(qps)
	nconf = len(confs)

	for x in range(threads):

		file2 = open("%s/%s/%d_%s"%(homepath,shpath,x+1,filename),"w")
		j=0


		while i < tam:

			line = lines[i]
			print >> file2, line
			i=i+1
			j=j+1
			if j >= (tam/threads):
				break

		if gitpull == 1:
			linhag = "cd %s/%s && sh %s.sh || true"%(homepath,gitpath,gitscript)
			print >> file2, linhag
	file2.close
file.close