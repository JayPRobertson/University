/** @file music_manager.c
 *  @brief A small program to analyze songs data.
 *  @author Mike Z.
 *  @author Felipe R.
 *  @author Hausi M.
 *  @author Juan G.
 *  @author Angadh S.
 *  @author Robertson J.
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"

#define MAX_LINE_LEN 200
#define OUTFILE ("output.csv")
#define ARGV_SEPARATE ("=")
#define CSV_SEPARATE (",")

#define LEN_WITH_LIMIT 7
#define NO_LIM -1

void inccounter(node_t*, void*);
void print_node(node_t*, void*);
void analysis(node_t *);

char* get_arg(char*);
FILE* open_files(char*);
node_t* get_node(char*, char*);
node_t* readlines(FILE*, char*, char*, char*, char*);
void writefile(node_t*, FILE*);
void filtered_write(node_t*, FILE*, char*, int);


/**
 * @brief The main function and entry point of the program.
 *
 * @param argc The number of arguments passed to the program.
 * @param argv The list of arguments passed to the program.
 * @return int 0: No errors; 1: Errors produced.
 *
 */
int main(int argc, char* argv[]){
    char* data = get_arg(argv[1]);
    
    //open given file data and create outfile "output.csv"
    FILE* fileopen = open_files(data);
    FILE* outfile = open_files(OUTFILE);
    
    //get a list of songs in fileopen that match CL argument specifications
    char* filter = get_arg(argv[2]);
    char* val = get_arg(argv[3]);
    char* order_by = get_arg(argv[4]);
    char* order = get_arg(argv[5]);
    node_t* list = readlines(fileopen, order_by, order, filter, val);
    
    //write out songs in list to outfile
    int limit;
    if(argc == LEN_WITH_LIMIT){    limit = atoi(get_arg(argv[6]));
    }else{                         limit = NO_LIM; //arbitrary val
    }
    filtered_write(list, outfile, order_by, limit);

    //release the space allocated for the list and other emalloc'ed elements
    node_t *temp_n = NULL;
    for (; list != NULL; list = temp_n){
        temp_n = list->next;
        free(list);
    }
    free(temp_n);
    
    //close files
    fclose(fileopen);
    fclose(outfile);

    return EXIT_SUCCESS;
}

/**
 * @brief Serves as an incremental counter for navigating the list.
 *
 * @param p The pointer of the node to print.
 * @param arg The pointer of the index.
 *
 */
void inccounter(node_t *p, void *arg){
    int *ip = (int *)arg;
    (*ip)++;
}

/**
 * @brief Allows to print out the content of a node.
 *
 * @param p The pointer of the node to print.
 * @param arg The format of the string.
 *
 */
void print_node(node_t *p, void *arg){
    char *fmt = (char *)arg;
    printf(fmt, p->song, p->artist, p->order);
}

/**
 * @brief Allows to print each node in the list.
 *
 * @param l The first node in the list
 *
 */
void analysis(node_t *l){
    int len = 0;
    apply(l, inccounter, &len);    
    printf("Number of songs: %d\n", len);
    apply(l, print_node, "%s by %s: %s\n");
}

/**
 * @brief Formats a command line argument as a str.
 *
 * @param argv A str formatted as --type="DATA".
 * @return arg A str formatted as "DATA".
 *
 */
char* get_arg(char* argv){
    char* arg = strtok(argv, ARGV_SEPARATE);
    arg = strtok(NULL, ARGV_SEPARATE);
    return arg;
}

/**
 * @brief Allows access to a given file.
 *
 * @param  filename The name of the file to open.
 * @return fileopen A pointer to the opened file.
 *
 */

FILE* open_files(char* filename){
    FILE* fileopen = NULL;
    
    if(!strcmp(filename, OUTFILE)){
        fileopen = fopen(filename, "w");
    }else{
        fileopen = fopen(filename, "r");
    }
    
    return fileopen;
}

/**
 * @brief Create a node_t representation of given song info.
 *
 * @param line A pointer to a str of song info separated by commas.
 * @param order_by A str corresponding to the column that will be ordered.
 *
 * @return cur_node A pointer to the created node.
 *
 */
