import os

f = 32 # numero de frames

#[37,32,27,22]

qps = [22,27,32,37]

#confs = ["encoder_randomaccess_vtm.cfg","encoder_lowdelay_vtm.cfg","encoder_intra_vtm.cfg"]

confs = ["encoder_randomaccess_vtm.cfg"]

minqs = [8,16,32]

OPT = 1 # optimizacoes ligadas = 1
gprof = 0

taps = 6

threads = 4 # numero de processos em parelelo

#yuvs=[Tennis_1920x1080_24.yuv","ParkScene_1920x1080_24.yuv","Kimono_1920x1080_24.yuv","PeopleOnStreet_2560x1600_30_crop.yuv","Traffic_2560x1600_30_crop.yuv"]#OLD

#yuvs = ["BasketballPass_416x240_50fps_8bit_420.yuv","BasketballDrillText_832x480_50fps_8bit_420.yuv","SlideShow_1280x720_20fps_8bit_420.yuv","Cactus_1920x1080_50fps_8bit_420.yuv","Campfire_3840x2160_30fps_10bit_420.yuv"] #gprofiling

#yuvs=["Campfire_3840x2160_30fps_10bit_420.yuv","FoodMarket4_3840x2160_60fps_10bit_420.yuv","Tango2_3840x2160_60fps_10bit_420.yuv"]#ClasseA1

#yuvs=["ParkRunning3_3840x2160_50fps_10bit_420.yuv","CatRobot_3840x2160_60fps_10bit_420.yuv","DaylightRoad2_3840x2160_60fps_10bit_420.yuv"]#ClasseA2

#yuvs=["BasketballDrive_1920x1080_50.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","MarketPlace_1920x1080_60fps_10bit_420.yuv","RitualDance_1920x1080_60fps_10bit_420.yuv"]#ClasseB

#yuvs=["RaceHorses_832x480_30fps_8bit_420","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv"]#ClasseC

#yuvs=["BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30fps_8bit_420.yuv"]#ClasseD

#yuvs=["FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","KristenAndSara_1280x720_60fps_8bit_420.yuv"]#ClasseE

#yuvs=[ArenaOfValor_1920x1080_60fps_8bit_420.yuv,"BasketballDrillText_832x480_50fps_8bit_420.yuv","SlideShow_1280x720_20fps_8bit_420.yuv","SlideEditing_1280x720_30.yuv"]#ClasseF


#yuvsvvc = ["MarketPlace_1920x1080_60fps_10bit_420.yuv","RitualDance_1920x1080_60fps_10bit_420.yuv","ArenaOfValor_1920x1080_60fps_8bit_420.yuv","BasketballDrillText_832x480_50fps_8bit_420.yuv","SlideShow_1280x720_20fps_8bit_420.yuv","Campfire_3840x2160_30fps_10bit_420.yuv","KristenAndSara_1280x720_60fps_8bit_420.yuv","FoodMarket4_3840x2160_60fps_10bit_420.yuv","Tango2_3840x2160_60fps_10bit_420.yuv","ParkRunning3_3840x2160_50fps_10bit_420.yuv","CatRobot_3840x2160_60fps_10bit_420.yuv","DaylightRoad2_3840x2160_60fps_10bit_420.yuv"]	#VVC

#yuvshevc = ["RaceHorses_832x480_30.yuv","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv","BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30.yuv","BasketballDrive_1920x1080_50.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","SlideEditing_1280x720_30.yuv"]	#VVC_HEVC

yuvs = ["RaceHorses_832x480_30.yuv","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv","BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30.yuv","BasketballDrive_1920x1080_50.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","MarketPlace_1920x1080_60fps_10bit_420.yuv","RitualDance_1920x1080_60fps_10bit_420.yuv","ArenaOfValor_1920x1080_60fps_8bit_420.yuv","BasketballDrillText_832x480_50fps_8bit_420.yuv","SlideShow_1280x720_20fps_8bit_420.yuv","Campfire_3840x2160_30fps_10bit_420.yuv","FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","KristenAndSara_1280x720_60fps_8bit_420.yuv","FoodMarket4_3840x2160_60fps_10bit_420.yuv","Tango2_3840x2160_60fps_10bit_420.yuv","SlideEditing_1280x720_30.yuv","ParkRunning3_3840x2160_50fps_10bit_420.yuv","CatRobot_3840x2160_60fps_10bit_420.yuv","DaylightRoad2_3840x2160_60fps_10bit_420.yuv"]	#VVC

