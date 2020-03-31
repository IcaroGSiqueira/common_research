import os
from datetime import datetime

dateTimeObj = datetime.now()
timeObj = dateTimeObj.time()
time = "%s.%s.%s"%(timeObj.hour, timeObj.minute, timeObj.second)
# import glob
# import pandas as pd

pathin = "/home/icaro/pesquisa_ucpel/output_VTM/local/parsed_traces"
#pathin = "/home/icaro/testesHEVC/gprof"
files = sorted(os.listdir("%s"%pathin))

os.system("mkdir /home/icaro/pesquisa_ucpel/output_VTM/local/bk_parsed_cont")

os.system("mv /home/icaro/pesquisa_ucpel/output_VTM/local/bk_parsed_cont/parsed_cont /home/icaro/pesquisa_ucpel/output_VTM/local/bk_parsed_cont/parsed_cont_%s"%time)

os.system("mv /home/icaro/pesquisa_ucpel/output_VTM/local/parsed_cont /home/icaro/pesquisa_ucpel/output_VTM/local/bk_parsed_cont")

os.system("mkdir /home/icaro/pesquisa_ucpel/output_VTM/local/parsed_cont")

try:
    test = open("/home/icaro/pesquisa_ucpel/output_VTM/local/parsed_cont/cont_vtm-partitions.csv","r")
except:
    out2 = open("/home/icaro/pesquisa_ucpel/output_VTM/local/parsed_cont/cont_vtm-partitions.csv","a")
    linhaf = "YUV,OPT,QP,128x128,128x64,64x128,64x64,64x48,64x32,64x24,64x16,64x12,64x8,64x4,64x2,48x64,48x32,48x16,48x8,48x4,32x64,32x48,32x32,32x24,32x16,32x12,32x8,32x4,32x2,24x64,24x32,24x16,24x8,24x4,16x64,16x48,16x32,16x24,16x16,16x12,16x8,16x4,16x2,12x64,12x32,12x16,12x8,12x4,8x64,8x48,8x32,8x24,8x16,8x12,8x8,8x4,8x2,4x64,4x48,4x32,4x24,4x16,4x12,4x8,4x4,4x2,2x64,2x32,2x16,2x8,2x4,zeros,resto,chroma\n"

    out2.write(linhaf)

p128x128 = p128x64 = p64x128 = p64x64 = p64x48 = p64x32 = p64x24 = p64x16 = p64x12 = p64x8 = p64x4 = p64x2 = p48x64 = p48x32 = p48x16 = p48x8 = p48x4 = p32x64 = p32x48 = p32x32 = p32x24 = p32x16 = p32x12 = p32x8 = p32x4 = p32x2 = p24x64 = p24x32 = p24x16 = p24x8 = p24x4 = p16x64 = p16x48 = p16x32 = p16x24 = p16x16 = p16x12 = p16x8 = p16x4 = p16x2 = p12x64 = p12x32 = p12x16 = p12x8 = p12x4 = p8x64 = p8x48 = p8x32 = p8x24 = p8x16 = p8x12 = p8x8 = p8x4 = p8x2 = p4x64 = p4x48 = p4x32 = p4x24 = p4x16 = p4x12 = p4x8 = p4x4 = p4x2 = p2x64 = p2x32 = p2x16 = p2x8 = p2x4 = zero = resto = chroma = 0

