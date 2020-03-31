import os

f = 32 # numero de frames

gitpull = 1 # backup automatico para o git

server = 0 # local = 0 ; servidor = 1

#[37,32,27,22]

qps = [22,27,32,37]

#confs = ["encoder_randomaccess_vtm.cfg","encoder_lowdelay_vtm.cfg","encoder_intra_vtm.cfg"]

confs = ["encoder_randomaccess_vtm.cfg"]

OPT = 1 # optimizacoes ligadas = 1
gprof = 0

threads = 7 # numero de processos em parelelo

gitpath = "pesquisa_ucpel"
gitscript = "git_upl"

shpath = "pesquisa_ucpel/codes/run-sh/vtm"
filename = "run_vtm.sh"

#yuvs = ["BasketballPass_416x240_50fps_8bit_420.yuv","BasketballDrillText_832x480_50fps_8bit_420.yuv","SlideShow_1280x720_20fps_8bit_420.yuv","Cactus_1920x1080_50fps_8bit_420.yuv","Campfire_3840x2160_30fps_10bit_420.yuv"] #gprofiling

#yuvs = os.listdir("/home/icaro/origCfP")

#yuvs = ["BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30.yuv"] 														#ClasseD
#yuvs = ["RaceHorses_832x480_30.yuv","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv"] 																#ClasseC
#yuvs = ["FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","SlideEditing_1280x720_30.yuv"] 																							#ClasseE e F
#yuvs = ["Tennis_1920x1080_24.yuv","ParkScene_1920x1080_24.yuv","BasketballDrive_1920x1080_50.yuv","Kimono_1920x1080_24.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv"] 	#ClasseB
#yuvs = ["PeopleOnStreet_2560x1600_30_crop.yuv","Traffic_2560x1600_30_crop.yuv"] 																										#ClasseA

yuvs = ["BlowingBubbles_416x240_50fps_8bit_420.yuv","BQSquare_416x240_60fps_8bit_420.yuv","BasketballPass_416x240_50fps_8bit_420.yuv","RaceHorses_416x240_30fps_8bit_420.yuv","RaceHorses_832x480_30fps_8bit_420.yuv","BasketballDrill_832x480_50fps_8bit_420.yuv","BQMall_832x480_60fps_8bit_420.yuv","PartyScene_832x480_50fps_8bit_420.yuv","BasketballDrillText_832x480_50fps_8bit_420.yuv","SlideShow_1280x720_20fps_8bit_420.yuv","SlideEditing_1280x720_30fps_8bit_420.yuv","BasketballDrive_1920x1080_50fps_8bit_420.yuv","BQTerrace_1920x1080_60fps_8bit_420.yuv","Cactus_1920x1080_50fps_8bit_420.yuv","ArenaOfValor_1920x1080_60_8bit_420.yuv"]#,"MarketPlace_1920x1080_60fps_10bit_420.yuv","RitualDance_1920x1080_60fps_10bit_420.yuv","Campfire_3840x2160_30fps_10bit_420.yuv"]#,"Tango2_3840x2160_60fps_10bit_420.yuv","DaylightRoad2_3840x2160_60fps_10bit_420.yuv","ParkRunning3_3840x2160_50fps_10bit_420.yuv"]#,"FoodMarket4_3840x2160_60fps_10bit_420.yuv","CatRobot_3840x2160_60fps_10bit_420.yuv"]	#VVC

if server == 1:	
	homepath = "/home/grellert"
	yuvpath = "/videos"
	outpath = "pesquisa_ucpel/output_VTM/server"
	binpath = "vtm/build" #partindo da homepath
	confpath = "vtm/cfg"

	#yuvs = ["BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30.yuv","RaceHorses_832x480_30.yuv","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv","FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","SlideEditing_1280x720_30.yuv","Tennis_1920x1080_24.yuv","ParkScene_1920x1080_24.yuv","BasketballDrive_1920x1080_50.yuv","Kimono_1920x1080_24.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","PeopleOnStreet_2560x1600_30_crop.yuv","Traffic_2560x1600_30_crop.yuv"]

else:
	homepath = "/home/icaro"
	yuvpath = "/home/icaro/origCfP"
	outpath = "pesquisa_ucpel/output_VTM/local"
	binpath = "vtm/bin" #partindo da homepath
	confpath = "vtm/cfg"

	#yuvs = ["BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30.yuv","RaceHorses_832x480_30.yuv","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv","ParkScene_1920x1080_24.yuv","BasketballDrive_1920x1080_50.yuv","Kimono_1920x1080_24.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","PeopleOnStreet_2560x1600_30_crop.yuv","Traffic_2560x1600_30_crop.yuv"]

if OPT == 1:
	simd = "--SIMD=AVX2"
	if gprof == 0:
		#bina = "EncoderAppStatic_std"
		bina = "EncoderAppStatic"
		inf = "OPT"
	else:
		bina = "EncoderAppStaticd_gprof"
		inf = "gprof_OPT"
else:
	simd = "--SIMD=SCALAR"
	if gprof == 0:
		#bina = "EncoderAppStatic_std"
		bina = "EncoderAppStatic"
		inf = "noOPT"
	else:
		bina = "EncoderAppStaticd_gprof"
		inf = "gprof_noOPT"

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

