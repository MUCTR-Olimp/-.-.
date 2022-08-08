import sys
if(False):file=sys.stdin
else:file=open("input.txt","r")
flag=0
friends={}
ma=0
for line in file:
	if(flag==0):flag=1;continue
	friends[flag]=list(map(int,line.split()))[:-1]
	ma=max(ma,len(friends[flag]))
	flag+=1
in_progress=[]
team0=[]
team1=[]
ma+=1

while(True):
	mi=ma
	for index in friends:
		if(len(friends[index])<mi):mi=len(friends[index]);mi_index=index
	team0.append(mi_index)
	if(mi==1):team1.append(friends[mi_index][0]);friends.pop(mi_index)
	else:in_progress.append(mi_index);break
while(in_progress):
	mi=ma
	for index in in_progress:
		if((mi_index in friends[index]) and (len(friends[index])<mi)):mi=len(friends[index]);mi_index=index
	print(friends)

