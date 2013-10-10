#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <openssl/sha.h>
#include <netdb.h>
#include <unistd.h>
#include <regex.h>
#include <fcntl.h>


int main(int agrc, char *argv[]) {

  int socketfd = socket(PF_INET, SOCK_STREAM, 0);
  //SCKDGRAM - UDP, STREAM - TCP

  char buffer[256];
  char* adres = "192.168.1.6";
  struct hostent *server;
  struct sockaddr_in server_addr;

  server = gethostbyname(argv[1]);

  server_addr.sin_port=htons(atoi(argv[2]));
  bcopy((char *)server->h_addr,(char *)&server_addr.sin_addr.s_addr,server->h_length);
  //server_addr.sin_addr.s_addr = inet_addr(adres);
  server_addr.sin_family = PF_INET;

  if(socketfd) {
    int c = connect(socketfd, (struct sockaddr*)&server_addr, sizeof(server_addr));
    memset(&buffer[0], 0, sizeof(buffer));
    strcat(buffer, "inf106582");
    int i = write(socketfd, buffer, 255);
    memset(&buffer[0], 0, sizeof(buffer));
    read(socketfd, buffer, 255);
    printf("%d\n", i);
    printf("%s\n", buffer);
  } else {
    printf("Blad wszystkiego.");
  }

  return 0;
}
