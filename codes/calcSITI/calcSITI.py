import math
import os

numf=32

def sobel(frame):
	sobelFrame = []
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
	return sobelFrame

def diff(frame1,frame2):
	diffFrame = []
	h = len(frame)
	w = len(frame[0])
	for x in range(0,h):
		row = list(a - b for a,b in zip(frame1[x],frame2[x]))
		diffFrame.append(row)
	return diffFrame

def std(frame):
	h = len(frame)
	w = len(frame[0])
	# 1 - calc avg pixel
	frameSum = 0
	for row in frame:
		frameSum += sum(row)
	avg = frameSum/(h*w)
	
	# 2 - accumulate squared diff
	acum = 0
	for row in frame:
		for pixel in row:
			acum += pow(pixel-avg,2)

	return math.sqrt(acum/(w*h))


def getYFrame(video,w,h):
	frames = []
	res = w*h
	frame = []
	for i in range(0,h):
		row = []
		for j in range(0,w):
			pixel = video.read(1)
			if not(pixel): #EOF
				return False
			row.append(ord(pixel))
		frame.append(row)
	return frame

# --- M A I N ------------------------------------------------

#["BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30.yuv","RaceHorses_832x480_30.yuv","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv","BasketballDrillText_832x480_50.yuv","SlideShow_1280x720_20.yuv","SlideEditing_1280x720_30.yuv","ArenaOfValor","BasketballDrive_1920x1080_50.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv","MarketPlace","RitualDance","Tango2","FoodMarket4","Campfire","CatRobot","DaylightRoad2","ParkRunning3"]		

yuvs = ["BlowingBubbles_416x240_50fps_8bit_420.yuv","BQSquare_416x240_60fps_8bit_420.yuv","BasketballPass_416x240_50fps_8bit_420.yuv","RaceHorses_416x240_30fps_8bit_420.yuv","RaceHorses_832x480_30fps_8bit_420.yuv","BasketballDrill_832x480_50fps_8bit_420.yuv","BQMall_832x480_60fps_8bit_420.yuv","PartyScene_832x480_50fps_8bit_420.yuv","BasketballDrillText_832x480_50fps_8bit_420.yuv","SlideShow_1280x720_20fps_8bit_420.yuv","SlideEditing_1280x720_30fps_8bit_420.yuv","BasketballDrive_1920x1080_50fps_8bit_420.yuv","BQTerrace_1920x1080_60fps_8bit_420.yuv","Cactus_1920x1080_50fps_8bit_420.yuv","ArenaOfValor_1920x1080_60_8bit_420.yuv","MarketPlace_1920x1080_60fps_10bit_420.yuv","RitualDance_1920x1080_60fps_10bit_420.yuv","Campfire_3840x2160_30fps_8bit_420.yuv","Tango2_3840x2160_60fps_10bit_420.yuv","DaylightRoad2_3840x2160_60fps_10bit_420.yuv","ParkRunning3_3840x2160_50fps_10bit_420.yuv"]#,"FoodMarket4_3840x2160_60fps_10bit_420.yuv","CatRobot_3840x2160_60fps_10bit_420.yuv"] 

#yuvs = os.listdir("/home/icaro/origCfP/")

# try:
# 	outAvgFile = open('SITI_AVG.csv','r')
# 	lines = outAvgFile.readlines()
# 	outAvgFile = open('SITI_AVG.csv','w')
# 	for i in range(len(lines)):
# 		print >> outAvgFile, lines[i]
# except:
# 	outAvgFile = open('SITI_AVG.csv','w')
		
