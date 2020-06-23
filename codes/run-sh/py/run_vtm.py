import os

f = 8 # numero de frames

#[37,32,27,22]

qps = [22,27,32,37]

#confs = ["encoder_randomaccess_vtm.cfg","encoder_lowdelay_vtm.cfg","encoder_intra_vtm.cfg"]

confs = ["encoder_randomaccess_vtm.cfg"]

minqs = [8,16,32]

OPT = 0 # optimizacoes ligadas = 1
gprof = 1

threads = 4 # numero de processos em parelelo

#shpath = "git_repo/common_research/codes/run-sh/vtm"
filename = "run_vtm.sh"

shpath = "pesquisa_av1/common_research/codes/run-sh/vtm"

#yuvs = ["BasketballPass_416x240_50fps_8bit_420.yuv","BasketballDrillText_832x480_50fps_8bit_420.yuv","SlideShow_1280x720_20fps_8bit_420.yuv","Cactus_1920x1080_50fps_8bit_420.yuv","Campfire_3840x2160_30fps_10bit_420.yuv"] #gprofiling

#yuvs = os.listdir("/home/icaro/origCfP")

#yuvs = ["BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30fps_8bit_420.yuv"] 														#ClasseD
#yuvs = ["RaceHorses_832x480_30fps_8bit_420","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv"] 																#ClasseC
#yuvs = ["FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","SlideEditing_1280x720_30.yuv"] 																							#ClasseE e F
#yuvs = ["Tennis_1920x1080_24.yuv","ParkScene_1920x1080_24.yuv","BasketballDrive_1920x1080_50.yuv","Kimono_1920x1080_24.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv"] 	#ClasseB
#yuvs = ["PeopleOnStreet_2560x1600_30_crop.yuv","Traffic_2560x1600_30_crop.yuv"] 																										#ClasseA

yuvs = ["BlowingBubbles_416x240_50fps_8bit_420.yuv", "RaceHorses_832x480_30fps_8bit_420"]	#VVC


#homepath = "/home/icaro"
#yuvpath = "/home/icaro/Videos"
outpath = "output_VTM"
#binpath = "VVCSoftware_VTM/bin" #partindo da homepath
#confpath = "VVCSoftware_VTM/cfg"

homepath = "/home/grellert"
yuvpath = "/home/grellert/videos/vvc_sets"
#outpath = "output_VTM"
confpath = "encoders/vtm9.1/cfg"


if OPT == 1:
	simd = "AVX2"
	if gprof == 0:
		#bina = "EncoderAppStatic_std"
		binpath = "encoders/vtm9.1/bin" #partindo da homepath
		bina = "EncoderAppStatic"
		inf = "OPT"
	else:
		binpath = "encoders/vtm9.1/build_gprof" #partindo da homepath
		bina = "EncoderAppStaticd"
		inf = "gprof_OPT"
else:
	simd = "SCALAR"
	if gprof == 0:
		#bina = "EncoderAppStatic_std"
		binpath = "encoders/vtm9.1/bin" #partindo da homepath
		bina = "EncoderAppStatic"
		inf = "noOPT"
	else:
		binpath = "encoders/vtm9.1/build_gprof" #partindo da homepath
		bina = "EncoderAppStaticd"
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
			for minq in minqs:
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

				if gprof == 1:
					linha = "%s/%s/%s -c %s/%s/%s -i \"%s/%s\" -fr %s -wdt %s -hgt %s -q %s -f %s --MinQTLumaISlice=%s --MinQTChromaISliceInChromaSamples=%s --MinQTNonISlice=%s --InputBitDepth=%s --SIMD=%s -b \"%s/%s/bin/%s_%s.bin\" > %s/%s/out/%s_%s.txt"%(homepath,binpath,bina,homepath,confpath,conf,yuvpath,yuv,fr,w,h,qp,f,minq,minq/2,minq,b,simd,homepath,outpath,nome,info,homepath,outpath,nome,info)

					linha2 = "mv gmon.out %s/%s/gmon/gmon_%s_%s.out"%(homepath,outpath,nome,info)

					linha3 = "gprof %s/%s/%s %s/%s/gmon/gmon_%s_%s.out > %s/%s/gprof/%s_%s.txt"%(homepath,binpath,bina,homepath,outpath,nome,info,homepath,outpath,nome,info)

					linha4 =  "echo \"%s_%s DONE!\""%(nome,info)

					#VERIFICAR SOBRESCRICAO
					try:
						test = open("%s/%s/%s"%(homepath,shpath,filename),"r")
						tlines = test.readlines()
						tline = tlines[0]
						if linha not in tline:
							print >> file, linha + " && " + linha4
					except:
						print >> file, linha + " && " + linha2 + " && " + linha3 + " && " + linha4
					
				else:
					linha = "%s/%s/%s -c %s/%s/%s --InputFile=\"%s/%s\" -fr %s --SourceWidth=%s --SourceHeight=%s -q %s -f %s --InputBitDepth=%s %s --BitstreamFile=\"%s/%s/bin/%s_%s.bin\" > %s/%s/out/%s_%s.txt"%(homepath,binpath,bina,homepath,confpath,conf,yuvpath,yuv,fr,w,h,qp,f,b,simd,homepath,outpath,nome,info,homepath,outpath,nome,info)
					linha4 =  "echo \"%s_%s DONE!\""%(nome,info)

					try:
						test = open("%s/%s/%s_%s.txt"%(homepath,outpath,nome,info),"r")
						tlines = test.readlines()
						tline = tlines[-1]
						if "Total Time" not in tline:
							print >> file, linha + " && " + linha4
					except:
						print >> file, linha + " && " + linha4


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
