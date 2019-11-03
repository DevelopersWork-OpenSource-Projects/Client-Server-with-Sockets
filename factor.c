#define max 255
int n;
void getfactors(char data[]){
	char output[max] = "";
	n = atoi(data);
    int i = 2;
    do{
        if(n % i == 0){
            n = n / i;
			if(strcmp(output,"") == 0)
				sprintf(output,"%d",i);
			else
				sprintf(output,"%s x %d",output,i);
            continue;
        }else
            i += 1; 
    }while(n > 1);
	n = atoi(data);
	sprintf(data,"%s = %d\0",output,n);
}
