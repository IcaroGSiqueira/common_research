from bjontegaardhmvtm import bdbr,bdpsnr,plotRDCurves, plotGroupedRDCurves

bdb_m=0;
bdbyuv_m=0;
bdp_m=0;
bdpyuv_m=0;
dt_m=0;
tim=0;

csv_ref = open('/home/icaro/pesquisa_ucpel/output_HM/hm_br-psnr.csv','rb')
csv_test = open('/home/icaro/pesquisa_ucpel/output_HM/hm_6t_br-psnr.csv','rb')
# csv_test = open('/home/icaro/pesquisa_ucpel/hm4taps_br-psnr.csv','rb')
# csv_test = open('/home/icaro/pesquisa_ucpel/hm6taps_br-psnr.csv','rb')
# csv_test = open('/home/icaro/pesquisa_ucpel/hm2taps_br-psnr.csv','rb')

out = open("/home/icaro/pesquisa_ucpel/bd-rate/hm_hm-6t.csv","w")

lines = csv_ref.readlines()
tlines = csv_test.readlines()
tam = len(lines)

print >> out,"YUV","BD-BR_Y","BD-BR_YUV","BD-PSNR_Y","BD-PSNR_YUV","DIF_TIME"


results = {}
results['1920x1080'] = []

resultshq = {}
resultshq['1280x720'] = []

results2k = {}
results2k['2560x1600'] = []

resultssq = {}
resultssq['832x480'] = []

resultslq = {}
resultslq['416x240'] = []



