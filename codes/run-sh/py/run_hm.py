import os

f=200

clip=0
gprof=0

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

yuvs = ["BlowingBubbles_416x240_50.yuv","BasketballPass_416x240_50.yuv","BQSquare_416x240_60.yuv","RaceHorses_416x240_30.yuv","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","RaceHorses_832x480_30.yuv","PartyScene_832x480_50.yuv","BasketballDrive_1920x1080_50.yuv","Kimono1_1920x1080_24.yuv","ParkScene_1920x1080_24.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","Tennis_1920x1080_24.yuv","SlideEditing_1280x720_30.yuv","FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","PeopleOnStreet_2560x1600_30_crop.yuv","Traffic_2560x1600_30_crop.yuv"] #SERVIDOR

#yuvs = ["BasketballDrill_832x480_50.yuv","BasketballDrive_1920x1080_50.yuv","BasketballPass_416x240_50.yuv","Kimono_1920x1080_24.yuv","BlowingBubbles_416x240_50.yuv","ParkScene_1920x1080_24.yuv","BQMall_832x480_60.yuv","BQSquare_416x240_60.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","PartyScene_832x480_50.yuv","PeopleOnStreet_2560x1600_30_crop.yuv","RaceHorses_832x480_30.yuv","RaceHorses_416x240_30.yuv","Traffic_2560x1600_30_crop.yuv"] #UCPEL_PC

#yuvs = os.listdir("%s"%yuvpath)

if server == 1:	
	homepath = "/home/grellert"
	yuvpath = "/videos"
	outpath = "pesquisa_ucpel/output_HM/server"
	binpath = "hm/bin" #partindo da homepath
	confpath = "hm/cfg"

	#yuvs = ["BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30.yuv","RaceHorses_832x480_30.yuv","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv","FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","SlideEditing_1280x720_30.yuv","Tennis_1920x1080_24.yuv","ParkScene_1920x1080_24.yuv","BasketballDrive_1920x1080_50.yuv","Kimono_1920x1080_24.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","PeopleOnStreet_2560x1600_30_crop.yuv","Traffic_2560x1600_30_crop.yuv"]

else:
	homepath = "/home/icaro"
	yuvpath = "/home/icaro/origCfP"
	outpath = "pesquisa_ucpel/output_HM/local"
	binpath = "hm/bin" #partindo da homepath
	confpath = "hm/cfg"

	#yuvs = ["BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30.yuv","RaceHorses_832x480_30.yuv","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv","ParkScene_1920x1080_24.yuv","BasketballDrive_1920x1080_50.yuv","Kimono_1920x1080_24.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","PeopleOnStreet_2560x1600_30_crop.yuv","Traffic_2560x1600_30_crop.yuv"]

if gprof == 0:
	bina = "TAppEncoderStatic"
	inf = ""
else:
	bina = "TAppEncoderStaticd"
	inf = "gprof"

file = open("%s/%s/%s"%(homepath,shpath,filename),"w")

try:
	os.system("mkdir %s/%s/"%(homepath,outpath))
except:
	pass
try:
	os.system("mkdir %s/%s/bin"%(homepath,outpath))
except:
	pass
try:
	os.system("mkdir %s/%s/out"%(homepath,outpath))
except:
	pass

if gprof == 1:
	try:
		os.system("mkdir %s/%s/gprof"%(homepath,outpath))
	except:
		pass
	try:
		os.system("mkdir %s/%s/gmon"%(homepath,outpath))
	except:
		pass