for file in files:
    if "~" in file:
        continue
    prof = open("%s/%s"%(pathin,file),"r")
    lines = prof.readlines()

    dummy,VID,pix,fr,b,fl,conf,opt,intx = file.split("_")
    VID = VID+"_"+intx

    line=lines[1]
    nome, poc, QP, x, y, w, h, wxh, Normalized, PredMode, Depth, QT_Depth, BT_Depth, MT_Depth, QP_Real, ChromaQPAdj, BlockQP, SplitSeries, TransQuantBypassFlag, TransformSkipFlag_Y, BDPCM, TileIdx, IndependentSliceIdx, LFNSTIdx, JointCbCr, CompAlphaCb, CompAlphaCr, RDPCM_Y, RDPCM_Cb, RDPCM_Cr, Luma_IntraMode, Chroma_IntraMode, MultiRefIdx, MIPFlag, ISPMode, SkipFlag, RootCbf, SbtIdx, SbtPos, Cbf_Y, Cbf_Cb, Cbf_Cr, IMVMode, InterDir, MergeFlag, RegularMergeFlag, MergeIdx, MergeType, MVPIdxL0, MVPIdxL1, MVL0, MVL1, MVDL0, MVDL1, MotionBufL0, MotionBufL1, RefIdxL0, RefIdxL1, AffineFlag, AffineMVL0, AffineMVL1, AffineType, MMVDSkipFlag, MMVDMergeFlag, MMVDMergeIdx, MHIntraFlag, SMVDFlag, TrianglePartitioning, TriangleMVL0, TriangleMVL1, GBIIndex, Depth_Chroma, QT_Depth_Chroma, BT_Depth_Chroma, MT_Depth_Chroma, ChromaQPAdj_Chroma, QP_Chroma, SplitSeries_Chroma, TransQuantBypassFlag_Chroma = line.split(",")
    break

