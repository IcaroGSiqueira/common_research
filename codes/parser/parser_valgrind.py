import os
from collections import OrderedDict
import matplotlib.pyplot as plt 
import numpy as np 
import time
from sys import argv

enc_steps_dict_HM = {}
enc_steps_dict_HM['Intra Search'] = ['estIntraPredLumaQT>xGetHADs']
enc_steps_dict_HM['Inter FME Search'] = ['xPatternRefinement']
enc_steps_dict_HM['Inter FME Interp. Half'] = ['xExtDIFUpSamplingH']
enc_steps_dict_HM['Inter FME Interp. Quarter'] = ['xExtDIFUpSamplingQ']
enc_steps_dict_HM['Inter IME Search TZ'] = ['xPatternSearchFast']
enc_steps_dict_HM['Inter IME Search Bipred.'] = ['xPatternSearch']
enc_steps_dict_HM['Inter IME AMVP'] = ['xEstimateMvPredAMVP']
enc_steps_dict_HM['Inter Merge'] = ['xCheckRDCostMerge2Nx2N>encodeResAndCalcRdInterCU']
enc_steps_dict_HM['Inter MC'] = ['motionCompensation']
enc_steps_dict_HM['Transforms T'] = ['xT','xTransformSkip']
enc_steps_dict_HM['Transforms IT'] = ['xIT']
enc_steps_dict_HM['Quantization Q'] = ['xQuant']
enc_steps_dict_HM['Quantization IQ'] = ['xDeQuant']
enc_steps_dict_HM['Filter SAO'] = ['SAOProcess']
enc_steps_dict_HM['Filter Deblock'] = ['xDeblockCU']
enc_steps_dict_HM['Entropy'] = ['estimateBit']

enc_steps_dict_VTM = {}
#enc_steps_dict_VTM['Intra Search'] = ['estIntraPredLumaQT>xGetHADs', 'estIntraPredLumaQT>xGetHADs_SIMD']
enc_steps_dict_VTM['Intra Search'] = ['RdCost::xGetHADs', 'RdCost::xGetHADs_SIMD']
enc_steps_dict_VTM['Inter FME Search'] = ['xPatternRefinement']
enc_steps_dict_VTM['Inter FME Interp. Half'] = ['xExtDIFUpSamplingH']
enc_steps_dict_VTM['Inter FME Interp. Quarter'] = ['xExtDIFUpSamplingQ']
enc_steps_dict_VTM['Inter IME Search TZ'] = ['xPatternSearchFast']
enc_steps_dict_VTM['Inter IME Search Bipred.'] = ['xPatternSearch']
enc_steps_dict_VTM['Inter IME AMVP'] = ['xEstimateMvPredAMVP']
enc_steps_dict_VTM['Inter Merge'] = ['xCheckRDCostMerge2Nx2N>xEncodeInterResidual']
enc_steps_dict_VTM['Inter MC'] = ['motionCompensation']
enc_steps_dict_VTM['Transforms T'] = ['xT','xTransformSkip']
enc_steps_dict_VTM['Transforms IT'] = ['xIT']
enc_steps_dict_VTM['Quantization Q'] = ['xQuant']
enc_steps_dict_VTM['Quantization IQ'] = ['xDeQuant']
enc_steps_dict_VTM['Filter SAO'] = ['SAOProcess']
enc_steps_dict_VTM['Filter Deblock'] = ['xDeblockCU']
enc_steps_dict_VTM['Entropy'] = ['getCtx']



enc_steps_dict_HM = {}
enc_steps_dict_HM['Intra Search'] = ['estIntraPredLumaQT>xGetHADs']
enc_steps_dict_HM['FME Search'] = ['xPatternRefinement']
enc_steps_dict_HM['FME Interp.'] = ['xExtDIFUpSamplingH','xExtDIFUpSamplingQ']
enc_steps_dict_HM['IME Search'] = ['xPatternSearchFast','xPatternSearch']
enc_steps_dict_HM['AMVP/Merge'] = ['xEstimateMvPredAMVP','xCheckRDCostMerge2Nx2N>encodeResAndCalcRdInterCU']
enc_steps_dict_HM['MC'] = ['motionCompensation']
enc_steps_dict_HM['T/IT'] = ['xT','xTransformSkip','xIT']
enc_steps_dict_HM['Q/IQ'] = ['xQuant','xDeQuant']
#enc_steps_dict_HM['Filter'] = ['SAOProcess','xDeblockCU']
#enc_steps_dict_HM['Entropy'] = ['estimateBit']

