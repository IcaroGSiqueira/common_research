import os

f=5
simd=0 #vtm

#yuvs = {"BasketballDrill_832x480_50.yuv","BasketballDrive_1920x1024_50.yuv","BasketballDrive_1920x1080_50.yuv","BasketballPass_416x240_50.yuv","Kimono_1920x1080_24.yuv","BlowingBubbles_416x240_50.yuv","ParkScene_1920x1080_24.yuv","BQMall_832x480_60.yuv","BQSquare_416x240_60.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","PartyScene_832x480_50.yuv","PeopleOnStreet_2560x1600_30_crop.yuv","RaceHorses_416x240_30.yuv","RaceHorses_832x480_30.yuv","Traffic_2560x1600_30_crop.yuv","SlideEditing_1280x720_30.yuv","Tennis_1920x1080_24.yuv"}

yuvs = {"BQSquare_416x240_60.yuv"}

#homepath = "/home/grellert"
homepath = "/home/icaro"
#yuvpath = "/workareas/share/video_sequences"
yuvpath = "/home/icaro/origCfP"

file = open("../run_vg.sh","w")
for yuv in yuvs:
	for qp in [37,32,27,22]:
		if "crop" in yuv:
			vid,pix,fr,y = yuv.split("_")
			nome = vid+"_"+pix+"_"+fr+"_qp%s_"%(qp)+y
		else:
			vid,pix,fps = yuv.split("_")
			fr,y = fps.split(".")
			nome = vid+"_"+pix+"_"+fr+"_qp%s_"%(qp)+y
		w,h = pix.split("x")
		#print w,h,fr,qp,nome
		linhaH = "cd %s/pesquisa_ucpel/HM-16.9_fme_aprox/bin/ && valgrind --tool=callgrind --callgrind-out-file=%s/testesHEVC/%s_hm_valg  ./hm_16_9_valgrind -c ../cfg/encoder_randomaccess_main.cfg  --InputFile=%s/%s --SourceHeight=%s --SourceWidth=%s -f %s -fr %s -q %s " %(homepath,homepath,nome,yuvpath,yuv,h,w,f,fr,qp)
		print >> file, linhaH

	# for qp in [37,32,27,22]:
	# 	if "crop" in yuv:
	# 		vid,pix,fr,y = yuv.split("_")
	# 		nome = vid+"_"+pix+"_"+fr+"_qp%s_"%(qp)+y
	# 	else:
	# 		vid,pix,fps = yuv.split("_")
	# 		fr,y = fps.split(".")
	# 		nome = vid+"_"+pix+"_"+fr+"_qp%s_"%(qp)+y
	# 	if simd == 1:
	# 		linhaV = "cd %s/pesquisa_ucpel/VTM_5.0/bin/ && valgrind --tool=callgrind --callgrind-out-file=%s/testesVVC/%s_vtm_valg ./EncoderAppStatic -c ../cfg/encoder_randomaccess_vtm.cfg   --InputFile=%s/%s --SourceHeight=%s --SourceWidth=%s -f %s -fr %s -q %s " %(homepath,homepath,nome,yuvpath,yuv,h,w,f,fr,qp)
	# 	else:
	# 		linhaV = "cd %s/pesquisa_ucpel/VTM_5.0_noSIMD/bin/ && valgrind --tool=callgrind --callgrind-out-file=%s/testesVVC/%s_vtm_valg ./EncoderAppStatic -c ../cfg/encoder_randomaccess_vtm.cfg   --InputFile=%s/%s --SourceHeight=%s --SourceWidth=%s -f %s -fr %s -q %s " %(homepath,homepath,nome,yuvpath,yuv,h,w,f,fr,qp)
	# 	print >> file, linhaV
file.close