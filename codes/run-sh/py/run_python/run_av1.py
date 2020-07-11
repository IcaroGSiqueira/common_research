import os
yuvs = os.listdir("/home/icaro/origCfP")
f=50
file = open("run_av1.sh","w")
for qp in [19,24,29,34]:
	for yuv in yuvs:
		if ".py" in yuv:
			continue
		if "bit" in yuv:
			continue
		if "crop" in yuv:
			vid,pix,fr,y = yuv.split("_")
			nome = vid+"_"+pix+"_"+fr+"_qp%s_"%(qp+3)+y
		else:
			vid,pix,fps = yuv.split("_")
			fr,y = fps.split(".")
			nome = vid+"_"+pix+"_"+fr+"_qp%s_"%(qp+3)+y
		w,h = pix.split("x")
		
		#qp = map(float,qp)
		linha = "./aomenc -p 1 -t 1 --psnr -v --fps=%s/1 -w %s -h %s --min-q=%s --max-q=%s --limit=%s --good --tune=psnr --lag-in-frames=0 --end-usage=q --min-gf-interval=16 --max-gf-interval=16 -b 8 -o /home/icaro/Documents/TesteAV1/%s.bin /home/icaro/origCfP/%s 2> /home/icaro/Documents/TesteAV1/%s_qp%s_av1_out"%(fr,w,h,qp,qp+8,f,nome,yuv,yuv,qp+3)
		print >> file, linha
		file.close