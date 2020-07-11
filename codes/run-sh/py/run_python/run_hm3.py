import os
yuvs = os.listdir("../../Videos")
f=50
file = open("run_hm3.sh","w")
for yuv in yuvs:
	for bina in ["2h","4h3q","6h5q"]:
		for qp in [37,32,27,22]:
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
			linha = "./hm_%s -c ../cfg/encoder_randomaccess_main.cfg --InputFile=/home/icaro/Videos/%s --SourceHeight=%s --SourceWidth=%s -f %s -fr %s -q %s --BitstreamFile=/home/icaro/Documents/TesteHEVC/%s_%st.bin  > /home/icaro/Documents/TesteHEVC/tapsnovos/%s_qp%s_%st_hm_out" %(bina,yuv,h,w,f,fr,qp,nome,bina,yuv,qp,bina)
			print >> file, linha
			file.close