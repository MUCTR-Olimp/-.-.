#Success
import sys
file = sys.stdin if 1 else open("input.txt", "r")
n = int(file.readline())
k = int(file.readline())
file.close()
def check(num):
	global count
	if(not "00" in num):
		count+=(k - 1)**num.count("1")
count = 0
num = "1" + "0" * (n - 1)
check(num)
while("0" in num):
	i = n - 1
	while(i>=0):
		num = num[:i] + ("1" if (num[i] == "0") else "0") + num[i + 1:]
		if(num[i] != "0"):break
		i-=1
	check(num)
print(count)
