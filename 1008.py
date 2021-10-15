import sys
s=[]
Mode=True
true=True
if(False):file=sys.stdin
else:file=open("input.txt","r")
for line in file:
	if(true):
		true=False
		try:kol=int(line)
		except:
			Mode=False
			x,y=list(map(int,line.split()))
	else:
		if(Mode):s.append(list(map(int,line.split())))
		else:
			s.append(line[:-2])
if(Mode):
	#print(s)
	x,y=[10,10]
	for i in range(kol):
		if(s[i][0]<=x):x=s[i][0]
	for i in range(kol):
		if((s[i][0]==x) and (s[i][1]<y)):y=s[i][1]
	print(x,y)
	MAP=[[x,y]]
	s=s[:s.index([x,y])]+s[s.index([x,y])+1:]
	while(MAP):#RTLB
		x,y=MAP[0]
		MAP=MAP[1:]
		if([x+1,y] in s):
			print("R",end="")
			s=s[:s.index([x+1,y])]+s[s.index([x+1,y])+1:]
			MAP.append([x+1,y])
		if([x,y+1] in s):
			print("T",end="")
			s=s[:s.index([x,y+1])]+s[s.index([x,y+1])+1:]
			MAP.append([x,y+1])
		if([x-1,y] in s):
			print("L",end="")
			s=s[:s.index([x-1,y])]+s[s.index([x-1,y])+1:]
			MAP.append([x-1,y])
		if([x,y-1] in s):
			print("B",end="")
			s=s[:s.index([x,y-1])]+s[s.index([x,y-1])+1:]
			MAP.append([x,y-1])
		if(MAP):print(",")
	print(".")
else:
	points=[]
	MAP=[[x,y]]
	for index,i in enumerate(s):
		#RTLB
		x,y=MAP[index]
		points.append(MAP[index])
		if("R" in i):MAP.append([x+1,y])
		if("T" in i):MAP.append([x,y+1])
		if("L" in i):MAP.append([x-1,y])
		if("B" in i):MAP.append([x,y-1])
	print(len(points))
	for x in range(10):
		for y in range(10):
			if([x,y] in points):print(x,y)
'''
6
2 3
2 4
3 3
3 4
4 2
4 3
'''