for file in files:
    if "~" in file:
        continue

    #QP = " QP"

    prof = open("%s/%s"%(pathin,file),"r")
    lines = prof.readlines()
    line=i=1

    dummy,vid,pix,fr,b,fl,conf,opt,intx = file.split("_")
    b = b.strip("bit")
    fr = fr.strip("fps")
    #QP = qp.strip("qp")
    fl = fl.strip("fframes")
    #poc = poc.strip("poc.csv")
    #nome = vid+"_"+pix+"_"+fr+"fps"+"_"+b+"bit"+"_"+fl+"flimit"+"_"+conf+"_"+opt

    # try:
    #     test = open("/home/icaro/pesquisa_ucpel/output_VTM/local/parsed_cont/cont_%s_INTER.csv"%nome,"r")
    # except:
    #     out2 = open("/home/icaro/pesquisa_ucpel/output_VTM/local/parsed_cont/cont_%s_INTER.csv"%nome,"a")
    #     linhaf = "YUV,QP,128x128,128x64,64x128,64x64,64x48,64x32,64x24,64x16,64x12,64x8,64x4,64x2,48x64,48x32,48x16,48x8,48x4,32x64,32x48,32x32,32x24,32x16,32x12,32x8,32x4,32x2,24x64,24x32,24x16,24x8,24x4,16x64,16x48,16x32,16x24,16x16,16x12,16x8,16x4,16x2,12x64,12x32,12x16,12x8,12x4,8x64,8x48,8x32,8x24,8x16,8x12,8x8,8x4,8x2,4x64,4x48,4x32,4x24,4x16,4x12,4x8,4x4,4x2,2x64,2x32,2x16,2x8,2x4\n"

    #     out2.write(linhaf)
    # try:
    #     test = open("/home/icaro/pesquisa_ucpel/output_VTM/local/parsed_cont/cont_%s_INTRA.csv"%nome,"r")
    # except:
    #     out2 = open("/home/icaro/pesquisa_ucpel/output_VTM/local/parsed_cont/cont_%s_INTRA.csv"%nome,"a")
    #     linhaf = "YUV,QP,128x128,128x64,64x128,64x64,64x48,64x32,64x24,64x16,64x12,64x8,64x4,64x2,48x64,48x32,48x16,48x8,48x4,32x64,32x48,32x32,32x24,32x16,32x12,32x8,32x4,32x2,24x64,24x32,24x16,24x8,24x4,16x64,16x48,16x32,16x24,16x16,16x12,16x8,16x4,16x2,12x64,12x32,12x16,12x8,12x4,8x64,8x48,8x32,8x24,8x16,8x12,8x8,8x4,8x2,4x64,4x48,4x32,4x24,4x16,4x12,4x8,4x4,4x2,2x64,2x32,2x16,2x8,2x4\n"

    #     out2.write(linhaf)

    # if intx == "INTRA":
    #     out2 = open("/home/icaro/pesquisa_ucpel/output_VTM/local/parsed_traces/cont_%s_INTRA.csv"%nome,"a")
    # if intx == "INTER":
    #     out2 = open("/home/icaro/pesquisa_ucpel/output_VTM/local/parsed_traces/cont_%s_INTER.csv"%nome,"a")
    
    while line != lines[-1]:
        line=lines[i]
        i+=1
        nome, poc, qp, x, y, w, h, wxh, Normalized, PredMode, Depth, QT_Depth, BT_Depth, MT_Depth, QP_Real, ChromaQPAdj, BlockQP, SplitSeries, TransQuantBypassFlag, TransformSkipFlag_Y, BDPCM, TileIdx, IndependentSliceIdx, LFNSTIdx, JointCbCr, CompAlphaCb, CompAlphaCr, RDPCM_Y, RDPCM_Cb, RDPCM_Cr, Luma_IntraMode, Chroma_IntraMode, MultiRefIdx, MIPFlag, ISPMode, SkipFlag, RootCbf, SbtIdx, SbtPos, Cbf_Y, Cbf_Cb, Cbf_Cr, IMVMode, InterDir, MergeFlag, RegularMergeFlag, MergeIdx, MergeType, MVPIdxL0, MVPIdxL1, MVL0, MVL1, MVDL0, MVDL1, MotionBufL0, MotionBufL1, RefIdxL0, RefIdxL1, AffineFlag, AffineMVL0, AffineMVL1, AffineType, MMVDSkipFlag, MMVDMergeFlag, MMVDMergeIdx, MHIntraFlag, SMVDFlag, TrianglePartitioning, TriangleMVL0, TriangleMVL1, GBIIndex, Depth_Chroma, QT_Depth_Chroma, BT_Depth_Chroma, MT_Depth_Chroma, ChromaQPAdj_Chroma, QP_Chroma, SplitSeries_Chroma, TransQuantBypassFlag_Chroma = line.split(",")

        dummy,vid,pix,fr,b,fl,conf,opt,intx = file.split("_")
        vid = vid+"_"+intx

        if((qp != QP) or (vid != VID)):

            VID,OPT = VID.split("_")

            lin2 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(VID,OPT,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma)

            out2.write(lin2)
            print(lin2)

            p128x128 = p128x64 = p64x128 = p64x64 = p64x48 = p64x32 = p64x24 = p64x16 = p64x12 = p64x8 = p64x4 = p64x2 = p48x64 = p48x32 = p48x16 = p48x8 = p48x4 = p32x64 = p32x48 = p32x32 = p32x24 = p32x16 = p32x12 = p32x8 = p32x4 = p32x2 = p24x64 = p24x32 = p24x16 = p24x8 = p24x4 = p16x64 = p16x48 = p16x32 = p16x24 = p16x16 = p16x12 = p16x8 = p16x4 = p16x2 = p12x64 = p12x32 = p12x16 = p12x8 = p12x4 = p8x64 = p8x48 = p8x32 = p8x24 = p8x16 = p8x12 = p8x8 = p8x4 = p8x2 = p4x64 = p4x48 = p4x32 = p4x24 = p4x16 = p4x12 = p4x8 = p4x4 = p4x2 = p2x64 = p2x32 = p2x16 = p2x8 = p2x4 = zero = resto = chroma = 0

            QP = qp
            VID = vid

        if (((Cbf_Y != "0") or (Cbf_Y == "---")) and ((Cbf_Cb == "---") or (Cbf_Cb == 0) or (Cbf_Cb == "0")) and ((Cbf_Cr == "0") or (Cbf_Cr == "---") or (Cbf_Cr == 0)) and ((ChromaQPAdj == 0) or (ChromaQPAdj == "0") or (ChromaQPAdj == "---")) and ((Chroma_IntraMode == "---") or (Chroma_IntraMode == 0) or (Chroma_IntraMode == "0")) and ((Depth_Chroma == "0") or (Depth_Chroma == 0) or (Depth_Chroma == "---")) and ((QT_Depth_Chroma == 0) or (QT_Depth_Chroma == "---") or (QT_Depth_Chroma == "0")) and ((MT_Depth_Chroma == "0") or (MT_Depth_Chroma == 0) or (MT_Depth_Chroma == "---")) and ((BT_Depth_Chroma == "---") or (BT_Depth_Chroma == 0) or (BT_Depth_Chroma == "0")) and ((QP_Chroma == "---") or (QP_Chroma == 0) or (QP_Chroma == "0")) and ((SplitSeries_Chroma == "0") or (SplitSeries_Chroma == 0) or (SplitSeries_Chroma == "---")) and ((TransQuantBypassFlag_Chroma == "0\n") or (TransQuantBypassFlag_Chroma == 0) or (TransQuantBypassFlag_Chroma == "---\n")) and ((ChromaQPAdj_Chroma == "0") or (ChromaQPAdj_Chroma == 0) or (ChromaQPAdj_Chroma == "---"))):

            part = wxh
            if part == "128x128":
                p128x128+=1
            elif part == "128x64":
                p128x64+=1
            elif part == "64x128":
                p64x128+=1
            elif part == "64x64":
                p64x64+=1
            elif part == "64x48":
                p64x48+=1
            elif part == "64x32":
                p64x32+=1
            elif part == "64x24":
                p64x24+=1
            elif part == "64x16":
                p64x16+=1
            elif part == "64x12":
                p64x12+=1
            elif part == "64x 8":
                p64x8+=1
            elif part == "64x 4":
                p64x4+=1
            elif part == "64x 2":
                p64x2+=1
            elif part == "48x64":
                p48x64+=1
            elif part == "48x32":
                p48x32+=1
            elif part == "48x16":
                p48x16+=1
            elif part == "48x 8":
                p48x8+=1
            elif part == "48x 4":
                p48x4+=1
            elif part == "32x64":
                p32x64+=1
            elif part == "32x48":
                p32x48+=1
            elif part == "32x32":
                p32x32+=1
            elif part == "32x24":
                p32x24+=1
            elif part == "32x16":
                p32x16+=1
            elif part == "32x12":
                p32x12+=1
            elif part == "32x 8":
                p32x8+=1
            elif part == "32x 4":
                p32x4+=1
            elif part == "32x 2":
                p32x2+=1
            elif part == "24x64":
                p24x64+=1
            elif part == "24x32":
                p24x32+=1
            elif part == "24x16":
                p24x16+=1
            elif part == "24x 8":
                p24x8+=1
            elif part == "24x 4":
                p24x4+=1
            elif part == "16x64":
                p16x64+=1
            elif part == "16x48":
                p16x48+=1
            elif part == "16x32":
                p16x32+=1
            elif part == "16x24":
                p16x24+=1
            elif part == "16x16":
                p16x16+=1
            elif part == "16x12":
                p16x12+=1
            elif part == "16x 8":
                p16x8+=1
            elif part == "16x 4":
                p16x4+=1
            elif part == "16x 2":
                p16x2+=1
            elif part == "12x64":
                p12x64+=1
            elif part == "12x32":
                p12x32+=1
            elif part == "12x16":
                p12x16+=1
            elif part == "12x 8":
                p12x8+=1
            elif part == "12x 4":
                p12x4+=1
            elif part == " 8x64":
                p8x64+=1
            elif part == " 8x48":
                p8x48+=1
            elif part == " 8x32":
                p8x32+=1
            elif part == " 8x24":
                p8x24+=1
            elif part == " 8x16":
                p8x16+=1
            elif part == " 8x12":
                p8x12+=1
            elif part == " 8x 8":
                p8x8+=1
            elif part == " 8x 4":
                p8x4+=1
            elif part == " 8x 2":
                p8x2+=1
            elif part == " 4x64":
                p4x64+=1
            elif part == " 4x48":
                p4x48+=1
            elif part == " 4x32":
                p4x32+=1
            elif part == " 4x24":
                p4x24+=1
            elif part == " 4x16":
                p4x16+=1
            elif part == " 4x12":
                p4x12+=1
            elif part == " 4x 8":
                p4x8+=1
            elif part == " 4x 4":
                p4x4+=1
            elif part == " 4x 2":
                p4x2+=1
            elif part == " 2x64":
                p2x64+=1
            elif part == " 2x32":
                p2x32+=1
            elif part == " 2x16":
                p2x16+=1
            elif part == " 2x 8":
                p2x8+=1
            elif part == " 2x 4":
                p2x4+=1
            elif part == " 0x 0":
                zero+=1
            else:
                resto+=1
        else:
            chroma+=1

