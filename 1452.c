#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#define len 2000
int main(){
	unsigned int i,g,z,h,ma_kol=1,kol,kol_deltas=0,kol_znach,s[len],output[len],znach[len],flag;
	unsigned int* deltas=(unsigned int*)malloc(len*len*sizeof(unsigned int));
	output[0]=1;
	if(1){
		FILE *file=fopen("input.txt","r");
		fscanf(file,"%u\n",&kol);
		for(i=0;i<kol;i++) fscanf(file,"%u ",&s[i]);
		fclose(file);
	}else{
		scanf("%u\n",&kol);
		for(i=0;i<kol;i++) scanf("%u ",&s[i]);
	}
	for(i=0;i<(kol-1);i++){
		for(g=i+1;g<kol;g++){
			if(s[i]!=s[g]){
				deltas[kol_deltas]=s[g]-s[i];
				if(deltas[kol_deltas]<0) deltas[kol_deltas]*=-1;
				flag=1;
				for(z=0;z<kol_deltas;z++){
					if(deltas[z]==deltas[kol_deltas]) {
						flag=0;
						break;
					}
				}
				if(flag) kol_deltas++;
			}
		}
	}
	for(h=0;h<kol_deltas;h++){
		kol_znach=0;
		for(i=0;i<(kol-1);i++){
			for(g=i+1;g<kol;g++){
				if(((s[g]-s[i])==deltas[h]) || ((s[i]-s[g])==deltas[h])){
					flag=0;
					for(z=0;z<kol_znach;z++){
						if(znach[z]==s[i]){
							if(flag==0) flag=1;
							else flag=3;
						}
						if(znach[z]==s[g]){
							if(flag==0) flag=2;
							else flag=3;
						}
					}
					if(flag==3) continue;
					if((flag==2) || (flag==0)){
						znach[kol_znach]=s[i];
						kol_znach++;
					}
					if((flag==1) || (flag==0)){
						znach[kol_znach]=s[g];
						kol_znach++;
					}
					if(ma_kol<kol_znach){
						ma_kol=kol_znach;
						for(z=0;z<kol_znach;z++) output[z]=znach[z];
					}
				}
			}
		}
	}
	printf("%u\n",ma_kol);
	for(i=0;i<ma_kol;i++){
		for(g=0;g<kol;g++) {
			if(s[g]==output[i]){
				printf("%u ",g+1);//Переделать
				break;
			}
		}
	}
	free(deltas);
	//scanf(" ");
	return 0;
}