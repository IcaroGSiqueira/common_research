import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

image = cv2.imread('entrada.jpeg')
output = "saida"

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#image = cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)
#image = cv2.cvtColor(image, cv2.COLOR_YCR_CB2RGB)
#image = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
#image = cv2.cvtColor(image, cv2.COLOR_YCrCb2BGR)

print ("altura (height): %d pixels" % (image.shape[0]))
print ("largura (width): %d pixels" % (image.shape[1]))
print ("Canais (channels): %d" % (image.shape[2]))

w = image.shape[1]
h = image.shape[0]
d = image.shape[2]

def equacoes(C,B,A,W,D,E,F,G):
	#------ EQUAÇÕES -------
	eq1 = ((0*C) + (1*B) + (-3*A) + (63*W) + (4*D) + (-2*E) + (1*F) + (0*G))>>6
	#--------
	eq2 = ((-1*C) + (2*B) + (-5*A) + (62*W) + (8*D) + (-3*E) + (1*F) + (0*G))>>6
	#---------
	eq3 = ((-1*C) + (3*B) + (-8*A) + (60*W) + (13*D) + (-4*E) + (1*F) + (0*G))>>6
	#---------
	eq4 = ((-1*C) + (4*B) + (-10*A) + (58*W) + (17*D) + (-5*E) + (1*F) + (0*G))>>6
	#---------
	eq5 = ((-1*C) + (4*B) + (-11*A) + (52*W) + (26*D) + (-8*E) + (3*F) + (-1*G))>>6
	#---------
	eq6 = ((-1*C) + (3*B) + (-9*A) + (47*W) + (31*D) + (-10*E) + (4*F) + (-1*G))>>6
	#----------
	eq7 = ((-1*C) + (4*B) + (-11*A) + (45*W) + (34*D) + (-10*E) + (4*F) + (-1*G))>>6
	#---------
	eq8 = ((-1*C) + (4*B) + (-11*A) + (40*W) + (40*D) + (-11*E) + (4*F) + (-1*G))>>6
	#---------
	eq9 = ((-1*C) + (4*B) + (-10*A) + (34*W) + (45*D) + (-11*E) + (4*F) + (-1*G))>>6
	#---------
	eq10 = ((-1*C) + (4*B) + (-10*A) + (31*W) + (47*D) + (-9*E) + (3*F) + (-1*G))>>6
	#---------
	eq11 = ((-1*C) + (3*B) + (-8*A) + (26*W) + (52*D) + (-11*E) + (4*F) + (-1*G))>>6
	#---------
	eq12 = ((0*C) + (1*B) + (-5*A) + (17*W) + (58*D) + (-10*E) + (4*F) + (-1*G))>>6
	#---------
	eq13 = ((0*C) + (1*B) + (-4*A) + (13*W) + (60*D) + (-8*E) + (3*F) + (-1*G))>>6
	#---------
	eq14 = ((0*C) + (1*B) + (-3*A) + (8*W) + (62*D) + (-5*E) + (2*F) + (-1*G))>>6
	#---------
	eq15 = ((0*C) + (1*B) + (-2*A) + (4*W) + (63*D) + (-3*E) + (1*F) + (0*G))>>6

	eq1 = np.clip(eq1,0,255)
	eq2 = np.clip(eq2,0,255)
	eq3 = np.clip(eq3,0,255)
	eq4 = np.clip(eq4,0,255)
	eq5 = np.clip(eq5,0,255)
	eq6 = np.clip(eq6,0,255)
	eq7 = np.clip(eq7,0,255)
	eq8 = np.clip(eq8,0,255)
	eq9 = np.clip(eq9,0,255)
	eq10 = np.clip(eq10,0,255)
	eq11 = np.clip(eq11,0,255)
	eq12 = np.clip(eq12,0,255)
	eq13 = np.clip(eq13,0,255)
	eq14 = np.clip(eq14,0,255)
	eq15 = np.clip(eq15,0,255)

	return (eq1,eq2,eq3,eq4,eq5,eq6,eq7,eq8,eq9,eq10,eq11,eq12,eq13,eq14,eq15)
 
wimage = np.zeros((h,w+6,d), dtype=int)
wimage = np.pad(image, ((0, 0),(3, 3),(0, 0)), 'edge')

horimg = np.zeros(((h),(w*16-15),d), dtype=int)

horhimg = np.zeros((h+6,(w*16-15),d), dtype=int)

finalimg = np.zeros(((h*16-15),(w*16-15),d), dtype=int)

#-----HORIZONTAL-----
for j in range (0, d):
	for r in range(0, h):
		for i in range (3, w+6-4):
			C = wimage[r][i-3][j]
			B = wimage[r][i-2][j]
			A = wimage[r][i-1][j]
			W = wimage[r][i][j]
			D = wimage[r][i+1][j]
			E = wimage[r][i+2][j]
			F = wimage[r][i+3][j]
			G = wimage[r][i+4][j] 

			horimg[r][(i-3)*16][j] = image[r][i-3][j]
			horimg[r][(i-3)*16+1][j], horimg[r][(i-3)*16+2][j],horimg[r][(i-3)*16+3][j], horimg[r][(i-3)*16+4][j], horimg[r][(i-3)*16+5][j], horimg[r][(i-3)*16+6][j], horimg[r][(i-3)*16+7][j], horimg[r][(i-3)*16+8][j], horimg[r][(i-3)*16+9][j], horimg[r][(i-3)*16+10][j], horimg[r][(i-3)*16+11][j], horimg[r][(i-3)*16+12][j], horimg[r][(i-3)*16+13][j], horimg[r][(i-3)*16+14][j], horimg[r][(i-3)*16+15][j] = equacoes(C,B,A,W,D,E,F,G)
		horimg[r][w*16-16][j] = image[r][w-1][j]

horhimg = np.pad(horimg, ((3, 3),(0, 0),(0, 0)), 'edge')

#-----Vertical-----
for j in range (0, d):
	for i in range(0, w*16-15):
		for r in range (3, h+6-4):
			C = horhimg[r-3][i][j]
			B = horhimg[r-2][i][j]
			A = horhimg[r-1][i][j]
			W = horhimg[r][i][j]
			D = horhimg[r+1][i][j]
			E = horhimg[r+2][i][j]
			F = horhimg[r+3][i][j]
			G = horhimg[r+4][i][j] 

			finalimg[(r-3)*16][i][j] = horimg[r-3][i][j]
			finalimg[(r-3)*16+1][i][j], finalimg[(r-3)*16+2][i][j],finalimg[(r-3)*16+3][i][j], finalimg[(r-3)*16+4][i][j], finalimg[(r-3)*16+5][i][j], finalimg[(r-3)*16+6][i][j], finalimg[(r-3)*16+7][i][j], finalimg[(r-3)*16+8][i][j], finalimg[(r-3)*16+9][i][j], finalimg[(r-3)*16+10][i][j], finalimg[(r-3)*16+11][i][j], finalimg[(r-3)*16+12][i][j], finalimg[(r-3)*16+13][i][j], finalimg[(r-3)*16+14][i][j], finalimg[(r-3)*16+15][i][j] = equacoes(C,B,A,W,D,E,F,G)
		finalimg[(h*16-16)][i][j] = horimg[h-1][i][j]

array = np.array(finalimg, dtype=np.uint8)
im = Image.fromarray(array)
#im.show()
im.save('%s.jpg'%output)