#yuvs=["BlowingBubbles_416x240_50.yuv"] #test

#homepath = "/home/icaro"
#yuvpath = "/home/icaro/Videos"
#outpath = "output_VTM"
#encpath = "vtm9.1"
#confpath = "%s/cfg"%encpath
#binpath = "%s/bin"%encpath #partindo da homepath
#shpath = "%s/Documents/pesquisa/common_research/codes/run-sh/vtm"%homepath


homepath = "/home/grellert"

yuvvvc = "%s/videos/vvc_sets"%homepath
yuvhevc = "/videos"

outpath = "%s/output_VTM"%homepath

#encpath = "%s/encoders/vtm10.0"%homepath
encpath = "%s/encoders/vvc_10.0_approx"%homepath

confpath = "%s/cfg"%encpath
binpath = "%s/bin"%encpath

shpath = "../vtm"

filename = "run_vtm.sh"

#yuvs = os.listdir("/home/icaro/origCfP")

if OPT == 1:
	simd = "AVX2"
	if gprof == 0:
		#bina = "EncoderAppStatic_std"
		bina = "EncoderAppStatic"
		inf = "OPT"
	else:
		bina = "EncoderAppStaticd"
		inf = "gprof_OPT"
else:
	simd = "SCALAR"
	if gprof == 0:
		#bina = "EncoderAppStatic_std"
		bina = "EncoderAppStatic"
		inf = "noOPT"
	else:
		bina = "EncoderAppStaticd"
		inf = "gprof_noOPT"

#file = open("/home/icaro/git_repo/common_research/codes/run-sh/vtm/%s"%filename,"w")

file = open("%s/%s"%(shpath,filename),"w")

try:
	os.system("mkdir %s/"%(outpath))
except:
	pass
try:
	os.system("mkdir %s/bin"%(outpath))
except:
	pass
try:
	os.system("mkdir %s/out"%(outpath))
except:
	pass

if gprof == 1:
	try:
		os.system("mkdir %s/gprof"%(outpath))
	except:
		pass
	try:
		os.system("mkdir %s/gmon"%(outpath))
	except:
		pass

