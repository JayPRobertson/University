#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LEN 20

//tokenize a str into words
/*INPUT: "This is a str", OUPTPUT:
Word: This
Word: is
Word: a
Word: str
*/

int main(int argc, char *argv[]) { //expects str from user
    char *line = NULL;
    char *t;
    int  num = 0;

    if (argc < 2) {
        fprintf(stderr, "usage: %s <some string>\n", argv[0]);
        exit(1);
    }

    line = (char *)malloc(sizeof(char) * MAX_LEN); //define space of size MAX_LEN 
    if (line == NULL) {
        fprintf(stderr,
            "Argh. Something bad happened with malloc. :-(\n");
    }

    strcpy(line, argv[1]); //copying content of first arg to line

    t = strtok(line, " "); //differentiate words based on spaces
    while (t) {
        num++;
        printf("Word: %s\n", t);
        t = strtok(NULL, " ");
    }
  
    printf("Number of words: %d\n", num);
 
    exit(0); 
}