for v in yuvs:
	print "SITI Calc: ", v
	if '.py' in v:
		continue
	if '.csv' in v:
		continue
	if '10bit' in v:
		continue
	video = open('/home/icaro/origCfP/' + v,'rb')
	w = int((v.split('_')[1]).split('x')[0])
	h = int((v.split('_')[1]).split('x')[1].split('.')[0])

	try:
		outFile = open(v+'.csv','r')

	except:
		siavg=0
		tiavg=0
		outFile = open(v+'.csv','w')
		frame = getYFrame(video,w,h)
		prevFrame = frame
		vetSI = [std(sobel(frame))]
		vetTI = []
		frameIdx = 1
		
		while frame:
			vetSI.append(std(sobel(frame)))
			vetTI.append(std(diff(prevFrame,frame)))
			prevFrame = frame
			if frameIdx % 10 == 0:
				print "\tFrame #:",frameIdx
			frameIdx += 1
			frame = getYFrame(video,w,h)
			if frameIdx > numf:
				break
		video.close()

		print >> outFile, v,';SI;TI'
		for si, ti in zip(vetSI,vetTI):
			print >> outFile,';',si,';',ti
			siavg=siavg+si
			tiavg=tiavg+ti
		print >> outFile, 'MAX;', max(vetSI), ';', max(vetTI)
		print >> outFile, 'AVG;', siavg/numf, ';', tiavg/numf
		outFile.close()
print "\nDONE!!!\n"

# --- P A R S E ------------------------------------------------

outAvgFile = open('SITI_AVG.csv','w')
print >> outAvgFile, 'YUVS;SI;TI'
sitis = os.listdir("./")
for siti in sitis:
	if '.py' in siti:
		continue
	if '.png' in siti:
		continue
	if 'SITI_AVG.csv' in siti:
		continue	
	print "Avg Calc: ", siti
	file = open("./%s"%siti,'r')
	lines = file.readlines()
	line = lines[-1]
	line1 = line.split(';')[1]
	line2 = line.split(';')[2]
	line2 = line2.strip('\n')
	print >> outAvgFile, siti, ';', line1, ';', line2

outAvgFile.close()
print "\nDONE!!!\n"


# --- S C A T T E R ------------------------------------------------


import pandas as pd
import  matplotlib.pyplot as plt
#from StringIO import StringIO

sstr = open('SITI_AVG.csv','r')

# sstr = StringIO("""YUVS	SI	TI
# BasketballDrill_832x480_50.yuv	8.28554838896	40.4969134626
# BasketballDrive_1920x1080_50.yuv	5.53605638081235	39.3533488924529
# BasketballPass	9.05520407629	36.3455636908
# BlowingBubbles	8.56374544757	61.7980582219
# BQMall_832x480_60.yuv	11.1710822008	54.9636243346
# BQSquare	20.0019046057	91.7932459389
# BQTerrace_1920x1080_60.yuv	11.3562721827747	81.6378013137765
# Cactus_1920x1080_50.yuv	6.94960086193039	70.9861379517921
# Kimono_1920x1080_24.yuv	2.78899414696	47.3708771293
# ParkJoy_3840x2160_50.yuv	5.42938442302922	59.5845068123667
# ParkScene_1920x1080_24.yuv	5.37725782900353	54.242118571351
# PartyScene_832x480_50.yuv	12.862781892	57.9137289423
# PeopleOnStreet_2560x1600_30_crop.yuv	8.60799421455392	66.8918880517157
# RaceHorses	9.59908959484	52.1056618805
# Traffic_2560x1600_30_crop.yuv	6.64494985360274	57.6850642312902
# FourPeople_1280x720_60.yuv	7.46208191589921	61.6236052476706
# Johnny	7.06431549011	57.8705451849
# Tennis	4.45836315139	59.2368128785
# SlideEditing	26.0431579821	87.0229854694
# """)

df = pd.read_csv(sstr, sep = ';')
df.plot(x = 'SI', y = 'TI', style = 'o')
x = df['SI']
y = df['TI']
l = df['YUVS']
#plt.text(x,y,l)

#for x,y, label in zip(df['SI'],df['TI'], df['YUVS']):
#    plt.text(label, # this is the text
#                 x,y, # this is the point to label
#                 ha='center') # horizontal alignment can be left, right or center

si_mean = df.SI.mean()
ti_mean = df.TI.mean()
plt.axvline(x=si_mean, c = 'k', linestyle = '--')
plt.axhline(y=ti_mean, c = 'k', linestyle = '--')

#for i, txt in enumerate(n):
#    ax.annotate(txt, (SI[i], TI[i]))

plt.show()