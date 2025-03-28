/** @file song_analyzer.c
 *  @brief A pipes & filters program that uses conditionals, loops, and string processing tools in C to process song
 *  data and printing it in a different format.
 *  @author Felipe R.
 *  @author Hausi M.
 *  @author Angadh S.
 *  @author Juan G.
 *  @author Robertson J.
 *
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * @brief The maximum line length.
 *
 */
#define MAX_LINE_LEN 185

#define RANGE_ERR ("Question number out of range [1,5]")
#define MISSARG_ERR ("Missing argument")
#define FILEOPEN_ERR ("Error in opening file: ")

#define OUTFILE ("output.csv")
#define ARGV_SEPARATE ("=")
#define CSV_SEPARATE (",")
#define ARGV_QUESTION_INDEX 1
#define ARGV_DATA_INDEX 2 
#define ARGC_NUM 3 //desired number of command line arguments passed

/**
 * Function: main
 * --------------
 * @brief The main function and entry point of the program.
 *
 * @param argc The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @return int 0: No errors; 1: Errors produced.
 *
 */
 
//prototypes
void check_args(int);
FILE* open_files(char*);
void readlines(FILE*, int, FILE*);
void writefile(char*, char*, FILE*);

int main(int argc, char *argv[]){
    check_args(argc); //check if correct amount of arguments
    
    //isolate given arguments into data (str) and question (int)
    char* data = strtok(argv[ARGV_DATA_INDEX], ARGV_SEPARATE);
    data = strtok(NULL, ARGV_SEPARATE);
    char* question_str = strtok(argv[ARGV_QUESTION_INDEX], ARGV_SEPARATE);
    question_str = strtok(NULL, ARGV_SEPARATE);
    int question = atoi(question_str);
    
    //open given file data and create outfile "output.csv"
    FILE* fileopen = open_files(data);
    FILE* outfile = open_files(OUTFILE);
    
    fprintf(outfile,"Artist(s),Song\n"); //create header in outfile
    readlines(fileopen, question, outfile); //read given file line by line
    
    //close files
    fclose(fileopen);
    fclose(outfile);
    
    return EXIT_SUCCESS;

}

void check_args(int argc){
    //determines if there are the correct amount of arguments
    //if > 3 arguments, program uses first 3 arguments and ignores rest
    if(argc < ARGC_NUM){
        printf(MISSARG_ERR);
        exit(EXIT_FAILURE);
    }
}

FILE* open_files(char* filename){
    //opens a given file if possible and returns a pointer to it
    FILE* fileopen = NULL;
    
    if(!strcmp(filename, OUTFILE)){
        fileopen = fopen(filename, "w");
    }else{
        fileopen = fopen(filename, "r");
    }
     
    if (filename == NULL){
            printf(FILEOPEN_ERR, filename);
            exit(EXIT_FAILURE);
    }
    
    return fileopen;
}

void readlines(FILE* filename, int question, FILE* outfile){
    /* reads filename line by line -> determines if line contains a song
       matching the question parameters; if yes, writes out artist and 
       song title to outfile */
       
    char line[MAX_LINE_LEN];
    char* song;
    char* artists;
    char* token;
    fgets(line, MAX_LINE_LEN, filename); //read off header line in file
    
    while(fgets(line, MAX_LINE_LEN, filename) != NULL){ 
        song = strtok(line, CSV_SEPARATE);
        artists = strtok(NULL, CSV_SEPARATE);
    
        switch(question){
            case 1: //cur artist is Rae Spoon
                if(!strcmp(artists, "Rae Spoon")){
                    goto write_file;
                }
                break;
            case 2: //cur artists is Tate McRae
                if(!strcmp(artists, "Tate McRae")){
                   goto write_file;
                }
                break;
            case 3: //cur artist is The Weeknd and song in Major key
                //get mode from line
                for(int i=0; i<6; i++){
                    token = strtok(NULL, CSV_SEPARATE);
                }
                char* mode = token;
        
                if(!strcmp(artists, "The Weeknd") && !strcmp(mode, "Major\n")){
                    goto write_file;
                }
                break;
            case 4: //cur song in >5000 playlists and in key of A or D
                //get number of spotify playlists from line
                for(int i=0; i<3; i++){
                    token = strtok(NULL, CSV_SEPARATE);
                }
                int playlists = atoi(token);
                
                //get key from line
                for(int i=0; i<2; i++){
                    token = strtok(NULL, CSV_SEPARATE);
                }
                char* key = token;
                
                if(playlists >= 5000 && (!strcmp(key, "A") || !strcmp(key, "D"))){
                    goto write_file;
                }
                break;
            case 5: //cur song published in 2021 or 2022 and Drake is one of artists
                for(int i=0; i<2; i++){
                    token = strtok(NULL, CSV_SEPARATE);
                }
                char* year = token;
                char* ptr = strstr(artists, "Drake");
                
                if (ptr != NULL && (!strcmp(year,"2021") || !strcmp(year,"2022"))){
                    goto write_file;
                }
                break;
            default:
                //if question number not in range [1,5]
                printf(RANGE_ERR);
                exit(EXIT_FAILURE);
            }
        
        continue;
        
        write_file: 
            writefile(artists, song, outfile);      
    }  
}

void writefile(char* artists, char* song, FILE* outfile){
    //format info as: "artist, song\n" and write out
    fprintf(outfile, artists); 
    fprintf(outfile, ","); 
    fprintf(outfile, song); 
    fprintf(outfile, "\n"); 
}