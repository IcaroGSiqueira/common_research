import os

#OPT = 0 # optimizacoes ligadas = 1

pathin = "/home/icaro/output_VTM/test"
out = open("/home/icaro/output_VTM/vtm_taps-brpsnr.csv","w")
#out = open("/home/icaro/output_VTM/local/vtm-noSIMD.csv","w")
#out = open("/home/grellert/testesVVC/vtm-SIMD.csv","w")
yuvs = sorted(os.listdir("%s"%pathin))

linha = "YUV,SETTING,QP,OPT,Y-PSNR,U-PSNR,V-PSNR,YUV-PSNR,BITRATE,TOTAL TIME\n"
#print >> out, linha
out.write(linha)

for yuv in yuvs:
	if "gprof" in yuv:
	#if "vtmSIMD" in yuv:
	#if "vtmSIMD" not in yuv:
		continue
	if ".bin" in yuv:
		continue

	try:
		file = open("%s/%s"%(pathin,yuv),"r")
		lines = file.readlines()
		line = lines[-1]
		dummy,t = line.split(":")
		print(t)
		dummy,t,dummy0 = t.split("]")
		t,dummy = t.split("sec")
		t = t.strip(" ")
		line = lines[-4]
		fl,r = line.split("a")
		r = r.strip(" ")
		br,y,u,v,yuvv = r.split("   ")
		yuvv = yuvv[:-1]

		print(yuv)
	except:
		print("\n Saida Incompleta")

	vid,pix,fr,bit,qp,fl,conf,opt = yuv.split("_")
	bit = bit.strip("bit")
	fr = fr.strip("fps")
	fl = fl.strip("fframes")
	qp = qp.strip("qp")
	opt = opt.strip(".txt")
	nome = vid+"_"+pix+"_"+fr+"fps_"+bit+"bit"
	sett = fl+"framelimt_"+conf

	linha = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(nome,sett,qp,opt,y,u,v,yuvv,br,t)
	out.write(linha)
	out.close
