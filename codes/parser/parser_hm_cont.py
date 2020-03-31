import os
out22 = open("/home/icaro/Documents/Parsers/hm_cont224k_out.csv","w")
out27 = open("/home/icaro/Documents/Parsers/hm_cont274k_out.csv","w")
out32 = open("/home/icaro/Documents/Parsers/hm_cont324k_out.csv","w")
out37 = open("/home/icaro/Documents/Parsers/hm_cont374k_out.csv","w")
yuvs = os.listdir("/home/icaro/Documents/TesteHEVCCont/")
i22=0
i27=0
i32=0
i37=0
for yuv in sorted(yuvs):
	cont_dict = {}

	if "bin" in yuv:
		continue
	if "zip" in yuv:
		continue
	x = range(1, 21)
	file = open("/home/icaro/Documents/TesteHEVCCont/%s"%yuv,"r")
	lines = file.readlines()
	file.close()
	for l in x:
		line = lines[-l].strip('\n')
		print line,yuv
		tam,cont = line.split(" ")
		#cont = cont[:-1]
		cont_dict[tam] = cont

		
	conts = ''
	tams = ''
	for tam in sorted(cont_dict.keys()):
		cont = cont_dict[tam]

		conts = conts+","+cont
		tams = ","+tams+","+tam
		linha = "%s,%s"%(yuv,conts)
	if "qp22" in yuv:
		if i22 != 1:
			print >> out22, tams
		print >> out22, linha
		i22=1
	if "qp27" in yuv:
		if i27 != 1:
			print >> out27, tams
		print >> out27, linha
		i27=1
	if "qp32" in yuv:
		if i32 != 1:
			print >> out32, tams
		print >> out32, linha
		i32=1
	if "qp37" in yuv:
		if i37 != 1:
			print >> out37, tams
		print >> out37, linha
		i37=1
out22.close()
out27.close()
out32.close()
out37.close()