enc_steps_dict_VTM = {}
#enc_steps_dict_VTM['Intra Search'] = ['estIntraPredLumaQT>xGetHADs', 'estIntraPredLumaQT>xGetHADs_SIMD']
enc_steps_dict_VTM['Intra Search'] = ['RdCost::xGetHADs', 'RdCost::xGetHADs_SIMD']
enc_steps_dict_VTM['FME Search'] = ['xPatternRefinement']
enc_steps_dict_VTM['FME Interp.'] = ['xExtDIFUpSamplingH','xExtDIFUpSamplingQ']
enc_steps_dict_VTM['IME Search'] = ['xPatternSearchFast','xPatternSearch']
enc_steps_dict_VTM['AMVP/Merge'] = ['xEstimateMvPredAMVP','xCheckRDCostMerge2Nx2N>xEncodeInterResidual']
enc_steps_dict_VTM['MC'] = ['motionCompensation']
enc_steps_dict_VTM['T/IT'] = ['xT','xTransformSkip','xIT']
enc_steps_dict_VTM['Q/IQ'] = ['xQuant','xDeQuant']
#enc_steps_dict_VTM['Filter'] = ['SAOProcess','xDeblockCU']
#enc_steps_dict_VTM['Entropy'] = ['getCtx']

def save_comparison_fig(enc_time_dicts,seq, qp):


	fig = plt.figure(figsize=(9,3))
	for key in enc_time_dicts[seq][qp]["HM 16.9"].keys():
		if key not in enc_time_dicts[seq][qp]["VTM 4.0.1"].keys():
			del enc_time_dicts[seq][qp]["HM 16.9"][key] 
	print enc_time_dicts[seq][qp]["HM 16.9"].keys(), enc_time_dicts[seq][qp]["VTM 4.0.1"].keys()
	
	y_hm = np.asarray(enc_time_dicts[seq][qp]["HM 16.9"].values())/float(10**9)
	y_vtm = np.asarray(enc_time_dicts[seq][qp]["VTM 4.0.1"].values())/float(10**9)
	#y_vtm_noSIMD = np.asarray(enc_time_dicts[seq]["VTM 1.1 (no SIMD)"].values())/float(10**9)
	x = np.arange(len(enc_time_dicts[seq][qp]["HM 16.9"].values()))

	w = 0.3
	plt.bar(x, y_hm, label = 'HM 16.9', width = w, color='gold', edgecolor='k')
	plt.bar(x+w, y_vtm, label = 'VTM 4.0.1', width = w, color='turquoise', edgecolor='k')
	#plt.bar(x+2*w, y_vtm_noSIMD, label = 'VTM 1.1 (no SIMD)', width = w, color = 'midnightblue', alpha=1, edgecolor='k')
	plt.xticks(x+w,  enc_time_dicts[seq][qp]["HM 16.9"].keys())

	plt.ylabel(r'Cycle Estimate ($\times 10^9$)')
	plt.legend()

	#add_percentage_labels(x, x+w, x+2*w, y_hm, y_vtm, y_vtm_noSIMD)

	#plt.text(-0.2, max(y_vtm_noSIMD)-20, seq + '@QP' + qp, bbox = {'fc':'white','ec':'k'})
	millis = int(round(time.time() * 1000))

	plt.tight_layout()
	fig.savefig('fig_enc_compare_%s_%s_%d.pdf' % (seq,qp,millis) )


def add_percentage_labels(x1,x2,x3,y1,y2,y3):
	y1pct = y1/np.sum(y1)
	y2pct = y2/np.sum(y2)
	y3pct = y3/np.sum(y3)

	for idx in range(len(x)):
		x_1 = x1[idx]
		x_2 = x2[idx]
		x_3 = x3[idx]

		y_1 = y1[idx] + 20
		y_2 = y2[idx] + 20
		y_3 = y3[idx] + 20

		z_1 = y1pct[idx]
		z_2 = y2pct[idx]
		z_3 = y3pct[idx]

		# if (abs(y_1 - y_2) < 70) or (abs(y_3 - y_2) < 70):
		# 	y_2 = max(y_1,y_2) + 70
		# if  (abs(y_3 - y_2) < 70):
		# 	y_3 = max(y_2,y_3) + 70

		#plt.text(x_1,y_1,'%2.0f%%' % (z_1*100), ha = 'center', weight = 'normal', size = 9, bbox={'fc':'white'})
		#plt.text(x_2,y_2,'%2.0f%%' % (z_2*100), ha = 'center', weight = 'normal', size = 9, bbox={'fc':'white'})
		#plt.text(x_3,y_3,'%2.0f%%' % (z_3*100), ha = 'center', weight = 'normal', size = 9, bbox={'fc':'white'})
		plt.text(x_1,y_1,'%2.0f%%' % (z_1*100), ha = 'center', va = 'bottom',weight = 'normal', rotation=90)
		plt.text(x_2,y_2,'%2.0f%%' % (z_2*100), ha = 'center', va = 'bottom',weight = 'normal', rotation = 90)
		plt.text(x_3,y_3,'%2.0f%%' % (z_3*100), ha = 'center', va = 'bottom', weight = 'normal', rotation = 90)


