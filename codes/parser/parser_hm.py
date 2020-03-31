import os

homepath = "/home/icaro"
#homepath = "/home/grellert"

outspath = 'output_HM/local/out'
outpath = 'output_HM'

pathin = "%s/pesquisa_ucpel/%s"%(homepath,outspath)
out = open("%s/pesquisa_ucpel/%s/hm_2t_br-psnr.csv"%(homepath,outpath),"w")

yuvs = sorted(os.listdir("%s"%pathin))

linha = "YUV,Bitrate,Y-PSNR,U-PSNR,V-PSNR,YUV-PSNR,Time"
print >> out, linha

for yuv in yuvs:
	# if "bin" in yuv:
	# 	continue
	if "6taps" in yuv:
		continue
	if "4taps" in yuv:
		continue
	if "8taps" in yuv:
		continue
	file = open("%s/%s"%(pathin,yuv),"r")
	lines = file.readlines()
	line = lines[-1]
	dummy0,time = line.split(":")
	time,dummy1 = time.split("s")
	time = time.strip(" ")
	line = lines[-21]
	dummy2,info = line.split("a")
	info = info.strip(" ")
	br,ypsnr,upsnr,vpsnr,yuvpsnr = info.split("   ")
	yuvpsnr = yuvpsnr[:-1]

	linha = "%s,%s,%s,%s,%s,%s,%s"%(yuv,br,ypsnr,upsnr,vpsnr,yuvpsnr,time)

	print >> out, linha

	out.close

