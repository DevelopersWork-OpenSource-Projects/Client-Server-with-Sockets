#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<strings.h>

#include<sys/wait.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<arpa/inet.h>

#include "factor.c"

#define max 255

main(int argc,char *argv[]){
	if(argc < 2){
		perror("incorrect number of parameters passed\n");
		exit(0);
	}
	int sockfd;
	sockfd = socket(AF_INET,SOCK_STREAM,0);
	if(sockfd < 0){
		perror("socket creation failed\n");
		exit(0);
	}
	struct sockaddr_in server;
	bzero((char *)&server,sizeof(server));
	server.sin_port = htons(atoi(argv[1]));
	server.sin_family = AF_INET;
	server.sin_addr.s_addr = INADDR_ANY;
	if((bind(sockfd,(struct sockaddr *)&server,sizeof(server))) < 0){
		perror("binding socket failed\n");
		exit(0);
	}
	listen(sockfd,10);
	printf("server started\n");
	int clientid = 0;
	while(clientid != -1){
		struct sockaddr_in client;
		bzero((char *)&client,sizeof(client));
		int clen;
		int connectionfd;
		clen = sizeof(client);
		connectionfd = accept(sockfd,(struct sockaddr *)&client,&clen);
		if(connectionfd < 0){
			perror("client connection failed\n");
			continue;
		}
		clientid += 1;
		int pid = fork();
		if(pid < 0){
			perror("too many clients to handle\n");
			wait(0);
		}
		int i;
		if(pid==0){
			char buffer[max];
			bzero((char *)buffer,sizeof(buffer));
			sprintf(buffer,"%d",clientid);
			printf("%d : new client in line\n",clientid);
			send(connectionfd,buffer,strlen(buffer),0);
			for(i=0;i<6;i++){
				sleep(2);
				bzero((char *)buffer,sizeof(buffer));
				recv(connectionfd,buffer,max,0);
				printf("%d : got the input %s",clientid,buffer);
				getfactors(buffer);
				sleep(1);
				send(connectionfd,buffer,strlen(buffer),0);
				printf("%d : sent the output %s\n",clientid,buffer);
			}
			close(connectionfd);
			exit(0);
		}
		
	}
	waitpid(-1,0,0);
	close(sockfd);

	return 1;
}