node_t* get_node(char* line, char* order_by){
    char* token; //a placeholder to help iterate to needed lines
    char* song = strtok(line, CSV_SEPARATE);
    char* artists = strtok(NULL, CSV_SEPARATE);
    token = strtok(NULL, CSV_SEPARATE);
    int year = atoi(strtok(NULL, CSV_SEPARATE));
    int month = atoi(strtok(NULL, CSV_SEPARATE));
    int day = atoi(strtok(NULL, CSV_SEPARATE));
        
    //determine what column to keep for "order" param in node
    if (!strcmp(order_by, "STREAMS")){
        for(int i=0; i<2; i++){ //get streams
            token = strtok(NULL, CSV_SEPARATE);
        }
    }else if (!strcmp(order_by, "NO_SPOTIFY_PLAYLISTS")){
        token = strtok(NULL, CSV_SEPARATE); //get in_spotify_playlists
    }else{
        for(int i=0; i<3; i++){ //get in_apple_playlists
            token = strtok(NULL, CSV_SEPARATE);
        }
    }
        
    //make node
    node_t* cur_node = new_node(song, artists, year, month, day, token);
    return cur_node;
}

/**
 * @brief Reads songs into nodes from a csv file and adds them to a linked list
 *        if criteria is matched.
 *
 * @param filename A pointer to an opened file
 * @param order_by A str corresponding to the column that will be ordered.
 * @param order The order of order_by; either "DES" or "ASC".
 * @param filter A str corresponding to the column that will be filtered.
 * @param val What the filter column will be filtered by.
 *
 * @return list A pointer to the first node in a linked list of filtered songs.
 *
 */
node_t* readlines(FILE* filename, char* order_by, char* order, char* filter, char* val){
    //initialize needed variables
    char line[MAX_LINE_LEN];
    node_t *list = NULL;
    char* ptr;
    
    fgets(line, MAX_LINE_LEN, filename); //read off header line in file
    
    while(fgets(line, MAX_LINE_LEN, filename) != NULL){  
        line[strcspn(line, "\n")] = 0; //replace \n char with 0 terminator
        
        //make node for song in cur line
        ptr = line;
        node_t* cur_node = get_node(ptr, order_by);
        
        //check if cur_node should be added to list
        if(!strcmp(filter, "ARTIST")){
            if (strstr(cur_node->artist, val) != NULL){
                    list = add_inorder(list, cur_node, order);
                }else{
                    free(cur_node);
                } 
        }else{ //otherwise filter is "YEAR"
            if (cur_node->year == atoi(val)){
                    list = add_inorder(list, cur_node, order);
                }else{
                    free(cur_node);
                }
        } 
    }
    
    return list;
}

/**
 * @brief  Writes a formatted song line to a file.
 *
 * @param  cur_node A linked list node containing song info
 * @param  outfile A pointer to an opened file to write to.
 */
void writefile(node_t *cur_node, FILE* outfile){
    fprintf(outfile, "%d-%d-%d,", cur_node->year, cur_node->month, cur_node->day); 
    fprintf(outfile, "%s,%s,", cur_node->song, cur_node->artist); 
    fprintf(outfile, "%s\n", cur_node->order); 
}

/**
 * @brief Writes all song nodes out to a given file. If "limit" is a CL argument, 
 *        writes that many song nodes out instead.
 *
 * @param list A list of song nodes to write out.
 * @param argv The list of arguments passed to the program.
 * @param argc The number of arguments passed to the program.
 * @param outfile A pointer to the opened file to write to.
 *
 */
void filtered_write(node_t* list, FILE* outfile, char* order_by, int limit){
    //write out header
    fprintf(outfile, "released,track_name,artist(s)_name,");
    
    if       (!strcmp(order_by, "STREAMS")){               fprintf(outfile, "streams\n");
    }else if (!strcmp(order_by, "NO_SPOTIFY_PLAYLISTS")){  fprintf(outfile, "in_spotify_playlists\n");
    }else{                                                 fprintf(outfile, "in_apple_playlists\n");
    }
    
    //write out nodes in list
    node_t *temp_n = list;
    if (limit != NO_LIM){ //if "limit" is an arg
        for (int i=0; i<limit; i++){ //iterate through limit number of nodes
            writefile(temp_n, outfile);
            temp_n = temp_n->next;
        }
    }else{
        for (; temp_n != NULL; temp_n = temp_n->next){ //iterate through all nodes
            writefile(temp_n, outfile);
        }
    }
    free(temp_n);
}