lin2 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(VID,OPT,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma)

out2.write(lin2)
print(lin2)
out2.close

# try:
#     test = open("/home/icaro/pesquisa_ucpel/output_VTM/local/parsed_cont/ord_vtm-partitions.csv","r")
# except:
#     out = open("/home/icaro/pesquisa_ucpel/output_VTM/local/parsed_cont/ord_vtm-partitions.csv","a")
#     linhaf = "YUV,QP,128x128,128x64,64x128,64x64,64x48,64x32,64x24,64x16,64x12,64x8,64x4,64x2,48x64,48x32,48x16,48x8,48x4,32x64,32x48,32x32,32x24,32x16,32x12,32x8,32x4,32x2,24x64,24x32,24x16,24x8,24x4,16x64,16x48,16x32,16x24,16x16,16x12,16x8,16x4,16x2,12x64,12x32,12x16,12x8,12x4,8x64,8x48,8x32,8x24,8x16,8x12,8x8,8x4,8x2,4x64,4x48,4x32,4x24,4x16,4x12,4x8,4x4,4x2,2x64,2x32,2x16,2x8,2x4,zeros,resto,chroma\n"

# out.write(linhaf)

# file = open("/home/icaro/pesquisa_ucpel/output_VTM/local/parsed_cont/cont_vtm-partitions.csv","r")
# lines = file.readlines()

