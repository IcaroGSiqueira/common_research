import os

f = 32 # numero de frames

gitpull = 1 # backup automatico para o git

server = 0 # local = 0 ; servidor = 1

#[37,32,27,22]

qps = [22,27,32,37]

#["encoder_randomaccess_vtm.cfg","encoder_lowdelay_vtm.cfg","encoder_intra_vtm.cfg"]

confs = ["encoder_randomaccess_vtm.cfg"]

OPT = 0 # optimizacoes ligadas = 1
gprof = 0
debug = 1 # se gprof = 1 debug = 0

#threads = 8 # numero de processos em parelelo

gitpath = "pesquisa_ucpel"
gitscript = "git_upl"

shpath = "pesquisa_ucpel/codes/run-sh/vtm"
filename = "run_dec_vtm.sh"

# manter YUVS em ordem de menor para maior resolucao para melhor eficiencia no paralelismo
yuvs = ["BlowingBubbles_416x240_50fps_8bit_420.yuv","BQSquare_416x240_60fps_8bit_420.yuv","BasketballPass_416x240_50fps_8bit_420.yuv","RaceHorses_416x240_30fps_8bit_420.yuv","RaceHorses_832x480_30fps_8bit_420.yuv","BasketballDrill_832x480_50fps_8bit_420.yuv","BQMall_832x480_60fps_8bit_420.yuv","PartyScene_832x480_50fps_8bit_420.yuv","BasketballDrillText_832x480_50fps_8bit_420.yuv","SlideShow_1280x720_20fps_8bit_420.yuv","SlideEditing_1280x720_30fps_8bit_420.yuv","BasketballDrive_1920x1080_50fps_8bit_420.yuv","BQTerrace_1920x1080_60fps_8bit_420.yuv","Cactus_1920x1080_50fps_8bit_420.yuv","ArenaOfValor_1920x1080_60_8bit_420.yuv","MarketPlace_1920x1080_60fps_10bit_420.yuv","RitualDance_1920x1080_60fps_10bit_420.yuv"]#,"Campfire_3840x2160_30fps_8bit_420.yuv","Tango2_3840x2160_60fps_10bit_420.yuv","DaylightRoad2_3840x2160_60fps_10bit_420.yuv","ParkRunning3_3840x2160_50fps_10bit_420.yuv"]#,"FoodMarket4_3840x2160_60fps_10bit_420.yuv","CatRobot_3840x2160_60fps_10bit_420.yuv"] 

#yuvs = os.listdir("/home/icaro/origCfP")

#yuvs = ["BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30.yuv"] 														#ClasseD
#yuvs = ["RaceHorses_832x480_30.yuv","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv"] 																#ClasseC
#yuvs = ["FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","SlideEditing_1280x720_30.yuv"] 																							#ClasseE e F
#yuvs = ["Tennis_1920x1080_24.yuv","ParkScene_1920x1080_24.yuv","BasketballDrive_1920x1080_50.yuv","Kimono_1920x1080_24.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv"] 	#ClasseB
#yuvs = ["PeopleOnStreet_2560x1600_30_crop.yuv","Traffic_2560x1600_30_crop.yuv"] 																										#ClasseA

#["BlowingBubbles_416x240_50fps_8bit_420.yuv","BQSquare_416x240_60fps_8bit_420.yuv","BasketballPass_416x240_50fps_8bit_420.yuv","RaceHorses_416x240_30fps_8bit_420.yuv","RaceHorses_832x480_30fps_8bit_420.yuv","BasketballDrill_832x480_50fps_8bit_420.yuv","BQMall_832x480_60fps_8bit_420.yuv","PartyScene_832x480_50fps_8bit_420.yuv","BasketballDrillText_832x480_50fps_8bit_420.yuv","SlideShow_1280x720_20fps_8bit_420.yuv","SlideEditing_1280x720_30fps_8bit_420.yuv","BasketballDrive_1920x1080_50fps_8bit_420.yuv","BQTerrace_1920x1080_60fps_8bit_420.yuv","Cactus_1920x1080_50fps_8bit_420.yuv","ArenaOfValor_1920x1080_60_8bit_420.yuv","MarketPlace_1920x1080_60fps_10bit_420.yuv","RitualDance_1920x1080_60fps_10bit_420.yuv","Campfire_3840x2160_30fps_8bit_420.yuv","Tango2_3840x2160_60fps_10bit_420.yuv","DaylightRoad2_3840x2160_60fps_10bit_420.yuv","ParkRunning3_3840x2160_50fps_10bit_420.yuv","FoodMarket4_3840x2160_60fps_10bit_420.yuv","CatRobot_3840x2160_60fps_10bit_420.yuv"]														#VVC

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

	#yuvs = ["BlowingBubbles_416x240_50fps_8bit_420.yuv","BQSquare_416x240_60fps_8bit_420.yuv","BasketballPass_416x240_50fps_8bit_420.yuv","RaceHorses_416x240_30fps_8bit_420.yuv","RaceHorses_832x480_30fps_8bit_420.yuv","BasketballDrill_832x480_50fps_8bit_420.yuv","BQMall_832x480_60fps_8bit_420.yuv","PartyScene_832x480_50fps_8bit_420.yuv","BasketballDrillText_832x480_50fps_8bit_420.yuv","SlideShow_1280x720_20fps_8bit_420.yuv","SlideEditing_1280x720_30fps_8bit_420.yuv","BasketballDrive_1920x1080_50fps_8bit_420.yuv","BQTerrace_1920x1080_60fps_8bit_420.yuv","Cactus_1920x1080_50fps_8bit_420.yuv","ArenaOfValor_1920x1080_60_8bit_420.yuv","MarketPlace_1920x1080_60fps_10bit_420.yuv","RitualDance_1920x1080_60fps_10bit_420.yuv","Campfire_3840x2160_30fps_8bit_420.yuv","Tango2_3840x2160_60fps_10bit_420.yuv","DaylightRoad2_3840x2160_60fps_10bit_420.yuv","ParkRunning3_3840x2160_50fps_10bit_420.yuv"]

