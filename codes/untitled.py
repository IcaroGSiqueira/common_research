#try:
#    test = open("/home/icaro/pesquisa_ucpel/output_VTM/local/parsed_cont/ord_vtm-partitions.csv","r")
#except:
out = open("/home/icaro/pesquisa_ucpel/output_VTM/local/parsed_cont/ord_vtm-partitions.csv","a")
linhaf = "YUV,QP,128x128,128x64,64x128,64x64,64x48,64x32,64x24,64x16,64x12,64x8,64x4,64x2,48x64,48x32,48x16,48x8,48x4,32x64,32x48,32x32,32x24,32x16,32x12,32x8,32x4,32x2,24x64,24x32,24x16,24x8,24x4,16x64,16x48,16x32,16x24,16x16,16x12,16x8,16x4,16x2,12x64,12x32,12x16,12x8,12x4,8x64,8x48,8x32,8x24,8x16,8x12,8x8,8x4,8x2,4x64,4x48,4x32,4x24,4x16,4x12,4x8,4x4,4x2,2x64,2x32,2x16,2x8,2x4,zeros,resto,chroma\n"

out.write(linhaf)

file = open("/home/icaro/pesquisa_ucpel/output_VTM/local/parsed_cont/cont_vtm-partitions.csv","r")
lines = file.readlines()

i=line=1
while line != lines[-1]:
    line=lines[i]
    i+=1
    VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma = line.split(",")
    if "INTRA" in VID:
        if QP == 22:
            lin2 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma)
            out.write(lin2)
i=1
while line != lines[-1]:
    line=lines[i]
    i+=1
    VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma = line.split(",")
    if "INTRA" in VID:
        if QP == 27:
            lin2 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma)
            out.write(lin2)
i=1
while line != lines[-1]:
    line=lines[i]
    i+=1
    VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma = line.split(",")
    if "INTRA" in VID:
        if QP == 32:
            lin2 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma)
            out.write(lin2)
i=1
while line != lines[-1]:
    line=lines[i]
    i+=1
    VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma = line.split(",")
    if "INTRA" in VID:
        if QP == 37:
            lin2 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma)
            out.write(lin2)
i=1
while line != lines[-1]:
    line=lines[i]
    i+=1
    VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma = line.split(",")
    if "INTER" in VID:
        if QP == 22:
            lin2 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma)
            out.write(lin2)
i=1
while line != lines[-1]:
    line=lines[i]
    i+=1
    VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma = line.split(",")
    if "INTER" in VID:
        if QP == 27:
            lin2 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma)
            out.write(lin2)
i=1
while line != lines[-1]:
    line=lines[i]
    i+=1
    VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma = line.split(",")
    if "INTER" in VID:
        if QP == 32:
            lin2 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma)
            out.write(lin2)
i=1
while line != lines[-1]:
    line=lines[i]
    i+=1
    VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma = line.split(",")
    if "INTER" in VID:
        if QP == 37:
            lin2 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma)
            out.write(lin2)