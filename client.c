#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#include<unistd.h>
#include<netdb.h>
#include<time.h>

#include<sys/types.h>
#include<sys/wait.h>
#include<arpa/inet.h>
#include<sys/socket.h>

#include "randomnumber.c"
#include "createfile.c"
#include "readfile.c"

#define max 255
//char createfile;
char buffer[max];
int sockfd;
int connectionfd;
int n;
main(int argc,char *argv[]){
	if(argc < 3){
		perror("incorrect number of parameters passed\n");
		exit(0);
	}
	sockfd = socket(AF_INET,SOCK_STREAM,IPPROTO_TCP);
	if(sockfd < 0){
		perror("socket creation failed\n");
		exit(0);
	}
	struct sockaddr_in sockstruct;
	bzero((char *)&sockstruct,sizeof(sockstruct));
	sockstruct.sin_family = AF_INET;
	sockstruct.sin_port = htons(atoi(argv[2]));
	sockstruct.sin_addr.s_addr = inet_addr(argv[1]);
	connectionfd = connect(sockfd,(struct sockaddr *)&sockstruct,sizeof(sockstruct));
	if(connectionfd < 0){
		perror("failed connecting to server\n");
		return 0;
	}
	printf("connected to server\n");
	bzero((char *)buffer,sizeof(buffer));
	recv(sockfd,buffer,max,0);
	 n = atoi(buffer);
	printf("id at server is %d\n",n);
	char filename[20] = "";
	sprintf(filename,"client%d.inputdat",n);
	if(!createfile(filename,6)){
		perror("unable to create a file\n");
		return 0;
	}

	if(!readfile(filename,sockfd)){
		perror("connection with server is no more\n");
		return 0;
	}
	close(sockfd);
	return 1;
}
