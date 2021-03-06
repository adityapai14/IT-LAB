#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {    
    int sockfd, portno=8080;
    struct sockaddr_in server, client;

    int n = socket(AF_INET, SOCK_STREAM, 0);
    if(n < 0) {
        printf("socket creation failed!");
        return EXIT_FAILURE;
    }
    
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = inet_addr("127.0.0.1");
    server.sin_port = htons(portno);

    if(connect(sockfd,(struct sockaddr *) &server, sizeof(server)) < 0) {
        printf("cant connect");
        return EXIT_FAILURE;
    }

    char fname[256],buffer[256];
    printf("Filename: "); scanf("%s",fname);
    write(sockfd, fname, sizeof(fname));
    
    recv(sockfd, buffer, sizeof(buffer), 0);
    printf("%s", buffer);
        
}