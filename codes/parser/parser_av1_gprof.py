import os
import re

#pathin = "/home/icaro/testesVVC/gprof"
pathin = "/home/icaro/pesquisa_ucpel/output_AV1/local/gprof"
out = open("/home/icaro/pesquisa_ucpel/output_AV1/local/gprof.csv","w")
#out = open("/home/icaro/testesVVC/vtm_gprof.csv","w")
files = sorted(os.listdir("%s"%pathin))

#linha = "YUV,Filter,I.Quant,INT-S.,I.Transf,Entpy,Transf,AMVP,IME-S.,Quant,MC,Merge,FME-Interp.,FME-S.,SUM,TOTAL,%"
linha = "YUV,FME-Interp.,FME-S.,Quant,I.Quant,Transf,I.Transf,Filter,INT-S.,ENTPY,AMVP,T/IT,IME-S,Q/IQ,MC,Merge,FME,SUM,TOTAL,%"

print >> out, linha

for file in files:
	#if "SIMD" in file:
	#	continue
	if ".csv" in file:
		continue

	prof = open("%s/%s"%(pathin,file),"r")
	lines = prof.readlines()
	line=0

	FMEINT=0
	Entpy=0
	INTS=0
	AMVP=0
	IMES=0
	FMES=0
	FLT=0
	MRG=0
	IQ=0
	IT=0
	MC=0
	Q=0
	T=0
	i=0

	print file

	yuv = file.strip(".txt")
	yuv = yuv.strip(".yuv")
	yuv = yuv.strip("gprof_")

	i=2500
	while line != lines[-10000]:
		i+=1
		line=lines[i]

		#linha = re.match(r'granularity:',line)
		#if linha != None:
		#		pt1 = re.findall(r'\d*\.\d*',line)
		#		p1,called = pt1
		#		called = float(called)
		#		TOTAL = called
		#		print TOTAL

		linha = re.match(r'\[1\][\d \.]+main \[1\]',line)
		if linha != None:
				pt1 = re.findall(r'\d*\.\d*',line)
				p1,selff,called = pt1
				called = float(called)
				TOTAL = called
				print TOTAL

#########################################################################################

		linha = re.match(r'\[\d+\] [ \d \.\d]+[A-Za-z]+::xCheckRDCostMerge2Nx2N',line)
		if linha != None:
			j=i
			while "---" not in line:
				j+=1
				line = lines[j]
				if "encodeResAndCalcRdInterCU" in line:
					pt1 = re.findall(r'\d*\.\d*',line)
					print pt1
					selff,called = pt1
					selff = float(selff)
					called = float(called)
					MRG = MRG + selff + called

		linha = re.match(r'\[\d+\] [ \d \.\d]+TComTrQuant::xQuant',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			Q = Q + selff + called

		linha = re.match(r'\[\d+\] [ \d \.\d]+search_txk_type',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			T = T + selff + called

#########################################################################################

	SOMA = FMEINT + INTS + AMVP + IMES + FMES + FLT + MRG + IQ + IT + MC + Q + T
	PORC = SOMA/TOTAL*100

	QIQ = Q + IQ
	TIT = T + IT
	FME = FMES + FMEINT

	linha = "%s,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf"%(yuv,FMEINT,FMES,Q,IQ,T,IT,FLT,INTS,Entpy,AMVP,TIT,IMES,QIQ,MC,MRG,FME,SOMA,TOTAL,PORC)
	print >> out, yuv, linha

#print >> out,"Average", linha2
out.close
#linha = "Average,%s,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f"%(yuv,FLT,IQ,INTS,IT,Entpy,T,AMVP,IMES,Q,MC,MRG,FMEINT,FMES,SOMA,TOTAL,PORC)
#print out, linha
#out.close