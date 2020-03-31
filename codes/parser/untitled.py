import os
from datetime import datetime

dateTimeObj = datetime.now()
timeObj = dateTimeObj.time()
now = "oi%s%s%s"%(timeObj.hour, timeObj.minute, timeObj.second)

print(now)

import os
from datetime import datetime

dateTimeObj = datetime.now()
timeObj = dateTimeObj.time()
time = "%s.%s.%s"%(timeObj.hour, timeObj.minute, timeObj.second)
# import glob
# import pandas as pd
print(time)