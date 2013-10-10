#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>

// in order not to forget :)
// struct in_addr{
//  u_long s_addr; // 32-bitowy adres
// }

// struct sockaddr_in{
//  u_short sin_family; // PF_INET - zawsze
//  u_short sin_port; // numer porstu
//  struct in_addr sin_addr; // adres wezla
//  char sin_zero[8]; // pomijamy
// }

int main(){
  struct sockaddr_in sa;
  struct hostent *host;
  char buffer[256];
  host = gethostbyname("siema");

  int fd = socket(PF_INET, SOCK_STREAM, 0);

  if(fd){
    sa.sin_family = PF_INET;
    sa.sin_port = htons(13);

    // bcopy((char *) host->h_addr, (char *)&sa.sin_addr.s_addr, 4);
    bcopy((char *)host->h_addr,(char *)&sa.sin_addr.s_addr,host->h_length);
    printf("blalblalblalbl\n");

    int c = connect(fd, (struct sockaddr*) &sa, sizeof(struct sockaddr_in));

    memset(&buffer[0], 0, sizeof(buffer));
    read(fd, buffer, 256);
    printf("%s", buffer);
  } else {
    printf("Nie.\n");
  }
  return 0;
}
