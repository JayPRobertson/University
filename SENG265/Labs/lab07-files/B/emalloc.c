#include <stdlib.h>
#include <stdio.h>
#include "emalloc.h"

void *emalloc(size_t n) { //emalloc validates malloc but otherise works the same
    void *p; 

    p = malloc(n); 
    if (p == NULL) {
        fprintf(stderr, "malloc of %zu bytes failed", n); 
        exit(1);
    }   

    return p;
}
