from bjontegaard import bdbr,bdpsnr,plotRDCurves

#homepath = "home/grellert"
homepath = "home/icaro"

csv_ref = open('/home/icaro/pesquisa_ucpel/output_HM/hm_br-psnr.csv','rb')
csv_test = open('/home/icaro/pesquisa_ucpel/output_HM/hm_2t_br-psnr.csv','rb')
# csv_test = open('/home/icaro/pesquisa_ucpel/hm4taps_br-psnr.csv','rb')
# csv_test = open('/home/icaro/pesquisa_ucpel/hm6taps_br-psnr.csv','rb')
# csv_test = open('/home/icaro/pesquisa_ucpel/hm2taps_br-psnr.csv','rb')

out = open("/home/icaro/pesquisa_ucpel/bd-rate/hm_hm-2t.csv","w")

print >> out,"YUV,Resolution,BD-BRate,BD-PSNR_Y,Time_Difference"

lines = csv_ref.readlines()
tlines = csv_test.readlines()
tam = len(lines)

for x in xrange(1,tam):
	if "22qp" in lines[x]:
		print lines[x]

		nome22,b22,y22,u22,v22,yuv22,t22 = lines[x].split(",")
		b22,y22,u22,v22,yuv22,t22 = map(float,[b22,y22,u22,v22,yuv22,t22])

	if "27qp" in lines[x]:

		nome27,b27,y27,u27,v27,yuv27,t27 = lines[x].split(",")
		b27,y27,u27,v27,yuv27,t27 = map(float,[b27,y27,u27,v27,yuv27,t27])

	if "32qp" in lines[x]:

		nome32,b32,y32,u32,v32,yuv32,t32 = lines[x].split(",")
		b32,y32,u32,v32,yuv32,t32 = map(float,[b32,y32,u32,v32,yuv32,t32])

	if "37qp" in lines[x]:

		nome37,b37,y37,u37,v37,yuv37,t37 = lines[x].split(",")
		b37,y37,u37,v37,yuv37,t37 = map(float,[b37,y37,u37,v37,yuv37,t37])

	if "22qp" in tlines[x]:

		nome22t,b22t,y22t,u22t,v22t,yuv22t,t22t = tlines[x].split(",")
		b22t,y22t,u22t,v22t,yuv22t,t22t = map(float,[b22t,y22t,u22t,v22t,yuv22t,t22t])

		if "crop" in tlines[x]:
			n,n1,n2,n3,n4,n5,n6,n7,n8 = nome22t.split("_")
		else:
			n,n1,n2,n3,n4,n5,n6,n7 = nome22t.split("_")

	if "27qp" in tlines[x]:

		nome27t,b27t,y27t,u27t,v27t,yuv27t,t27t = tlines[x].split(",")
		b27t,y27t,u27t,v27t,yuv27t,t27t = map(float,[b27t,y27t,u27t,v27t,yuv27t,t27t])

		if "crop" in tlines[x]:
			n,n1,n2,n3,n4,n5,n6,n7,n8 = nome27t.split("_")
		else:
			n,n1,n2,n3,n4,n5,n6,n7 = nome27t.split("_")

	if "32qp" in tlines[x]:

		nome32t,b32t,y32t,u32t,v32t,yuv32t,t32t = tlines[x].split(",")
		b32t,y32t,u32t,v32t,yuv32t,t32t = map(float,[b32t,y32t,u32t,v32t,yuv32t,t32t])

		if "crop" in tlines[x]:
			n,n1,n2,n3,n4,n5,n6,n7,n8 = nome32t.split("_")
		else:
			n,n1,n2,n3,n4,n5,n6,n7 = nome32t.split("_")

	if "37qp" in tlines[x]:

		nome37t,b37t,y37t,u37t,v37t,yuv37t,t37t = tlines[x].split(",")
		b37t,y37t,u37t,v37t,yuv37t,t37t = map(float,[b37t,y37t,u37t,v37t,yuv37t,t37t])

		if "crop" in tlines[x]:
			n,n1,n2,n3,n4,n5,n6,n7,n8 = nome37t.split("_")
		else:
			n,n1,n2,n3,n4,n5,n6,n7 = nome37t.split("_")

	if ((x-1)%4)==3:

		ref = [[b22,y22,u22,v22,yuv22],[b27,y27,u27,v27,yuv27],[b32,y32,u32,v32,yuv32],[b37,y37,u37,v37,yuv37]]

		test = [[b22t,y22t,u22t,v22t,yuv22t],[b27t,y27t,u27t,v27t,yuv27t],[b32t,y32t,u32t,v32t,yuv32t],[b37t,y37t,u37t,v37t,yuv37t]]

		timetest = (t22t+t37t+t27t+t32t)/4
		timeref = (t22+t37+t27+t32)/4
		dt=timeref/timetest

		bdb = bdbr(ref,test,1)
		bdp = bdpsnr(ref,test,1) 
		plotRDCurves(ref,test,1,"/%s/Curva_%s.pdf"%(homepath,n),n)
		print >> out,n,n1,bdb,bdp,dt