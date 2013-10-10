#include <stdio.h>
#include <strings.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>


int main(int agrc, char *argv[]) {
  int socketfd = socket(PF_INET, SOCK_STREAM, 0);
  //SCKDGRAM - UDP, STREAM - TCP

  char buffer[256];
  char* adres = "192.168.1.6";
  char* index = "106525";
  struct hostent *server;
  struct sockaddr_in server_addr;

  server = gethostbyname(argv[1]);

  server_addr.sin_port=htons(atoi(argv[2]));

  bcopy((char *)server->h_addr,(char *)&server_addr.sin_addr.s_addr,server->h_length);
  printf("siema\n");

  server_addr.sin_family = PF_INET;

  if(socketfd) {
    int c = connect(socketfd, (struct sockaddr*)&server_addr, sizeof(server_addr));
    bzero(buffer, 256);
    strcat(buffer, "inf106525");
    int w = write(socketfd, buffer, 255);
    bzero(buffer, 256);
    int i = read(socketfd, buffer, 255);
    printf("%s\n", buffer);
  } else {
    printf("Blad wszystkiego.");
  }

  return 0;
}
