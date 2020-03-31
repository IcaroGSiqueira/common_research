import os
import re

pathin = "/home/icaro/testesVVC/gprof"
#pathin = "/home/grellert/testesHEVC/gprof"
#out = open("/home/grellert/testesHEVC/gprof.csv","w")
out = open("/home/icaro/testesVVC/vtmSIMD_gprof.csv","w")
files = sorted(os.listdir("%s"%pathin))

linha = "YUV,FME-Interp.,INT-S.,AMVP,IME-S.,FME-S.,Filter,Merge,I.Quant,I.Transf,MC,Quant,Transf,Affine,Bio,SUM,TOTAL,%"
print >> out, linha

for file in files:
	if "SIMD" not in file:
		continue
	if ".csv" in file:
		continue

	prof = open("%s/%s"%(pathin,file),"r")
	lines = prof.readlines()
	line=0

	FMEINT=0
	Bio=0
	Affine=0
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

	while line != lines[-1]:
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

		linha = re.match(r'\[\d+\][ \d \.]+InterSearch::xPatternSearch',line)
		if linha != None:
			if "Frac" in line:
				continue
			else:
				pt1 = re.findall(r'\d*\.\d*',line)
				p1,selff,called = pt1
				selff = float(selff)
				called = float(called)
				IMES = IMES + selff + called

		#linha = re.match(r'\[\d+\][ \d \.]+InterSearch::xTZSearch',line)
		#if linha != None:
		#	if "Help" in line:
		#		continue
		#	else:
		#		pt1 = re.findall(r'\d*\.\d*',line)
		#		p1,selff,called = pt1
		#		selff = float(selff)
		#		called = float(called)
		#		IMES = IMES + selff + called

		linha = re.match(r'\[\d+\][ \d \.]+[A-Za-z]+::xPatternRefinement',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			FMES = FMES + selff + called

		linha = re.match(r'\[\d+\][ \d \.]+[A-Za-z]+::xExtDIFUpSamplingQ',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			FMEINT = FMEINT + selff + called

		linha = re.match(r'\[\d+\][ \d \.]+[A-Za-z]+::xExtDIFUpSamplingH',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			FMEINT = FMEINT + selff + called

		linha = re.match(r'\[\d+\][ \d \.]+IntraSearch::estIntraPredLumaQT',line)
		if linha != None:
			temp=0
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			INTS = INTS + selff + called
			i+=1
			line = lines[i]
			pt1 = re.findall(r'\d*\.\d*',line)
			selff,called = pt1
			selff = float(selff)
			called = float(called)
			temp = temp + selff + called
			INTS = INTS - temp

		linha = re.match(r'\[\d+\][ \d \.]+InterPrediction::motionCompensation',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			MC = MC + selff + called

		linha = re.match(r'\[\d+\][ \d \.]+InterSearch::xEstimateAffineAMVP',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			AMVP = AMVP + selff + called

		linha = re.match(r'\[\d+\][ \d \.]+InterSearch::xEstimateMvPredAMVP',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			AMVP = AMVP + selff + called



		linha = re.match(r'\[\d+\][ \d \.]+EncCu::xCheckRDCostAffineMerge2Nx2N',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			MRG = MRG + selff + called
			j=i
			TempMC=0
			while "---" not in line:
				j+=1
				line = lines[j]
				if "EncCu::xEncodeInterResidual" in line:
					pt1 = re.findall(r'\d*\.\d*',line)
					selff,called = pt1
					selff = float(selff)
					called = float(called)
					TempMC = TempMC + selff + called
				if "InterPrediction::motionCompensation" in line:
					pt1 = re.findall(r'\d*\.\d*',line)
					selff,called = pt1
					selff = float(selff)
					called = float(called)
					TempMC = TempMC + selff + called
			MRG = MRG - TempMC

		linha = re.match(r'\[\d+\][ \d \.]+EncCu::xCheckRDCostMergeTriangle2Nx2N',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			MRG = MRG + selff + called
			j=i
			TempMC=0
			while "---" not in line:
				j+=1
				line = lines[j]
				if "EncCu::xEncodeInterResidual" in line:
					pt1 = re.findall(r'\d*\.\d*',line)
					selff,called = pt1
					selff = float(selff)
					called = float(called)
					TempMC = TempMC + selff + called
				if "InterPrediction::motionCompensation" in line:
					pt1 = re.findall(r'\d*\.\d*',line)
					selff,called = pt1
					selff = float(selff)
					called = float(called)
					TempMC = TempMC + selff + called
			MRG = MRG - TempMC


		linha = re.match(r'\[\d+\][ \d \.]+IntraSearch::xFracModeBitsIntra',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			INTS = INTS + selff + called

		linha = re.match(r'\[\d+\][ \d \.]+InterSearch::xAffineMotionEstimation',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			Affine = Affine + selff + called

		linha = re.match(r'\[\d+\][ \d \.]+[A-Za-z]+::xCheckRDCostMerge2Nx2N',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			MRG = MRG + selff + called
			j=i
			TempMC=0
			while "---" not in line:
				j+=1
				line = lines[j]
				if "EncCu::xEncodeInterResidual" in line:
					pt1 = re.findall(r'\d*\.\d*',line)
					selff,called = pt1
					selff = float(selff)
					called = float(called)
					TempMC = TempMC + selff + called				
				if "InterPrediction::motionCompensation" in line:
					pt1 = re.findall(r'\d*\.\d*',line)
					selff,called = pt1
					selff = float(selff)
					called = float(called)
					TempMC = TempMC + selff + called
			MRG = MRG - TempMC


		linha = re.match(r'\[\d+\][ \d \.]+TrQuant::xQuant',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			Q = Q + selff + called

		linha = re.match(r'\[\d+\][ \d \.]+TrQuant::xDeQuant',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			IQ = IQ + selff + called

		linha = re.match(r'\[\d+\][ \d \.]+TrQuant::xT',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			T = T + selff + called

		linha = re.match(r'\[\d+\][ \d \.]+TrQuant::xIT',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			IT = IT + selff + called

		linha = re.match(r'\[\d+\][ \d \.]+InterPrediction::applyBiOptFlow',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			Bio = Bio + selff + called

		linha = re.match(r'\[\d+\][ \d \.]+EncSampleAdaptiveOffset::SAOProcess',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			FLT = FLT + selff + called

		linha = re.match(r'\[\d+\][ \d \.]+EncAdaptiveLoopFilter::ALFProcess',line)
		if linha != None:
			pt1 = re.findall(r'\d*\.\d*',line)
			p1,selff,called = pt1
			selff = float(selff)
			called = float(called)
			FLT = FLT + selff + called

	SOMA = FMEINT + INTS + AMVP + IMES + FMES + FLT + MRG + IQ + IT + MC + Q + T + Affine
	PORC = SOMA/TOTAL*100
	linha = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"%(yuv,FMEINT,INTS,AMVP,IMES,FMES,FLT,MRG,IQ,IT,MC,Q,T,Affine,Bio,SOMA,TOTAL,PORC)
	print >> out, linha
	out.close

#linha = "Average,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"%(yuv,FMEINT,INTS,AMVP,IMES,FMES,FLT,MRG,IQ,IT,MC,Q,T,SOMA,TOTAL,PORC)
#print out, linha
#out.close