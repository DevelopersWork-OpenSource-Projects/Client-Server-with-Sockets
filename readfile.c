#include<sys/time.h>
#define max 255
char buffer[max];
int readfile(char filename[],int connectionfd){
	struct timeval start,end;
	FILE *file = fopen(filename,"r");
	if (file != NULL){
		char line[max];
		bzero((char *)line,max);
		while(fgets(line, max, file) != NULL){
			gettimeofday(&start,NULL);
			send(connectionfd,line,strlen(line),0);
			bzero((char *)buffer,sizeof(buffer));
			recv(connectionfd,buffer,max,0);
			printf("factors are %s\n",buffer);
			gettimeofday(&end,NULL);
			printf("throughput time is %lu ms\n",(end.tv_usec-start.tv_usec));
		}
		fclose(file);
	}
	else{
		perror(filename);
		return 0;
	}
	return 1;
}
