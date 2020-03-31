import os

#homepath = "/home/icaro"
homepath = "/home/grellert"

pathin = "%s/testesHEVC/out/0919"%homepath
out = open("%s/testesHEVC/hm0919.csv"%homepath,"w")

out6t = open("%s/testesHEVC/hm6t0919.csv"%homepath,"w")
out4t = open("%s/testesHEVC/hm4t0919.csv"%homepath,"w")
out2t = open("%s/testesHEVC/hm2t0919.csv"%homepath,"w")

yuvs = sorted(os.listdir("%s"%pathin))

linha = "YUV,Bitrate,Y-PSNR,U-PSNR,V-PSNR,YUV-PSNR,Time"
print >> out, linha
print >> out4t, linha
print >> out2t, linha
print >> out6t, linha

for yuv in yuvs:
	if "bin" in yuv:
		continue
	file = open("%s/%s"%(pathin,yuv),"r")
	lines = file.readlines()
	line = lines[-5]
	a,time = line.split(":")
	t,s = time.split("s")
	t = t.strip(" ")
	line = lines[-25]
	f,r = line.split("a")
	r = r.strip(" ")
	br,yp,up,vp,yuvp = r.split("   ")
	yuvp = yuvp[:-1]

	linha = "%s,%s,%s,%s,%s,%s,%s"%(yuv,br,yp,up,vp,yuvp,t)

	if "4taps" in yuv:
		print >> out4t, linha
	elif "6taps" in yuv:
		print >> out6t, linha
	elif "2taps" in yuv:
		print >> out2t, linha
	else:
		print >> out, linha

	out.close
	out2t.close
	out4t.close
	out6t.close
