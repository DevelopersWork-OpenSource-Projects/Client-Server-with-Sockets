int createfile(char filename[],int count){
  int i;
	FILE *file = fopen(filename,"w");
	if(file != NULL){
		int n = 255;
		for(i=0;i<count;i++){
			char num[6] = "";
			n = randomnumber(255,n);
			sprintf(num,"%d\n",n);
			fputs(num,file);
		}
		fclose(file);
	}
	else{
		perror(filename);
		return 0;
	}
	return 1;
}
