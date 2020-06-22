import os

f = 30

gitpull = 1

#[37,32,27,22]

qps = [20,32,43,55]

OPT = 0 # optimizacoes ligadas = 1
gprof = 1

threads = 5 # numero de processos em parelelo

#gitpath = "git_repo/pesquisa_av1"
gitpath = "pesquisa_ucpel/pesquisa_av1"
gitscript = "git_upl"

#shpath = "git_repo/common_research/codes/run-sh/aom"
shpath = "pesquisa_ucpel/pesquisa_av1/common_research/codes/run-sh/aom"
filename = "run_av1.sh"

#yuvs = ["RaceHorses_832x480_30.yuv","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv"] 

yuvs = os.listdir("~/Videos/av1_sets")

#["BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30.yuv"] 														#ClasseD
#["RaceHorses_832x480_30.yuv","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv"] 															#ClasseC
#["FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","SlideEditing_1280x720_30.yuv"] 																						#ClasseE e F
#["Tennis_1920x1080_24.yuv","ParkScene_1920x1080_24.yuv","BasketballDrive_1920x1080_50.yuv","Kimono_1920x1080_24.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv"] 	#ClasseB
#["PeopleOnStreet_2560x1600_30_crop.yuv","Traffic_2560x1600_30_crop.yuv"] 																										#ClasseA

yuvpath = "~/Videos/av1_sets"
outpath = "git_repo/pesquisa_av1/output_av1"
binpath = "av1_pesquisa/bin" #partindo da homepath

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

file = open("~/%s/%s"%(shpath,filename),"w")

try:
	os.system("mkdir ~/%s/"%(outpath))
except:
	pass
try:
	os.system("mkdir ~/%s/bin"%(outpath))
except:
	pass
try:
	os.system("mkdir ~/%s/out"%(outpath))
except:
	pass

if gprof == 1:
	try:
		os.system("mkdir ~/%s/gprof"%(outpath))
	except:
		pass
	try:
		os.system("mkdir ~/%s/gmon"%(outpath))
	except:
		pass

for yuv in yuvs:
	for qp in qps:
		if ".py" in yuv:
			continue

		nome,dummy = yuv.split(".")
		print(yuv)
		vid,pix,fr,fl,bit,yf = yuv.split("_")
		fl = fl.strip("f")
		bit = bit.strip("bit")
		w,h = pix.split("x")
		info = "%sqp_%sfframes_"%(qp,f) + inf

		#qp = map(float,qp) !!--end-usage=q!!--AVALIAR

		if gprof == 1:
			linha = "%s/%s/%s --fps=%s/1 -w %s -h %s --min-q=%s --max-q=%s --limit=%s --rt -b 8 -o %s/%s/bin/%s_%s.bin %s/%s 2> %s/%s/out/%s_%s.txt"%(homepath,binpath,bina,fr,w,h,qp-3,qp+5,f,homepath,outpath,nome,info,yuvpath,yuv,homepath,outpath,nome,info)

			linha2 = "mv %s/%s/gmon.out %s/%s/gmon/gmon_%s_%s.out"%(homepath,shpath,homepath,outpath,nome,info)

			linha3 = "gprof %s/%s/%s %s/%s/gmon/gmon_%s_%s.out > %s/%s/gprof/%s_%s.txt"%(homepath,binpath,bina,homepath,outpath,nome,info,homepath,outpath,nome,info)

			linha4 =  "echo \"%s_%s DONE!\"\n"%(nome,info)

			#VERIFICAR SOBRESCRICAO
			try:
				test = open("%s/%s/out/%s_%s.txt"%(homepath,outpath,nome,info),"r")
				tlines = test.readlines()
				tline = tlines[-1]
				if "Total Time" not in tline:
					file.write(linha + " && " + linha2 + " && " + linha3 + " && " + linha4)
			except:
				file.write(linha + " && " + linha2 + " && " + linha3 + " && " + linha4)
		else:
			linha = "{ time %s/%s/%s --fps=%s/1 -w %s -h %s --min-q=%s --max-q=%s --limit=%s --rt -b 8 -o %s/%s/bin/%s_%s.bin %s/%s ; } 2> %s/%s/out/%s_%s.txt"%(homepath,binpath,bina,fr,w,h,qp-3,qp+5,f,homepath,outpath,nome,info,yuvpath,yuv,homepath,outpath,nome,info)
			c
			linha4 =  "echo \"%s_%s DONE!\"\n"%(nome,info)

			try:
				test = open("%s/%s/out/%s_%s.txt"%(homepath,outpath,nome,info),"r")
				tlines = test.readlines()
				tline = tlines[-1]
				if "Total Time" not in tline:
					file.write(linha + " && " + linha4)
			except:
				file.write(linha + " && " + linha4)

if gitpull == 1:
	linhag = "sh %s/%s/%s.sh\n"%(homepath,gitpath,gitscript)
	file.write(linhag)

	#if threads == 1:
	#	if gitpull == 1:
	# 		linhag = "cd %s/%s && sh %s.sh || true"%(homepath,gitpath,gitscript)
	# 		print >> file, linhag
	#file.close

'''
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
'''