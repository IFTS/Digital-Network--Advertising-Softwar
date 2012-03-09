import ftplib
import sys
import os
import re
from datetime import datetime

new_f=ftplib.FTP("182.50.134.1")
new_f.login("myriadsdigital", "Password*123")
#print ('Files in home direcotory:---')
#new_f.retrlines('LIST')
#print('\n')


vlist=os.listdir('.')
name=''
for item in vlist:
        match=re.search(r'system\w*', item)
        if match:
                name=match.group()[6:]
print name

f = open('locallog.txt','w')
time = datetime.now()
if os.system("ps -e|grep mplayer") == 0 :
    f.write('System  no '+name+'  working  at    '+ datetime.isoformat(time))
else:
    f.write('System  no '+name+' not working  at    '+ datetime.isoformat(time))
f.close()

f = open("locallog.txt", "rb")
new_f.cwd("/log")
new_f.storlines("APPE log.txt", f)
new_f.retrlines('LIST')
print ('Log uploaded sucessfully!\n')
new_f.quit()

f.close()