for x in xrange(0,tam):
	if "qp22" in lines[x]:
		print lines[x]
		nome22,y22,u22,v22,yuv22,b22,t22 = lines[x].split(",")
		if "crop" in nome22:
			n,n1,n2,n3,n4,n5,n6,n7,n8 = nome22.split("_")
		else:
			n,n1,n2,n3,n4 = nome22.split("_")
		y22,u22,v22,yuv22,b22,t22 = map(float,[y22,u22,v22,yuv22,b22,t22])
	if "qp27" in lines[x]:
		nome27,y27,u27,v27,yuv27,b27,t27 = lines[x].split(",")
		if "crop" in nome27:
			n,n1,n2,n3,n4,n5,n6,n7,n8 = nome27.split("_")
		else:
			n,n1,n2,n3,n4 = nome27.split("_")
		y27,u27,v27,yuv27,b27,t27 = map(float,[y27,u27,v27,yuv27,b27,t27])
	if "qp32" in lines[x]:
		nome32,y32,u32,v32,yuv32,b32,t32 = lines[x].split(",")
		if "crop" in nome32:
			n,n1,n2,n3,n4,n5,n6,n7,n8 = nome32.split("_")
		else:
			n,n1,n2,n3,n4 = nome32.split("_")
		y32,u32,v32,yuv32,b32,t32 = map(float,[y32,u32,v32,yuv32,b32,t32])
	if "qp37" in lines[x]:
		nome37,y37,u37,v37,yuv37,b37,t37 = lines[x].split(",")
		if "crop" in nome37:
			n,n1,n2,n3,n4,n5,n6,n7,n8 = nome37.split("_")
		else:
			n,n1,n2,n3,n4 = nome37.split("_")
		y37,u37,v37,yuv37,b37,t37 = map(float,[y37,u37,v37,yuv37,b37,t37])

	if "qp22" in tlines[x]:
		nome22t,y22t,u22t,v22t,yuv22t,b22t,t22t = tlines[x].split(",")
		y22t,u22t,v22t,yuv22t,b22t,t22t = map(float,[y22t,u22t,v22t,yuv22t,b22t,t22t])
	if "qp27" in tlines[x]:
		nome27t,y27t,u27t,v27t,yuv27t,b27t,t27t = tlines[x].split(",")
		y27t,u27t,v27t,yuv27t,b27t,t27t = map(float,[y27t,u27t,v27t,yuv27t,b27t,t27t])
	if "qp32" in tlines[x]:
		nome32t,y32t,u32t,v32t,yuv32t,b32t,t32t = tlines[x].split(",")
		y32t,u32t,v32t,yuv32t,b32t,t32t = map(float,[y32t,u32t,v32t,yuv32t,b32t,t32t])
	if "qp37" in tlines[x]:
		nome37t,y37t,u37t,v37t,yuv37t,b37t,t37t = tlines[x].split(",")
		y37t,u37t,v37t,yuv37t,b37t,t37t = map(float,[y37t,u37t,v37t,yuv37t,b37t,t37t])
			 
	if (x%4)==3:
		ref = [[b22,y22,u22,v22,yuv22],[b27,y27,u27,v27,yuv27],[b32,y32,u32,v32,yuv32],[b37,y37,u37,v37,yuv37]]
		
		test = [[b22t,y22t,u22t,v22t,yuv22t],[b27t,y27t,u27t,v27t,yuv27t],[b32t,y32t,u32t,v32t,yuv32t],[b37t,y37t,u37t,v37t,yuv37t]]
		
		ttest = (t22t+t37t+t27t+t32t)/4
		tref = (t22+t37+t27+t32)/4
		dt=tref/ttest

		nome=n+"_"+n1+"_"+n2

		bdb = bdbr(ref,test,1)
		bdbyuv = bdbr(ref,test,4)
		bdp = bdpsnr(ref,test,1) 
		bdpyuv = bdpsnr(ref,test,4) 

		if '1920x1080' in nome:
			results['1920x1080'].append([ref,test, nome])

		if '2560x1600' in nome:
			results2k['2560x1600'].append([ref,test, nome])

		if '832x480' in nome:
			resultssq['832x480'].append([ref,test, nome])

		if '416x240' in nome:
			if "Blow" in nome:
				continue
			if "BQ" in nome:
				continue
			resultslq['416x240'].append([ref,test, nome])

		if '1280x720' in nome:
			resultshq['1280x720'].append([ref,test, nome])

		print >> out,nome,bdb,bdbyuv,bdp,bdpyuv,dt

		plotRDCurves(ref,test,1,"/home/icaro/pesquisa_ucpel/bd-rate/curvas/Curvas_%s_0919.pdf"% n,nome)

		bdb_m = bdb_m + bdb
		bdbyuv_m = bdbyuv_m + bdbyuv
		bdp_m = bdp_m + bdp
		bdpyuv_m = bdpyuv_m + bdpyuv
		dt_m = dt_m + dt
		tim=tim+1

bdb_m = bdb_m/tim
bdbyuv_m = bdbyuv_m/tim
bdp_m = bdp_m/tim
bdpyuv_m = bdpyuv_m/tim
dt_m = dt_m/tim


for group0 in results.keys():
	plotGroupedRDCurves(results[group0],1,"/home/icaro/pesquisa_ucpel/bd-rate/curvas/Curvas_%s.pdf"% group0)

for group1 in resultshq.keys():
	plotGroupedRDCurves(resultshq[group1],1,"/home/icaro/pesquisa_ucpel/bd-rate/curvas/Curvas_%s.pdf"% group1)

for group2 in resultslq.keys():
	plotGroupedRDCurves(resultslq[group2],1,"/home/icaro/pesquisa_ucpel/bd-rate/curvas/Curvas_%s_5.pdf"% group2)

for group3 in resultssq.keys():
	plotGroupedRDCurves(resultssq[group3],1,"/home/icaro/pesquisa_ucpel/bd-rate/curvas/Curvas_%s.pdf"% group3)

for group4 in results2k.keys():
	plotGroupedRDCurves(results2k[group4],1,"/home/icaro/pesquisa_ucpel/bd-rate/curvas/Curvas_%s.pdf"% group4)

print >> out,"AVERAGE:",bdb_m,bdbyuv_m,bdp_m,bdpyuv_m,dt_m

print "DONE!!!"