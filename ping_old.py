import ftplib
import sys
import os
from datetime import datetime

new_f=ftplib.FTP("ftp.drivehq.com")
new_f.login("pankajxdx", "password123")
print ('Files in home direcotory:---')
new_f.retrlines('LIST')
print('\n')

f = open('locallog.txt','w')
time = datetime.now()
if os.system("ps -e|grep firefox") == 0 :
    f.write('System  no -- working  at    '+ datetime.isoformat(time))
else:
    f.write('System  no -- not working  at    '+ datetime.isoformat(time))
f.close()

f = open("locallog.txt", "rb")
new_f.cwd("/log")
new_f.storlines("APPE log.txt", f)
new_f.retrlines('LIST')
print ('File', f.name, 'copied sucessfully\n')
new_f.quit()

f.close()
