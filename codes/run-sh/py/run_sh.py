import os
file = open("../run_sh.sh","w")
linhaHM = "cd ../HM-16.9/bin/ && sh run_hm.sh"
linhaVTM = "cd ../../VVCSoftware_VTM/bin/ && sh run_vtm.sh"
print >> file, linhaHM
print >> file, linhaVTM
file.close