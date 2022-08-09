#include <stdio.h>
#include <stdlib.h>
#define len 200000
int main(){
	char text[len];
	unsigned int i=0,g=0;
	FILE *file=fopen("input.txt","r");
	fscanf(file,"%s",&text);
	fclose(file);
	//scanf("%s",&text);
	while((i<len-1) && (text[i+1]!='\0')){
		if(text[i]!='.'){
			g=i+1;
			while((text[g]=='.') && (g<len-1) && (text[g+1]!='\0')) g++;
			if(text[i]==text[g]){
				text[i]='.';
				text[g]='.';
				if(i!=0) i-=2;
				while((text[i]=='.') && (i>0)) i--;
				if(text[i]=='.'){
					while((text[i]=='.') && (i<len-1) && (text[g+1]!='\0')) i++;
				}
			}
		}
		i++;
	}
	//printf("%s\n",text);
	for (i=0;text[i]!='\0';i++) {
		if(text[i]!='.') printf("%c",text[i]);
	}
	return 0;
}