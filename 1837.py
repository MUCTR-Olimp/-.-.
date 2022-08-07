import sys
DICT="abcdefghijklmnopqrstuvwxyz"
teams=[]
flag=True
if(True):file=sys.stdin
else:file=open("input.txt","r")
for line in file:
	if(flag):flag=False;continue
	if(line[-1]=="\n"):line=line[:-1]
	teams.append(line)
file.close()
del line,file
SeNames_tagged_last={}
SeNames_tagged={"Isenbaev":0}
while(SeNames_tagged_last!=SeNames_tagged):
	SeNames_tagged_last=SeNames_tagged.copy()
	team_index=0
	while(team_index<len(teams)):
		team=list(map(str,teams[team_index].split()))
		for i in range(len(team)):
			if(team[i] in SeNames_tagged):
				for g in range(len(team)):
					if(i!=g):
						if(team[g] in SeNames_tagged):
							if(SeNames_tagged[team[g]]>SeNames_tagged[team[i]]+1):SeNames_tagged[team[g]]=SeNames_tagged[team[i]]+1
						else:SeNames_tagged[team[g]]=SeNames_tagged[team[i]]+1
		team_index+=1
del SeNames_tagged_last
def SortByLetter(first,second):
	first=first.lower()
	second=second.lower()
	mi=min(len(first),len(second))
	for i in range(mi):
		if(first[i]!=second[i]):return DICT.find(first[i])<DICT.find(second[i])
	return len(second)==mi
output=[]
for SeName in SeNames_tagged:
	flag=False
	for g in range(len(output)):
		if(SortByLetter(SeName,output[g][0])):output=output[:g]+[(SeName,SeNames_tagged[SeName])]+output[g:];flag=True;break
	if(not flag):output.append((SeName,SeNames_tagged[SeName]))
for team in teams:
	team=list(map(str,team.split()))
	for i in range(len(team)):
		if(not team[i] in SeNames_tagged):
			flag=False
			for g in range(len(output)):
				if(SortByLetter(team[i],output[g][0])):output=output[:g]+[(team[i],"undefined")]+output[g:];flag=True;break
			if(not flag):output.append((team[i],"undefined"))
for SeName in output:print(*SeName)