for conf in confs:
	for yuv in yuvs:
		for qp in qps:
			#for minq in minqs:

			print(yuv)
			try:
				vid,pix,fr,b,dummy = yuv.split("_")
				b = b.strip("bit")
				fr = fr.strip("fps")
				nome = vid+"_"+pix+"_"+fr+"fps"+"_"+b+"bit"
			except:
				vid,pix,fr = yuv.split("_")
				b = "8"
				fr = fr.strip(".yuv")
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

			#linha = "%s/%s/%s -c %s/%s/%s -i \"%s/%s\" -fr %s -wdt %s -hgt %s -q %s -f %s --MinQTLumaISlice=%s --MinQTChromaISliceInChromaSamples=%s --MinQTNonISlice=%s --InputBitDepth=%s --SIMD=%s -b \"%s/%s/bin/%s_%s.bin\" "%(homepath,binpath,bina,homepath,confpath,conf,yuvpath,yuv,fr,w,h,qp,f,minq,int(minq/2),minq,b,simd,homepath,outpath,nome,info) # Linha de configuracao da codificacao

			if yuv in ["MarketPlace_1920x1080_60fps_10bit_420.yuv",
				"RitualDance_1920x1080_60fps_10bit_420.yuv",
				"ArenaOfValor_1920x1080_60fps_8bit_420.yuv",
				"BasketballDrillText_832x480_50fps_8bit_420.yuv",
				"SlideShow_1280x720_20fps_8bit_420.yuv",
				"Campfire_3840x2160_30fps_10bit_420.yuv",
				"KristenAndSara_1280x720_60fps_8bit_420.yuv",
				"FoodMarket4_3840x2160_60fps_10bit_420.yuv",
				"Tango2_3840x2160_60fps_10bit_420.yuv",
				"ParkRunning3_3840x2160_50fps_10bit_420.yuv",
				"CatRobot_3840x2160_60fps_10bit_420.yuv",
				"DaylightRoad2_3840x2160_60fps_10bit_420.yuv"]:

				linha = "%s/%s -c %s/%s -i \"%s/%s\" -fr %s -wdt %s -hgt %s -q %s -f %s --InputBitDepth=%s --fme_filter_ntaps=%s --SIMD=%s -b \"%s/bin/%s_%s.bin\" "%(binpath,bina,confpath,conf,yuvvvc,yuv,fr,w,h,qp,f,b,taps,simd,outpath,nome,info) # Linha de configuracao da codificacao

			elif yuv in ["RaceHorses_832x480_30.yuv",
				"BasketballDrill_832x480_50.yuv",
				"BQMall_832x480_60.yuv",
				"PartyScene_832x480_50.yuv",
				"BlowingBubbles_416x240_50.yuv",
				"BQSquare_416x240_60.yuv",
				"BasketballPass_416x240_50.yuv",
				"RaceHorses_416x240_30.yuv",
				"BasketballDrive_1920x1080_50.yuv",
				"BQTerrace_1920x1080_60.yuv",
				"Cactus_1920x1080_50.yuv",
				"FourPeople_1280x720_60.yuv",
				"Johnny_1280x720_60.yuv",
				"SlideEditing_1280x720_30.yuv"]:

				linha = "%s/%s -c %s/%s -i \"%s/%s\" -fr %s -wdt %s -hgt %s -q %s -f %s --InputBitDepth=%s --fme_filter_ntaps=%s --SIMD=%s -b \"%s/bin/%s_%s.bin\" "%(binpath,bina,confpath,conf,yuvhevc,yuv,fr,w,h,qp,f,b,taps,simd,outpath,nome,info) # Linha de configuracao da codificacao

			linha1 = "> %s/out/%s_%s.txt"%(outpath,nome,info) # linha da saida da codificacao

			# linhas do profiling
			linha2 = "mv gmon.out %s/gmon/gmon_%s_%s.out"%(outpath,nome,info)

			linha3 = "gprof %s/%s %s/gmon/gmon_%s_%s.out > %s/gprof/%s_%s.txt"%(binpath,bina,outpath,nome,info,outpath,nome,info)

			linha4 =  "echo \"%s_%s DONE!\""%(nome,info)

			#VERIFICAR SOBRESCRICAO
			if gprof == 1:
				try:
					test = open("%s/%s"%(shpath,filename),"r")
					tlines = test.readlines()
					tline = tlines[0]
					if linha not in tline:
						file.write(linha + linha1 + " && " + linha4 + "\n")
				except:
					file.write(linha + linha1 + " && " + linha2 + " && " + linha3 + " && " + linha4 + "\n")

			else:	
				try:
					test = open("%s/%s_%s.txt"%(outpath,nome,info),"r")
					tlines = test.readlines()
					tline = tlines[-1]
					if "Total Time" not in tline:
						file.write(linha + linha1 + " && " + linha4 + "\n")
				except:
					file.write(linha + linha1 + " && " + linha4 + "\n")


i=0
if threads >= 1:

	file = open("%s/%s"%(shpath,filename),"r")

	lines = file.readlines()
	tam = len(lines)
	nqp = len(qps)
	nconf = len(confs)

	for x in range(threads):

		try:
			os.system("mkdir %s/script%d"%(shpath,x+1))
		except:
			pass
		file2 = open("%s/script%d/%d_%s_taps.sh"%(shpath,x+1,x+1,inf),"w")
		i = x*nqp
		j=0

		while i < tam:

			line = lines[i]
			file2.write(line)

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
