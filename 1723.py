import sys
if(True):file=sys.stdin
else:file=open("input.txt","r")
word=file.read()
file.close()
max_kol=1
output=word
for len_word in range(2,len(word)-1):
	for i in range(len(word)-len_word):
		word_i=word[i:i+len_word]
		kol=0
		for g in range(len(word)):
			if(word_i==word[g:g+len_word]):kol+=1
		if(kol>=max_kol):output=word_i;max_kol=kol
print(output)
	
	