if OPT == 1:
	if gprof == 0:
		bina = "DecoderAppStatic_std"
		inf = "OPT"
	else:
		bina = "DecoderAppStaticd_gprof"
		inf = "gprof_OPT"
	if debug == 1:
		bina = "DecoderAppStaticd_std"
		inf = "OPT"
else:
	if gprof == 0:
		bina = "DecoderAppStatic_std"
		inf = "noOPT"
	else:
		bina = "DecoderAppStaticd_gprof"
		inf = "gprof_noOPT"
	if debug == 1:
		bina = "DecoderAppStaticd_std"
		inf = "noOPT"


file = open("%s/%s/%s"%(homepath,shpath,filename),"w")

try:
	os.system("mkdir %s/%s/"%(homepath,outpath))
except:
	pass
try:
	os.system("mkdir %s/%s/traces"%(homepath,outpath))
except:
	pass

for conf in confs:
	for yuv in yuvs:
		for qp in qps:
			for i in range(32):
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
					linha = "%s/%s/%s -b %s/%s/bin/%s_%s.bin -o %s/Videos/%s_%s.yuv --TraceFile=\"%s/%s/traces/%s_%s_poc%d.csv\" --TraceRule=D_BLOCK_STATISTICS_CODED:poc==%d"%(homepath,binpath,bina,homepath,outpath,nome,info,homepath,nome,info,homepath,outpath,nome,info,i,i)
					linha4 =  "echo \"%s_%s_poc%s DONE!\""%(nome,info,i)

					#VERIFICAR SOBRESCRICAO
					try:
						test = open("%s/%s/traces/%s_%s.txt"%(homepath,outpath,nome,info),"r")
					except:
						print >> file, linha + " && " + linha2 + " && " + linha3 + " && " + linha4
					
				else:
					linha = "%s/%s/%s -b %s/%s/bin/%s_%s.bin -o %s/Videos/%s_%s.yuv --TraceFile=\"%s/%s/traces/%s_%s_poc%d.csv\" --TraceRule=D_BLOCK_STATISTICS_CODED:poc==%d"%(homepath,binpath,bina,homepath,outpath,nome,info,homepath,nome,info,homepath,outpath,nome,info,i,i)
					linha4 =  "echo \"%s_%s_poc%s DONE!\""%(nome,info,i)

					try:
						test = open("%s/%s/traces/%s_%s.txt"%(homepath,outpath,nome,info),"r")
					except:
						print >> file, linha + " && " + linha4

	# GIT PULL on end of the file
	if gitpull == 1:
		linhag = "cd %s/%s && sh %s.sh || true"%(homepath,gitpath,gitscript)
		print >> file, linhag
	file.close

# i=0
# if threads != 1:

# 	file = open("%s/%s/%s"%(homepath,shpath,filename),"r")
# 	lines = file.readlines()
# 	tam = len(lines)
# 	nqp = len(qps)
# 	nconf = len(confs)

# 	for x in range(threads):

# 		file2 = open("%s/%s/%d_%s"%(homepath,shpath,x+1,filename),"w")
# 		i = x*nqp
# 		j=0

# 		while i < tam:

# 			line = lines[i]
# 			print >> file2, line

# 			i = i+1
# 			j = j+1

# 			if j == nqp:
# 				j=0
# 				i = (i-nqp)+(nqp*threads)
# 			# if nqp == 4:
# 			# 	if ((i-1)%4) == 3:
# 			# 		i = i+threads*(3)
# 			# else:
# 			# 	j = j+1
# 			# 	div = tam/threads
# 			# 	if j == div:
# 			# 		i = i+threads*div
# 			# 		j=0
#		# GIT PULL on end of the file
# 		# if gitpull == 1:
# 		# 	linhag = "cd %s/%s && sh %s.sh || true"%(homepath,gitpath,gitscript)
# 		# 	print >> file2, linhag
# 	file2.close
file.close
