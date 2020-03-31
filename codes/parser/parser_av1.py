import os
out = open("/home/icaro/Documents/Parsers/av1_out.csv","w")
yuvs = os.listdir("./")
for vid in yuvs:
	if "bin" in vid:
		continue
	if ".py" in vid:
		continue
	if ".csv" in vid:
		continue
	file = open("/home/icaro/Documents/TesteAV1/%s"%vid,"r")
	lines = file.readlines()
	line = lines[-1]
	r,l = line.split(") ")
	v,t = l.split("bps")
	yuv,avg,y,u,v,br,a = v.split(" ")
	a,b,t,c = t.split(" ")
	linha = "%s,%s,%s,%s,%s,%s,%s"%(vid,y,u,v,yuv,br,t)
	print >> out, linha
	out.close