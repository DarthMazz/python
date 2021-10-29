#include <stdio.h>
#include <stdlib.h>

char *result;

int reverse_bytes(int n, const char *buf)
{
    FILE* fp; 
    fp = fopen(buf, "r");
    if (fp == NULL)
    {
        return -1;
    }
    fclose(fp);
    return 0;
}

void free_result(void) {
  free(result);
}