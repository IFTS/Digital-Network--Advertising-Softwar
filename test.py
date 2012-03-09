
import os
import re
vlist=os.listdir('.')
name=''
for item in vlist:
        match=re.search(r'system\w*', item)
        if match:
                name=match.group()[6:]
print name