# i=1
# while line != lines[-1]:
#     line=lines[i]
#     i+=1
#     print(line)
    
#     VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma = line.split(",")
#     if "INTRA" in VID:
#         if QP == 22:
#             lin2 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma)
#             out.write(lin2)
# i=1
# while line != lines[-1]:
#     line=lines[i]
#     i+=1
#     VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma = line.split(",")
#     if "INTRA" in VID:
#         if QP == 27:
#             lin2 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma)
#             out.write(lin2)
# i=1
# while line != lines[-1]:
#     line=lines[i]
#     i+=1
#     VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma = line.split(",")
#     if "INTRA" in VID:
#         if QP == 32:
#             lin2 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma)
#             out.write(lin2)
# i=1
# while line != lines[-1]:
#     line=lines[i]
#     i+=1
#     VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma = line.split(",")
#     if "INTRA" in VID:
#         if QP == 37:
#             lin2 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma)
#             out.write(lin2)
# i=1
# while line != lines[-1]:
#     line=lines[i]
#     i+=1
#     VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma = line.split(",")
#     if "INTER" in VID:
#         if QP == 22:
#             lin2 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma)
#             out.write(lin2)
# i=1
# while line != lines[-1]:
#     line=lines[i]
#     i+=1
#     VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma = line.split(",")
#     if "INTER" in VID:
#         if QP == 27:
#             lin2 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma)
#             out.write(lin2)
# i=1
# while line != lines[-1]:
#     line=lines[i]
#     i+=1
#     VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma = line.split(",")
#     if "INTER" in VID:
#         if QP == 32:
#             lin2 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma)
#             out.write(lin2)
# i=1
# while line != lines[-1]:
#     line=lines[i]
#     i+=1
#     VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma = line.split(",")
#     if "INTER" in VID:
#         if QP == 37:
#             lin2 = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(VID,QP,p128x128,p128x64,p64x128,p64x64,p64x48,p64x32,p64x24,p64x16,p64x12,p64x8,p64x4,p64x2,p48x64,p48x32,p48x16,p48x8,p48x4,p32x64,p32x48,p32x32,p32x24,p32x16,p32x12,p32x8,p32x4,p32x2,p24x64,p24x32,p24x16,p24x8,p24x4,p16x64,p16x48,p16x32,p16x24,p16x16,p16x12,p16x8,p16x4,p16x2,p12x64,p12x32,p12x16,p12x8,p12x4,p8x64,p8x48,p8x32,p8x24,p8x16,p8x12,p8x8,p8x4,p8x2,p4x64,p4x48,p4x32,p4x24,p4x16,p4x12,p4x8,p4x4,p4x2,p2x64,p2x32,p2x16,p2x8,p2x4,zero,resto,chroma)
#             out.write(lin2)