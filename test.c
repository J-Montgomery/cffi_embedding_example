#include <stdio.h>

extern char *decode(char *msg);

int main() {
    char *msg = decode(0);
    printf("msg: %s\n", msg);
    return 0;
}