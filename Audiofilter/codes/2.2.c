#include <stdio.h>

int main(){
	int b=15;
	double x[6]={1.0,2.0,3.0,4.0,2.0,1.0};
	double y[b];
	y[0]=x[0];
	FILE *fptr;
	fptr=fopen("out_diffeq.txt","w");
	for(int i=0;i<b;i++){
		if(i<6){
			y[i]=x[i]+x[i-2]-0.5*y[i-1];
		}
		else if(i>=6&&i<8){
			y[i]=x[i-2]-0.5*y[i-1];
		}
		else if(i>8){
			y[i]=-0.5*y[i-1];
		}
		fprintf(fptr,"%f\n",y[i]);
	}
	fclose(fptr);
	return 0;

}
