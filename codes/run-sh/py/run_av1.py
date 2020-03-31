import os

f = 30

gitpull = 1

server = 0 # local = 0 ; servidor = 1

#[37,32,27,22]

qps = [22,27,32,37]

OPT = 0 # optimizacoes ligadas = 1
gprof = 1

threads = 4 # numero de processos em parelelo

gitpath = "pesquisa_ucpel"
gitscript = "git_upl"

shpath = "pesquisa_ucpel/codes/run-sh/aom"
filename = "run_av1.sh"

yuvs = ["RaceHorses_832x480_30.yuv","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv"] 

#yuvs = os.listdir("/home/icaro/origCfP")

#["BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30.yuv"] 														#ClasseD
#["RaceHorses_832x480_30.yuv","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv"] 															#ClasseC
#["FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","SlideEditing_1280x720_30.yuv"] 																						#ClasseE e F
#["Tennis_1920x1080_24.yuv","ParkScene_1920x1080_24.yuv","BasketballDrive_1920x1080_50.yuv","Kimono_1920x1080_24.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv"] 	#ClasseB
#["PeopleOnStreet_2560x1600_30_crop.yuv","Traffic_2560x1600_30_crop.yuv"] 																										#ClasseA

if server == 1:	
	homepath = "/home/grellert"
	yuvpath = "/videos"
	outpath = "pesquisa_ucpel/output_AV1/server"
	binpath = "aom/build" #partindo da homepath

	yuvs = ["BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30.yuv","RaceHorses_832x480_30.yuv","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv","FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","SlideEditing_1280x720_30.yuv","Tennis_1920x1080_24.yuv","ParkScene_1920x1080_24.yuv","BasketballDrive_1920x1080_50.yuv","Kimono_1920x1080_24.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","PeopleOnStreet_2560x1600_30_crop.yuv","Traffic_2560x1600_30_crop.yuv"]

else:
	homepath = "/home/icaro"
	yuvpath = "/home/icaro/origCfP"
	outpath = "pesquisa_ucpel/output_AV1/local"
	binpath = "aom/build" #partindo da homepath

	#yuvs = ["BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30.yuv","RaceHorses_832x480_30.yuv","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv","ParkScene_1920x1080_24.yuv","BasketballDrive_1920x1080_50.yuv","Kimono_1920x1080_24.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","PeopleOnStreet_2560x1600_30_crop.yuv","Traffic_2560x1600_30_crop.yuv"]

if OPT == 1:
	if gprof == 0:
		bina = "aomenc_OPT"
		inf = "OPT"
	else:
		bina = "aomenc_gprof_OPT"
		inf = "gprof_OPT"
else:
	if gprof == 0:
		bina = "aomenc_noOPT"
		inf = "noOPT"
	else:
		bina = "aomenc_gprof_noOPT"
		inf = "gprof_noOPT"

file = open("%s/%s/%s"%(homepath,shpath,filename),"w")

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
		info = "%sqp_%sfframes_"%(qp,f) + inf

		#qp = map(float,qp) !!--end-usage=q!!--AVALIAR

		if gprof == 1:
			linha = "%s/%s/%s --fps=%s/1 -w %s -h %s --min-q=%s --max-q=%s --limit=%s --rt -b 8 -o %s/%s/bin/%s_%s.bin %s/%s 2> %s/%s/out/%s_%s.txt"%(homepath,binpath,bina,fr,w,h,qp-3,qp+5,f,homepath,outpath,nome,info,yuvpath,yuv,homepath,outpath,nome,info)

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
			linha = "{ time %s/%s/%s --fps=%s/1 -w %s -h %s --min-q=%s --max-q=%s --limit=%s --rt -b 8 -o %s/%s/bin/%s_%s.bin %s/%s ; } 2> %s/%s/out/%s_%s.txt"%(homepath,binpath,bina,fr,w,h,qp-3,qp+5,f,homepath,outpath,nome,info,yuvpath,yuv,homepath,outpath,nome,info)
			
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

if threads != 1:

	file = open("%s/%s/%s"%(homepath,shpath,filename),"r")
	lines = file.readlines()
	tam = len(lines)
	nqp = len(qps)


	for x in range(threads):

		file2 = open("%s/%s/%d_%s"%(homepath,shpath,x+1,filename),"w")
		i = x*nqp
		j=0

		while i < tam:
			
			line = lines[i]
			print >> file2, line
			i = i+1

			if nqp == 4:
				if ((i-1)%4) == 3:
					i = i+threads*(3)
			else:
				j = j+1
				div = tam/threads
				if j == div:
					i = i+threads*div
					j=0
		if gitpull == 1:
			linhag = "cd %s/%s && sh %s.sh"%(homepath,gitpath,gitscript)
			print >> file2, linhag
	file2.close
file.close
