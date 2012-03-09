import os
import re

vlist=os.listdir('./videos')
plist=[]
glist=[]
slist=[]

for item in vlist:
	m=re.search(r'__p', item)
	if m :
		plist.append(item)
plist=sorted(plist)

for item in vlist:
        m=re.search(r'__g', item)
        if m :
                glist.append(item)
glist=sorted(glist)

for item in vlist:
        m=re.search(r'__s', item)
        if m :
                slist.append(item)
slist=sorted(slist)

#print 'All the items in directory: ', vlist, '\n'
#print 'plist is: ', plist, '\n'
#print 'glist is: ', glist, '\n'
#print 'slist is: ', slist, '\n'

slist1=plist
slist2=[]
slist3=[]

if len(plist)>len(glist):
	length=len(plist)
else :
	length=len(glist)


for i in range(0, length):
	if len(plist) > i:
		slist2.append(plist[i])
	if (len(glist) > i):
		slist2.append(glist[i])


if length < len(slist):
	length=len(slist)


for i in range(0, length):
        if len(plist) > i:
                slist3.append(plist[i])
        if (len(glist) > i):
                slist3.append(glist[i])
        if (len(slist) > i):
                slist3.append(slist[i])
	
finallist=slist1+slist2+slist3

#print 'final list is :', finallist, '\n'

st='mplayer -fixed-vo -fs -loop 0 '
for item in finallist:
	st+='./videos/'+item+' '

#print st
#os.system("echo 'zoom=no' >> $HOME/.mplayer/config")
#os.system("perl -p -i.bak -e 's|vo_driver = 'x11'|vo_driver = 'xv'|' .mplayer/gui.conf")
os.system("killall mplayer")
os.system(st)


