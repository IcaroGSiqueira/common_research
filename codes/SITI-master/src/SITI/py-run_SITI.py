import os


#yuvs = ["BasketballPass_416x240_50fps_8bit_420.yuv","BasketballDrillText_832x480_50fps_8bit_420.yuv","SlideShow_1280x720_20fps_8bit_420.yuv","Cactus_1920x1080_50fps_8bit_420.yuv","Campfire_3840x2160_30fps_10bit_420.yuv"] #gprofiling

#yuvs = os.listdir("/home/icaro/origCfP")

#yuvs = ["BlowingBubbles_416x240_50.yuv","BQSquare_416x240_60.yuv","BasketballPass_416x240_50.yuv","RaceHorses_416x240_30fps_8bit_420.yuv"] 														#ClasseD
#yuvs = ["RaceHorses_832x480_30fps_8bit_420","BasketballDrill_832x480_50.yuv","BQMall_832x480_60.yuv","PartyScene_832x480_50.yuv"] 																#ClasseC
#yuvs = ["FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv","SlideEditing_1280x720_30.yuv"] 																							#ClasseE e F
#yuvs = ["Tennis_1920x1080_24.yuv","ParkScene_1920x1080_24.yuv","BasketballDrive_1920x1080_50.yuv","Kimono_1920x1080_24.yuv","BQTerrace_1920x1080_60.yuv","Cactus_1920x1080_50.yuv"] 	#ClasseB
#yuvs = ["PeopleOnStreet_2560x1600_30_crop.yuv","Traffic_2560x1600_30_crop.yuv"] 																										#ClasseA

yuvsr = ["BasketballDrill_832x480_50.yuv","BasketballDrive_1920x1080_50.yuv","BasketballPass_416x240_50.yuv","PartyScene_832x480_50.yuv","BlowingBubbles_416x240_50.yuv","RaceHorses_416x240_30.yuv","RaceHorses_832x480_30.yuv","BQMall_832x480_60.yuv","BQSquare_416x240_60.yuv","BQTerrace_1920x1080_60.yuv","SlideEditing_1280x720_30.yuv","Cactus_1920x1080_50.yuv","FourPeople_1280x720_60.yuv","Johnny_1280x720_60.yuv"]	#VVC

yuvs = ["ArenaOfValor_1920x1080_60fps_8bit_420.yuv","KristenAndSara_1280x720_60fps_8bit_420.yuv","BasketballDrillText_832x480_50fps_8bit_420.yuv","MarketPlace_1920x1080_60fps_10bit_420.yuv","Campfire_3840x2160_30fps_10bit_420.yuv","ParkRunning3_3840x2160_50fps_10bit_420.yuv","CatRobot_3840x2160_60fps_10bit_420.yuv","RitualDance_1920x1080_60fps_10bit_420.yuv","DaylightRoad2_3840x2160_60fps_10bit_420.yuv","SlideShow_1280x720_20fps_8bit_420.yuv","FoodMarket4_3840x2160_60fps_10bit_420.yuv","Tango2_3840x2160_60fps_10bit_420.yuv"]
	#VVC

#homepath = "/home/icaro"
#yuvpath = "/home/icaro/Videos"

homepath = "/home/grellert"
yuvpath = "/home/grellert/videos/vvc_sets"

yuvrpath = "/videos"

file = open("run_SITI.sh","w")

for yuvr in yuvsr:
	vid,pix,fr = yuvr.split("_")
	fr = fr.strip("fps")
	nome = vid+"_"+pix+"_"+fr+"fps"

	w,h = pix.split("x")

	linha = "siti -i %s/%s -w %s -h %s \n"%(yuvrpath,yuvr,w,h)
	file.write(linha)

for yuv in yuvs:
	vid,pix,fr,b,dummy = yuv.split("_")
	b = b.strip("bit")
	fr = fr.strip("fps")
	nome = vid+"_"+pix+"_"+fr+"fps"+"_"+b+"bit"

	w,h = pix.split("x")

	linha = "siti -i %s/%s -b %s -w %s -h %s \n"%(yuvpath,yuv,b,w,h)
	file.write(linha)

file.close