def parse_callgrind_output(path, enc_steps_dict):
	global not_found
	f = open(path, "r")
	lines = f.readlines()
	f.close()
	enc_time_dict = {}

	while 'file:function' not in lines[0]:
		if 'PROGRAM TOTALS' in lines[0]:
			program_totals = float(lines[0].split()[0].replace(',',''))

		lines.pop(0)

	lines.pop(0)
	lines.pop(0)
	total_calls = 0

	for idx in range(len(lines)):
		line = lines[idx]
		if line.split() == []: continue
		if '---' in line: break 

		line = line.replace('unsigned int ', '')

		func_calls, func_type, func = line.split()[0:3]
		func_calls = float(func_calls.replace(',',''))
		func = func.split('/')[-1].split('(')[0].split('<')[0].split('>')[-1].split(':')[-1]
		if func_type == '<':
			idx_child = idx
			child_found = False
			while not child_found:
				line = lines[idx_child]
				line = line.replace('unsigned int ', '')

				child_calls, child_type, child_func = line.split()[0:3]
				if child_type == '*':
					child_found = True
					child_func = child_func.split('/')[-1].split('(')[0].split('<')[0].split('>')[-1].split(':')[-1]
					child_calls = float(child_calls.replace(',',''))

				idx_child += 1
			func = func + '>' + child_func
		

		found = False


		for enc_step in enc_steps_dict.keys():
			if func in enc_steps_dict[enc_step]:
				if enc_step not in enc_time_dict.keys():
					enc_time_dict[enc_step] = 0

				enc_time_dict[enc_step] += func_calls
				#enc_time_dict[enc_step][1] += [func]
				total_calls += func_calls

				found = True
			# elif child_func in enc_steps_dict[enc_step]:
			# 	if enc_step not in enc_time_dict.keys():
			# 		enc_time_dict[enc_step] = [[],[]]
			# 	print child_func, 'child'

			# 	enc_time_dict[enc_step][0] += [child_calls]
			# 	enc_time_dict[enc_step][1] += [child_func]

		if not found:
			if func not in not_found.keys():
				not_found[func] = 0

			not_found[func] += func_calls

	print 'Total program', program_totals
	print 'Total accounted', total_calls, total_calls/program_totals

	return enc_time_dict

not_found = {}

#fout_VTM = open('cg_annotated_vtm.csv','w')
#fout_HM = open('cg_annotated_hm.csv','w')
#fout_VTM_noSIMD = open('cg_annotated_vtm_noSIMD.csv','w')

cg_files = [_ for _ in os.listdir('./') if '_annotated' not in _ and '_valg' in _ and 'Party' in _]
seqs = []
	
enc_time_dicts = {}

for cg_file in cg_files:

	a,qpp = cg_file.split("_qp")
	qp,r = qpp.split("_y")

	fout = open('cg_annotated_qp'+qp+'.csv','w')

	cg_file_annotated = cg_file + '_annotated'
	if 'vtm' in cg_file:
		enc_steps_dict = enc_steps_dict_VTM		
		mode = 'VTM 4.0.1'
	else:
		enc_steps_dict = enc_steps_dict_HM
		mode = 'HM 16.9'

	os.system('callgrind_annotate --threshold=99.999 --auto=yes --inclusive=yes --tree=caller %s > %s' % (cg_file, cg_file_annotated))
	seq = '%s(%s)' % tuple(cg_file.split('_')[0:2])
	if seq not in seqs:
		seqs.append(seq)
		enc_time_dicts[seq] = {}
	if qp not in enc_time_dicts[seq].keys():
		enc_time_dicts[seq][qp] = {}

	print cg_file
	d = parse_callgrind_output(cg_file_annotated, enc_steps_dict)
	d = OrderedDict(sorted(d.items(), key=lambda t: t[0]))

	enc_time_dicts[seq][qp][mode] = d

for qp in ["22","27","32","37"]:
	save_comparison_fig(enc_time_dicts, 'PartyScene(832x480)', qp)

	
print seqs
for seq in seqs:
	print >> fout, '%s,%s,%s' % (seq, "HM 16.9","VTM 4.0.1")
	for step in enc_time_dicts[seq][qp]["HM 16.9"].keys():
		print >> fout, '%s,%f,' % (step, enc_time_dicts[seq][qp]["HM 16.9"][step]),
		print >> fout, '%f' % (enc_time_dicts[seq][qp]["VTM 4.0.1"][step])
fout.close()


#save_complexity_share_fig(enc_time_dicts, "BQSquare")

