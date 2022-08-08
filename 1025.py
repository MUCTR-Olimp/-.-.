import sys
if(False):file=sys.stdin
else:file=open("input.txt","r")
flag=True
for line in file:
	if(flag):kol=int(line);flag=False;continue
	s=list(map(int,line.split()))
file.close()
output=0
i=0
while(i<(kol//2+int(bool(kol/2%1)))):
	mi=min(s)
	index_mi=s.index(mi)
	s=s[:index_mi]+s[index_mi+1:]
	output+=mi//2+int(bool(mi/2%1))
	i+=1
print(output)
