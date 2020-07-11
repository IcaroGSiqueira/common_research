import os
yuvs = os.listdir("/home/icaro/origCfP")
f=60
file = open("run_vg.sh","w")
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
		linhaH = "cd /home/icaro/HM-16.9/bin/         && valgrind --tool=callgrind --callgrind-out-file=/home/icaro/Documents/valgrindTests/%s_hm_valg  ./hm_16_9_valgrind -c ../cfg/encoder_randomaccess_main.cfg  --InputFile=/home/icaro/origCfP/%s --SourceHeight=%s --SourceWidth=%s -f %s -fr %s -q %s " %(nome,yuv,h,w,f,fr,qp)
		print >> file, linhaH
	for qp in [37,32,27,22]:
		if "crop" in yuv:
			vid,pix,fr,y = yuv.split("_")
			nome = vid+"_"+pix+"_"+fr+"_qp%s_"%(qp)+y
		else:
			vid,pix,fps = yuv.split("_")
			fr,y = fps.split(".")
			nome = vid+"_"+pix+"_"+fr+"_qp%s_"%(qp)+y
		linhaV = "cd /home/icaro/VVCSoftware_VTM/bin/ && valgrind --tool=callgrind --callgrind-out-file=/home/icaro/Documents/valgrindTests/%s_vtm_valg ./EncoderAppStatic -c ../cfg/encoder_randomaccess_vtm.cfg   --InputFile=/home/icaro/origCfP/%s --SourceHeight=%s --SourceWidth=%s -f %s -fr %s -q %s " %(nome,yuv,h,w,f,fr,qp)
		print >> file, linhaV
	#for qp in [37,32,27,22]:
	#	linhaA = "cd /home/icaro/aom/build/ 	        && valgrind --tool=callgrind --callgrind-out-file=/home/icaro/Documents/valgrindTests/%s_aom_valg ./aomenc -p 1 -t 1 --psnr -v --fps=%s/1 -w %s -h %s --min-q=%s --max-q=%s --limit=%s --good --tune=psnr --lag-in-frames=0 --end-usage=q --min-gf-interval=16 --max-gf-interval=16 -b 8 /home/icaro/origCfP/%s" %(nome,fr,w,h,qp-3,qp+5,f,yuv)
	#	print >> file, linhaA
file.close