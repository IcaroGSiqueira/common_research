import os
yuvs = os.listdir("../hm")
f=50
file = open("run_hm.sh","w")
for qp in [22,27,32,37]:
	for yuv in yuvs:
		if ".py" in yuv:
			continue
		if "bit" in yuv:
			continue
		if "crop" in yuv:
			vid,pix,fr,y = yuv.split("_")
			nome = vid+"_"+pix+"_"+fr+"_qp%s_"%(qp)+y
		else:
			vid,pix,fps = yuv.split("_")
			fr,y = fps.split(".")
			nome = vid+"_"+pix+"_"+fr+"_qp%s_"%(qp)+y
		w,h = pix.split("x")
		#print w,h,f,fr,qp
		linha = "./TAppEncoderStatic -c ../cfg/encoder_randomaccess_main.cfg --InputFile=/home/icaro/origCfP/%s --SourceHeight=%s --SourceWidth=%s -f %s -fr %s -q %s --BitstreamFile=/home/icaro/Documents/TesteHEVCCont/%s.bin  > /home/icaro/Documents/TesteHEVCCont/%s_qp%s_hm_out" %(yuv,h,w,f,fr,qp,nome,yuv,qp)
		print >> file, linha
		file.close