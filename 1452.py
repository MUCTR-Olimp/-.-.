import sys
if(False):file=sys.stdin
else:file=open("input.txt","r")
flag=True
for line in file:
	if(flag):flag=False;continue
	s=list(map(int,line.split()))
file.close()
deltas=[]
for i in range(len(s)):
	for g in range(i+1,len(s)):
		kol=abs(s[i]-s[g])
		if((not kol in deltas) and kol):deltas.append(kol)
output=[1]
ma_kol=1
new_output=[]
for step in deltas:
	new_output=[]
	znach=[]
	kol=1
	for i in range(len(s)-1):
		for g in range(i+1,len(s)):
			if(abs(s[g]-s[i])==step):
				if((s[i] in znach) and (s[g] in znach)):continue
				kol+=1
				if(not s[i] in znach):new_output.append(i+1);znach.append(s[i])
				if(not s[g] in znach):new_output.append(g+1);znach.append(s[g])
				if(ma_kol<kol):output=new_output.copy();ma_kol=kol
print(ma_kol)
print(*output)
