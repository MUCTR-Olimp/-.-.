import sys
if(False):file=sys.stdin
else:file=open("input.txt","r")
flag=True
for line in file:
	if(flag):code0=int(line[-2]);flag=False
	else:code1=int(line[-2])
if((code0%2==0) or (code1%2==1)):print("yes")
else:print("no")
