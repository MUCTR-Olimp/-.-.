#Success
import sys
teams = []
flag = True
file = sys.stdin if 1 else open("input.txt", "r")
for line in file:
	if(flag):
		flag = False
		continue
	if(line[-1] == "\n"):
		line = line[:-1]
	teams.append(line)
file.close()
del line, file
def SortByLetter(first, second):
	i = 0
	mi = min(len(first), len(second))
	while(i < mi):
		if(first[i] != second[i]):
			return ord(first[i]) > ord(second[i])
		i += 1
	return len(second) == mi

Names = {}
Teams = []
for names in teams:
	Teams.append(list(names.split()))
	for name in names.split():
		Names[name] = 0 if (name == "Isenbaev") else "undefined"
New_Active_Names=["Isenbaev"]
lvl = 0
while(New_Active_Names):
	lvl += 1
	Active_Names = New_Active_Names.copy()
	New_Active_Names=[]
	for active_name in Active_Names:
		for team in Teams:
			if(active_name in team):
				for name in team:
					if((name == active_name) or ((Names[name] != "undefined") and (Names[name] < lvl))):continue
					Names[name] = lvl
					New_Active_Names.append(name)





#------output------
#------------------
#------------------
output=[]
for name in Names:
	output.append((name,Names[name]))
flag = True
while(flag):
	flag = False
	for i in range(len(output) - 1):
		if(SortByLetter(output[i][0], output[i + 1][0])):
			output[i], output[i + 1] = output[i + 1], output[i]
			flag = True
for SeName in output:
	print(*SeName)
