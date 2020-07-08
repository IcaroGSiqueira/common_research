import math
import os
import numpy as np 

from scipy import ndimage
import matplotlib.pyplot as plt 

numf=32

def sobel(frame):
	sobelFrame = []
	frame = frame.astype(np.int16)
	clip = 1
	h = len(frame)
	w = len(frame[0])
	for x in range(clip,(h-clip)): #clipping some first/last rows
		sobelVet = []
		for y in range(clip,(w-clip)): #clipping cols
			gradV = -(frame[x-1][y-1])-2*(frame[x-1][y])-(frame[x-1][y+1])
			gradV += (frame[x+1][y-1])+2*(frame[x+1][y])+(frame[x+1][y+1])
			gradV /= 8
			
			gradH =  -(frame[x-1][y-1])+(frame[x-1][y+1])
			gradH += -2*(frame[x][y-1])+2*(frame[x][y+1])
			gradH += -(frame[x+1][y-1])+(frame[x+1][y+1])
			gradH /= 8
			
			sobelPixel = math.sqrt((gradV*gradV)+(gradH*gradH))
			sobelVet.append(sobelPixel)
			y += 1
		sobelFrame.append(sobelVet)

	return np.asarray(sobelFrame)

def _sobel(frame):
	dx = ndimage.sobel(frame, 1)  # horizontal derivative
	dy = ndimage.sobel(frame, 0)  # vertical derivative
	sob = ndimage.sobel(frame)
	mag = np.hypot(dx, dy)  # magnitude
	mag *= 255.0 / np.max(mag)  # normalize (Q&D)
	print(mag.shape)
	print(mag)
	print(sob)
	plt.imshow(sob)
	plt.show()
	plt.imshow(frame)
	plt.show()
	return mag


def getYFrame(video,w,h, bit10 = False):
	if bit10:
		frameY = np.fromfile(video, dtype=np.uint16, count=w*h)
		frameU = np.fromfile(video, dtype=np.uint16, count=w*h >> 2)
		frameV = np.fromfile(video, dtype=np.uint16, count=w*h >> 2)
	else:
		frameY = np.fromfile(video, dtype=np.uint8, count=w*h)
		frameU = np.fromfile(video, dtype=np.uint8, count=w*h >> 2)
		frameV = np.fromfile(video, dtype=np.uint8, count=w*h >> 2)

	if len(frameY) == 0: return None
	return frameY.reshape((h,w))

# --- M A I N ------------------------------------------------

#yuv_dir = '/home/grellert/videos/vvc_sets'
#videos = os.listdir(yuv_dir)

outFile_all = open('SITI_all.csv','w')
#print('video;max(SI);max(TI);mean(SI);mean(TI)', file = outFile_all)

outFile_all.write('video;max(SI);max(TI);mean(SI);mean(TI)\n')

videos = ["BasketballDrill_832x480_50.yuv","BasketballDrive_1920x1080_50.yuv","BasketballPass_416x240_50.yuv","PartyScene_832x480_50.yuv","BlowingBubbles_416x240_50.yuv","RaceHorses_416x240_30.yuv","RaceHorses_832x480_30.yuv","BQMall_832x480_60.yuv","BQSquare_416x240_60.yuv","BQTerrace_1920x1080_60.yuv","SlideEditing_1280x720_30.yuv","Cactus_1920x1080_50.yuv","FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv"]

for v in videos:
	if '.yuv' not in v: continue

	print("Video: "+ v)
	
	#video = open(os.path.join(yuv_dir, v),'rb')
	video = open('/videos' + v,'rb')

	w = int((v.split('_')[1]).split('x')[0])
	h =  int((v.split('_')[1]).split('x')[1])
	outFile = open(v.split('_')[0]+'.csv','w')
	
	frame = getYFrame(video,w,h)
	prevFrame = frame
	vetSI = [sobel(frame).std()]
	vetTI = []
	frameIdx = 1
	
	while frame is not None:
		vetSI.append(sobel(frame).std())
		vetTI.append((frame-prevFrame).std())
		
		prevFrame = frame
		frame = getYFrame(video,w,h)

		if frameIdx % 10 == 0:
			print("\tFrame #:",frameIdx)

		if frameIdx > numf:
			break

	video.close()
	vetSI = np.array(vetSI)
	vetTI = np.array(vetTI)

	#print( '%s;SI;TI' % (v),file=outFile)
	#for si, ti in zip(vetSI,vetTI):
	#	print( ';%f;%f' % (si,ti),file=outFile)

	#print ('MAX;%f;%f' % ( vetSI.max(),vetTI.max()), file = outFile)
	#print ('MEAN;%f;%f' % ( vetSI.mean(),vetTI.mean()),file = outFile)
	#print ('%s;%f;%f;%f;%f' % (v, vetSI.max(),vetTI.max(),vetSI.mean(),vetTI.mean()), file = outFile_all)

	#print( '%s;SI;TI' % (v),file=outFile)
	outFile.write('%s;SI;TI\n' % (v))

	for si, ti in zip(vetSI,vetTI):
		#print( ';%f;%f' % (si,ti),file=outFile)
		outFile.write(';%f;%f\n' % (si,ti))

	#print ('MAX;%f;%f' % ( vetSI.max(),vetTI.max()), file = outFile)
	outFile.write('MAX;%f;%f\n' % ( vetSI.max(),vetTI.max()))
	#print ('MEAN;%f;%f' % ( vetSI.mean(),vetTI.mean()),file = outFile)
	outFile.write('MEAN;%f;%f\n' % ( vetSI.mean(),vetTI.mean()))
	#print ('%s;%f;%f;%f;%f' % (v, vetSI.max(),vetTI.max(),vetSI.mean(),vetTI.mean()), file = outFile_all)
	outFile_all.write('%s;%f;%f;%f;%f\n' % (v, vetSI.max(),vetTI.max(),vetSI.mean(),vetTI.mean()))

	outFile.close()
outFile_all.close()
