import os

f=30

simd=1
gprof=1

#yuvs = ["BasketballDrill_832x480_50.yuv","BasketballDrive_1920x1080_50.yuv","BasketballPass_416x240_50.yuv","Kimono_1920x1080_24.yuv","BlowingBubbles_416x240_50.yuv","ParkScene_1920x1080_24.yuv","BQMall_832x480_60.yuv","BQSquare_416x240_60.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","PartyScene_832x480_50.yuv","PeopleOnStreet_2560x1600_30_crop.yuv","RaceHorses_416x240_30.yuv","RaceHorses_832x480_30.yuv","Traffic_2560x1600_30_crop.yuv","SlideEditing_1280x720_30.yuv","Tennis_1920x1080_24.yuv"] #SERVIDOR

#yuvs = ["BasketballDrill_832x480_50.yuv","BasketballDrive_1920x1080_50.yuv","BasketballPass_416x240_50.yuv","Kimono_1920x1080_24.yuv","BlowingBubbles_416x240_50.yuv","ParkScene_1920x1080_24.yuv","BQMall_832x480_60.yuv","BQSquare_416x240_60.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","PartyScene_832x480_50.yuv","PeopleOnStreet_2560x1600_30_crop.yuv","RaceHorses_832x480_30.yuv","RaceHorses_416x240_30.yuv","Traffic_2560x1600_30_crop.yuv"] #UCPEL_PC

yuvs = ["ParkScene_1920x1080_24.yuv"]

#yuvs = os.listdir("/home/icaro/origCfP")

#homepath = "/home/grellert"
homepath = "/home/icaro"
#yuvpath = "/videos"
yuvpath = "/home/icaro/origCfP"

file = open("%s/pesquisa_ucpel/codes/run-sh/vtm/run_vtm.sh"%homepath,"w")
for yuv in yuvs:
	for qp in [37,32,27,22]:
		if ".py" in yuv:
			continue
		if "bit" in yuv:
			continue
		if "crop" in yuv:
			vid,pix,fr,y = yuv.split("_")
			nome = vid+"_"+pix+"_"+fr+"_%dqp_"%(qp)+y
		else:
			vid,pix,fps = yuv.split("_")
			fr,y = fps.split(".")
			nome = vid+"_"+pix+"_"+fr+"_%dqp_"%(qp)+y
		w,h = pix.split("x")
		#print w,h,f,fr,qp

		if simd == 1:
			if gprof == 0:
				linha = "{ time %s/vtm6.1/bin/EncoderAppStatic -c %s/vtm6.1/cfg/encoder_randomaccess_vtm.cfg --InputFile=%s/%s --SourceHeight=%s --SourceWidth=%s -f %s -fr %s -q %s --BitstreamFile=%s/testesVVC/bin/%s_%sfr_vtm_SIMD.bin ; } &> %s/testesVVC/out/%s_%dqp_%sf_vtm_SIMD_out" %(homepath,homepath,yuvpath,yuv,h,w,f,fr,qp,homepath,nome,f,homepath,yuv,qp,f)
			elif gprof == 1:
				linha = "%s/vtm6.1/bin/EncoderAppStaticd -c %s/vtm6.1/cfg/encoder_randomaccess_vtm.cfg --InputFile=%s/%s --SourceHeight=%s --SourceWidth=%s -f %s -fr %s -q %s --BitstreamFile=%s/testesVVC/gpbin/%s_%sf_vtm_SIMD.bin > %s/testesVVC/gpout/%s_%dqp_vtm_SIMD_out && mv ./gmon.out %s/pesquisa_ucpel/codes/run-sh/vtm/gmon_%s.out && gprof %s/vtm6.1/bin/EncoderAppStaticd %s/pesquisa_ucpel/codes/run-sh/vtm/gmon_%s.out > %s/testesVVC/gprof/gprof_%s_%dqp_SIMD_vtm.txt" %(homepath,homepath,yuvpath,yuv,h,w,f,fr,qp,homepath,nome,f,homepath,yuv,qp,homepath,nome,homepath,homepath,nome,homepath,yuv,qp)
		elif simd == 0:
			if gprof == 0:
				linha = "{ time %s/vtm6.1_noSIMD/bin/EncoderAppStatic -c %s/vtm6.1_noSIMD/cfg/encoder_randomaccess_vtm.cfg --InputFile=%s/%s --SourceHeight=%s --SourceWidth=%s -f %s -fr %s -q %s --BitstreamFile=%s/testesVVC/bin/%s_%sf_vtm_noSIMD.bin ; }  &> %s/testesVVC/out/%s_%dqp_%sfr_vtm_noSIMD_out" %(homepath,homepath,yuvpath,yuv,h,w,f,fr,qp,homepath,nome,f,homepath,yuv,qp,f)
			elif gprof == 1:
				linha = "%s/vtm6.1_noSIMD/bin/EncoderAppStaticd -c %s/vtm6.1_noSIMD/cfg/encoder_randomaccess_vtm.cfg --InputFile=%s/%s --SourceHeight=%s --SourceWidth=%s -f %s -fr %s -q %s --BitstreamFile=%s/testesVVC/gpbin/%s_%sf_vtm_noSIMD.bin > %s/testesVVC/gpout/%s_%dqp_vtm_noSIMD_out && gprof %s/vtm6.1_noSIMD/bin/EncoderAppStaticd %s/pesquisa_ucpel/codes/run-sh/vtm/gmon.out > %s/testesVVC/gprof/gprof_%s_%dqp_noSIMD_vtm.txt" %(homepath,homepath,yuvpath,yuv,h,w,f,fr,qp,homepath,nome,f,homepath,yuv,qp,homepath,homepath,homepath,yuv,qp)

		#linha = "%s/vtm6.1/bin/EncoderAppStatic_std -c %s/vtm6.1/cfg/encoder_randomaccess_vtm.cfg --InputFile=%s/%s --SourceHeight=%s --SourceWidth=%s -f %s -fr %s -q %s --BitstreamFile=%s/testesVVC/bin/%s_%sfr_vtm_orig.bin > %s/testesVVC/out/%s_qp%s_%sf_vtm_orig_out" %(homepath,homepath,yuvpath,yuv,h,w,f,fr,qp,homepath,nome,f,homepath,yuv,qp,f) #ORIGINAL

		print >> file, linha
		file.close