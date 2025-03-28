#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <wait.h>

#define MAX_INPUT_LINE 150 //increased to fix parsing issue
#define MAX_NUM_TOKENS 8
#define MAX_COMMANDS 4

//prototypes
int read_in(char*);
void piping(int, char*);

int main(){
    char lines[MAX_INPUT_LINE];
    int num_coms = read_in(lines);
    piping(num_coms, lines);
    
    return EXIT_SUCCESS;
}

int read_in(char* lines){
    /*reads all inputted lines into a single string*/
    
    ssize_t pos = 0;
    int num_tok = 0;
    
    while (num_tok < MAX_COMMANDS){
        ssize_t input = read(0, lines+pos, MAX_INPUT_LINE);
        
        if ((input==1)  && !num_tok){ //if no input, end program
            exit(EXIT_FAILURE);
        }else if(input==1){ //if enter hit, assume no more commands
            break;
        }
        num_tok++;
        pos += (input);
        lines[pos-1] = '|';
    }
    return num_tok;
}

void piping(int num_com, char* lines){
    /*executes commands*/
    char* cur_com;
    char* tokens;
    int pipes[2 * (num_com-1)];
    int pid;
    int status;
    char* envp[] = {0};
    char* args[MAX_NUM_TOKENS];
    
    cur_com = strtok(lines, "|");
    
    //create all pipes (even i are read ends, odd i are write ends)
    for (int i=0; i<(num_com-1); i++){
        pipe(i*2 + pipes); 
    }
    
    for (int i=0; i<num_com; i++){
        if ((pid = fork()) == 0){ //if child created
            if (i > 0){
                //dupe read end of prev command to stdin
                dup2(pipes[(i-1)*2], 0);
            }
            if (i < (num_com-1)){
                //dupe write end of cur command to stdout
                dup2(pipes[i*2 + 1], 1);
            }

            for (int j=0; j<(2*(num_com-1)); j++){
                close(pipes[j]); //close child's pipe ends
            }

            //separate and store all arguments of ith command
            int argi = 0;
            tokens = strtok(cur_com, " ");
            while (tokens != NULL){
                args[argi] = tokens;
                tokens = strtok(NULL, " ");
                argi++;
            }
            args[argi] = NULL; //set null terminator as per execve spec
            
            //execute ith command
            execve(args[0], args, envp);
        }
        cur_com = strtok(NULL, "|");
    }
    
    for (int i=0; i<(2*(num_com-1)); i++){
        close(pipes[i]); //close parent's pipe ends
    }
    
    for (int i=0; i<num_com; i++){
        waitpid(pid, &status, 0); //wait for child to finish
    }
}