for taps in [8,6,4,2]:
	for yuv in yuvs:
		for qp in qps:

			if ".py" in yuv:
				continue
			if "bit" in yuv:
				continue

			if "crop" in yuv:
				vid,pix,fr,y = yuv.split("_")
				nome = vid+"_"+pix+"_"+fr
			else:
				vid,pix,fps = yuv.split("_")
				fr,y = fps.split(".")
				nome = vid+"_"+pix+"_"+fr

			w,h = pix.split("x")

			if conf == "encoder_randomaccess_main.cfg":
				info = "%staps_%sqp_%sfframes_RA_"%(taps,qp,f) + inf
			elif conf == "encoder_lowdelay_main.cfg":
				info = "%staps_%sqp_%sfframes_LD_"%(taps,qp,f) + inf
			elif conf == "encoder_intra_main.cfg":
				info = "%staps_%sqp_%sfframes_IO_"%(taps,qp,f) + inf
			else:
				info = "%staps_%sqp_%sfframes_"%(taps,qp,f) + inf

			#print w,h,f,fr,qp

			if gprof == 1:
				linha = "%s/%s/%s -c %s/%s/%s --InputFile=\"%s/%s\" -fr %s --SourceWidth=%s --SourceHeight=%s -q %s -f %s --fme_filter_ntaps=%s -b 8 --BitstreamFile=\"%s/%s/bin/%s_%s.bin\" > %s/%s/out/%s_%s.txt"%(homepath,binpath,bina,homepath,confpath,conf,yuvpath,yuv,fr,w,h,qp,f,taps,homepath,outpath,nome,info,homepath,outpath,nome,info)

				linha2 = "mv %s/%s/gmon.out %s/%s/gmon/gmon_%s_%s.out"%(homepath,shpath,homepath,outpath,nome,info)

				linha3 = "gprof %s/%s/%s %s/%s/gmon/gmon_%s_%s.out > %s/%s/gprof/%s_%s.txt"%(homepath,binpath,bina,homepath,outpath,nome,info,homepath,outpath,nome,info)

				linha4 =  "echo \"%s_%s DONE!\""%(nome,info)

				#VERIFICAR SOBRESCRICAO
				try:
					test = open("%s/%s/out/%s_%s.txt"%(homepath,outpath,nome,info),"r")
					tlines = test.readlines()
					tline = tlines[-1]
					if "Total Time" not in tline:
						if gitpull == 1:
							linhag = "cd %s/%s && sh %s.sh"%(homepath,gitpath,gitscript)
							print >> file, linha + " && " + linha2 + " && " + linha3 + " && " + linha4 + " && " + linhag
						else:
							print >> file, linha + " && " + linha2 + " && " + linha3 + " && " + linha4
				except:
					if gitpull == 1:
						linhag = "cd %s/%s && sh %s.sh"%(homepath,gitpath,gitscript)
						print >> file, linha + " && " + linha2 + " && " + linha3 + " && " + linha4 + " && " + linhag
					else:
						print >> file, linha + " && " + linha2 + " && " + linha3 + " && " + linha4
				
			else:
				linha = "%s/%s/%s -c %s/%s/%s --InputFile=\"%s/%s\" -fr %s --SourceWidth=%s --SourceHeight=%s -q %s -f %s --fme_filter_ntaps=%s -b 8 --BitstreamFile=\"%s/%s/bin/%s_%s.bin\" > %s/%s/out/%s_%s.txt"%(homepath,binpath,bina,homepath,confpath,conf,yuvpath,yuv,fr,w,h,qp,f,taps,homepath,outpath,nome,info,homepath,outpath,nome,info)
				
				linha4 =  "echo \"%s_%s DONE!\""%(nome,info)

				try:
					test = open("%s/%s/out/%s_%s.txt"%(homepath,outpath,nome,info),"r")
					tlines = test.readlines()
					tline = tlines[-1]
					if "Total Time" not in tline:
						if gitpull == 1:
							linhag = "cd %s/%s && sh %s.sh"%(homepath,gitpath,gitscript)
							print >> file, linha + " && " + linha4 + " && " + linhag
						else:
							print >> file, linha + " && " + linha4
				except:
					if gitpull == 1:
						linhag = "cd %s/%s && sh %s.sh"%(homepath,gitpath,gitscript)
						print >> file, linha + " && " + linha4 + " && " + linhag
					else:
						print >> file, linha + " && " + linha4

	if threads == 1:
		if gitpull == 1:
	 		linhag = "cd %s/%s && sh %s.sh || true"%(homepath,gitpath,gitscript)
	 		print >> file, linhag
	file.close