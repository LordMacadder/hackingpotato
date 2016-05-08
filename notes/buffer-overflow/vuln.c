#include <stdio.h>

int main(int argc, char *argv[]) {
  char buffer[64];
  if (argc < 2) {
    prinf("syntax error\r\n");
    printf("must supply at-least one argument\r\n")
    return(1)
  }
  strcpy(buffer,argv[1]);
  return(0);
}