for conf in confs:
	for yuv in yuvs:
		for qp in qps:
			print yuv
			if ".py" in yuv:
				continue
			if "crop" in yuv:
				vid,pix,fr,dummy,b,dummy = yuv.split("_")
				b = b.strip("bit")
				fr = fr.strip("fps")
				nome = vid+"_"+pix+"_"+fr+"fps"+"_"+b+"bit"
			else:
				vid,pix,fr,b,dummy = yuv.split("_")
				b = b.strip("bit")
				fr = fr.strip("fps")
				nome = vid+"_"+pix+"_"+fr+"fps"+"_"+b+"bit"

			w,h = pix.split("x")

			if conf == "encoder_randomaccess_vtm.cfg":
				info = "%sqp_%sfframes_RA_"%(qp,f) + inf
			elif conf == "encoder_lowdelay_vtm.cfg":
				info = "%sqp_%sfframes_LD_"%(qp,f) + inf
			elif conf == "encoder_intra_vtm.cfg":
				info = "%sqp_%sfframes_IO_"%(qp,f) + inf
			else:
				info = "%sqp_%sfframes_"%(qp,f) + inf


			#qp = map(float,qp) !!--end-usage=q!!--AVALIAR

			if gprof == 1:
				linha = "%s/%s/%s -c %s/%s/%s --InputFile=\"%s/%s\" -fr %s --SourceWidth=%s --SourceHeight=%s -q %s -f %s --InputBitDepth=%s %s --BitstreamFile=\"%s/%s/bin4taps/%s_%s.bin\" > %s/%s/out4taps/%s_%s.txt"%(homepath,binpath,bina,homepath,confpath,conf,yuvpath,yuv,fr,w,h,qp,f,b,simd,homepath,outpath,nome,info,homepath,outpath,nome,info)
				linha2 = "mv gmon.out %s/%s/gmon/gmon_%s_%s.out"%(homepath,outpath,nome,info)
				linha3 = "gprof %s/%s/%s %s/%s/gmon/gmon_%s_%s.out > %s/%s/gprof/%s_%s.txt"%(homepath,binpath,bina,homepath,outpath,nome,info,homepath,outpath,nome,info)
				linha4 =  "echo \"%s_%s DONE!\""%(nome,info)

				#VERIFICAR SOBRESCRICAO
				try:
					test = open("%s/%s/gmon/gmon_%s_%s.out"%(homepath,outpath,nome,info),"r")
					#tlines = test.readlines()
					#tline = tlines[-1]
					#if "Total Time" not in tline:
					#	if gitpull == 1:
					#		linhag = "cd %s/%s && sh %s.sh"%(homepath,gitpath,gitscript)
					#		print >> file, linha + " && " + linha2 + " && " + linha3 + " && " + linhag + " && " + linha4
					#	else:
					#		print >> file, linha + " && " + linha2 + " && " + linha3 + " && " + linha4
				except:
					if gitpull == 1:
						linhag = "sh %s/%s/%s.sh"%(homepath,gitpath,gitscript)
						print >> file, linha + " && " + linha2 + " && " + linha3 + " && " + linha4 + " && " + linhag
					else:
						print >> file, linha + " && " + linha2 + " && " + linha3 + " && " + linha4
				
			else:
				linha = "%s/%s/%s -c %s/%s/%s --InputFile=\"%s/%s\" -fr %s --SourceWidth=%s --SourceHeight=%s -q %s -f %s --InputBitDepth=%s %s --BitstreamFile=\"%s/%s/bin4taps/%s_%s.bin\" > %s/%s/out4taps/%s_%s.txt"%(homepath,binpath,bina,homepath,confpath,conf,yuvpath,yuv,fr,w,h,qp,f,b,simd,homepath,outpath,nome,info,homepath,outpath,nome,info)
				linha4 =  "echo \"%s_%s DONE!\""%(nome,info)

				try:
					test = open("%s/%s/out4taps/%s_%s.txt"%(homepath,outpath,nome,info),"r")
					tlines = test.readlines()
					tline = tlines[-1]
					if "Total Time" not in tline:
						if gitpull == 1:
							linhag = "sh %s/%s/%s.sh"%(homepath,gitpath,gitscript)
							print >> file, linha + " && " + linha4 + " && " + linhag
						else:
							print >> file, linha + " && " + linha4
				except:
					if gitpull == 1:
						linhag = "sh %s/%s/%s.sh"%(homepath,gitpath,gitscript)
						print >> file, linha + " && " + linhag + " && " + linha4
					else:
						print >> file, linha + " && " + linha4

	# if threads == 1:
	# 	if gitpull == 1:
	#  		linhag = "cd %s/%s && sh %s.sh || true"%(homepath,gitpath,gitscript)
	#  		print >> file, linhag
	# file.close

i=0
if threads != 1:

	file = open("%s/%s/%s"%(homepath,shpath,filename),"r")
	lines = file.readlines()
	tam = len(lines)
	nqp = len(qps)
	nconf = len(confs)

	for x in range(threads):

		try:
			os.system("mkdir %s/%s/script%d"%(homepath,shpath,x+1))
		except:
			pass

		file2 = open("%s/%s/script%d/%d_%s"%(homepath,shpath,x+1,x+1,filename),"w")
		i = x*nqp
		j=0

		while i < tam:

			line = lines[i]
			print >> file2, line

			i = i+1
			j = j+1

			if j == nqp:
				j=0
				i = (i-nqp)+(nqp*threads)
			# if nqp == 4:
			# 	if ((i-1)%4) == 3:
			# 		i = i+threads*(3)
			# else:
			# 	j = j+1
			# 	div = tam/threads
			# 	if j == div:
			# 		i = i+threads*div
			# 		j=0
		# if gitpull == 1:
		# 	linhag = "cd %s/%s && sh %s.sh || true"%(homepath,gitpath,gitscript)
		# 	print >> file2, linhag
	file2.close
file.close
