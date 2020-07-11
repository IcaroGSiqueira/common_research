import os
yuvs = os.listdir("../../Videos")
f=50
bina=4
file = open("run_hm2,1.sh","w")
for yuv in yuvs:
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
		linha = "./hm_%staps -c ../cfg/encoder_randomaccess_main.cfg --InputFile=/home/icaro/Videos/%s --SourceHeight=%s --SourceWidth=%s -f %s -fr %s -q %s --BitstreamFile=/home/icaro/Documents/TesteHEVC/%s_%st.bin  > /home/icaro/Documents/TesteHEVCtaps/novos/%s_qp%s_%st_hm_out" %(bina,yuv,h,w,f,fr,qp,nome,bina,yuv,qp,bina)
		print >> file, linha
		file.close