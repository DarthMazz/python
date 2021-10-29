#include <stdlib.h>
#include <wchar.h>

int file_open(const char *path) {

    FILE* fp; 
    fp = fopen(path, "r");
    if (fp == NULL)
    {
        return -1;
    }
    fclose(fp);
    return 0;
}
