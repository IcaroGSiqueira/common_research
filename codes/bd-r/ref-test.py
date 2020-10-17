from bjontegaard import bdbr,bdpsnr,plotRDCurves

#homepath = "home/grellert"
homepath = "home/icaro"

csv_ref = open('/home/icaro/output_VTM/vtm-brpsnr (copy).csv','rb')
csv_test = open('/home/icaro/output_VTM/vtm_taps-brpsnr.csv','rb')

# csv_test = open('/home/icaro/pesquisa_ucpel/hm4taps_br-psnr.csv','rb')
# csv_test = open('/home/icaro/pesquisa_ucpel/hm6taps_br-psnr.csv','rb')
# csv_test = open('/home/icaro/pesquisa_ucpel/hm2taps_br-psnr.csv','rb')

out = open("/home/icaro/output_VTM/vtm_vtm-t.csv","w")

out.write("YUV,Resolution,BD-BRate,BD-PSNR_Y,Time_Difference\n")

lines = csv_ref.readlines()
tlines = csv_test.readlines()
tam = len(lines)

for x in range(1,tam):
	nome,frl,qp,opt,y,u,v,yuv,b,t = str(lines[x]).split(",")

	if "22" in str(qp):
		nome22,frl22,qp22,opt22,y22,u22,v22,yuv22,b22,t22 = str(lines[x]).split(",")
		t22,dummy = t22.split("\\")
		b22,y22,u22,v22,yuv22,t22 = list(map(float,[b22,y22,u22,v22,yuv22,t22]))

	if "27" in str(qp):
		nome27,frl27,qp27,opt27,y27,u27,v27,yuv27,b27,t27 = str(lines[x]).split(",")
		t27,dummy = t27.split("\\")
		b27,y27,u27,v27,yuv27,t27 = list(map(float,[b27,y27,u27,v27,yuv27,t27]))

	if "32" in str(qp):
		nome32,frl32,qp32,opt32,y32,u32,v32,yuv32,b32,t32 = str(lines[x]).split(",")
		t32,dummy = t32.split("\\")
		b32,y32,u32,v32,yuv32,t32 = list(map(float,[b32,y32,u32,v32,yuv32,t32]))

	if "37" in str(qp):
		nome37,frl,qp,opt,y37,u37,v37,yuv37,b37,t37 = str(lines[x]).split(",")
		t37,dummy = t37.split("\\")
		b37,y37,u37,v37,yuv37,t37 = list(map(float,[b37,y37,u37,v37,yuv37,t37]))

	if "22" in str(qp):
		nome22t,frl22t,qp22t,opt22t,y22t,u22t,v22t,yuv22t,b22t,t22t = str(tlines[x]).split(",")
		t22t,dummy = t22t.split("\\")
		b22t,y22t,u22t,v22t,yuv22t,t22t = list(map(float,[b22t,y22t,u22t,v22t,yuv22t,t22t]))

	if "27" in str(qp):

		nome27t,frl27t,qp27t,opt27t,y27t,u27t,v27t,yuv27t,b27t,t27t = str(tlines[x]).split(",")
		t27t,dummy = t27t.split("\\")
		b27t,y27t,u27t,v27t,yuv27t,t27t = list(map(float,[b27t,y27t,u27t,v27t,yuv27t,t27t]))

	if "32" in str(qp):

		nome32t,frl32t,qp32t,opt32t,y32t,u32t,v32t,yuv32t,b32t,t32t = str(tlines[x]).split(",")
		t32t,dummy = t32t.split("\\")
		b32t,y32t,u32t,v32t,yuv32t,t32t = list(map(float,[b32t,y32t,u32t,v32t,yuv32t,t32t]))

	if "37" in str(qp):

		nome37t,frl37t,qp37t,opt37t,y37t,u37t,v37t,yuv37t,b37t,t37t = str(tlines[x]).split(",")
		t37t,dummy = t37t.split("\\")
		b37t,y37t,u37t,v37t,yuv37t,t37t = list(map(float,[b37t,y37t,u37t,v37t,yuv37t,t37t]))

	n,n1,n2,n3 = nome.split("_")

	if ((x-1)%4)==3:

		ref = [[b22,y22,u22,v22,yuv22],[b27,y27,u27,v27,yuv27],[b32,y32,u32,v32,yuv32],[b37,y37,u37,v37,yuv37]]

		test = [[b22t,y22t,u22t,v22t,yuv22t],[b27t,y27t,u27t,v27t,yuv27t],[b32t,y32t,u32t,v32t,yuv32t],[b37t,y37t,u37t,v37t,yuv37t]]

		timetest = (t22t+t37t+t27t+t32t)/4
		timeref = (t22+t37+t27+t32)/4
		dt=timeref/timetest

		bdb = bdbr(ref,test,1)
		bdp = bdpsnr(ref,test,1) 
		plotRDCurves(ref,test,1,"/%s/Curva_%s.pdf"%(homepath,n),n)
		linha = "%s,%s,%s,%s,%s\n"%(n,n1,bdb,bdp,dt)
		out.write(linha)