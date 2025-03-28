#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/time.h>
#include <unistd.h>

#define PROCESS_ERR ("Process number %d not found.\n")
#define MAX_LINE_LEN 256 //arbitrary

//Prototypes
void print_process(int);
void print_system();
void format_dates(char* point);


int main(int argc, char *argv[]){
    if(argc > 1){
        int process_num = atoi(strtok(argv[1], "=")); //get first arg
        print_process(process_num);
    }else{
        print_system();
    }
    return EXIT_SUCCESS;
}

void print_process(int pid){
    /*Prints process information for a process with pid*/
    char line[MAX_LINE_LEN]; 
    char filepath[MAX_LINE_LEN]; 
    FILE* file;
    char* temp; //a multi-use temporary variable for storing data
    int context_switch = 0;

    snprintf(filepath, sizeof(filepath), "/proc/%d/comm", pid);
    file = fopen(filepath, "r");
    
    //stop program if process DNE
    if (file == NULL){
            printf(PROCESS_ERR, pid);
            exit(EXIT_FAILURE);
    }

    //print process number and name
    printf("Process number:   %d\n", pid);
    fgets(line, MAX_LINE_LEN, file);
    printf("Name:   %s", line);
    fclose(file);
    
    //print filenname
    snprintf(filepath, MAX_LINE_LEN, "cat /proc/%d/cmdline", pid);
    file = popen(filepath, "r");
    if(fgets(line, MAX_LINE_LEN, file) == NULL){
         printf("Filename (if any):\n"); //if no filename exists
    }else{
         printf("Filename (if any):    %s\n", line);
    }
    
    //print threads and context_switches
    snprintf(filepath, MAX_LINE_LEN, "/proc/%d/status", pid);
    file = fopen(filepath, "r");
    while (fgets(line, MAX_LINE_LEN, file)) {
            //searches lines for ones beginning with following terms
            if (!strncmp(line, "Threads:", 8)) {
                //if found, get data and print it
                temp = strtok(line, "Threads:	");
                printf("Threads:    %d\n", atoi(temp));
            }
            if (!strncmp(line, "voluntary", 9)){
                temp = strtok(line, ":");
                temp = strtok(NULL, ":");
                context_switch += atoi(temp);
            }
            if (!strncmp(line, "nonvoluntary", 12)){
                temp = strtok(line, ":");
                temp = strtok(NULL, ":");
                context_switch += atoi(temp);
                break;
                
            }
        }
    printf("Total context switches:   %d\n", context_switch); 
    fclose(file);
}

void print_system(){
    /*prints system information*/
    char line[MAX_LINE_LEN];
    FILE* file;
    char* temp; //a multi-use temporary variable for storing data
    
    //print model name
    file = popen("grep 'model name' /proc/cpuinfo", "r"); //get command output
    fgets(line, MAX_LINE_LEN, file);
    temp = strtok(line, ":"); //isolate data
    temp = strtok(NULL, ":");
    printf("model name: %s", temp);
    fclose(file);
    
    //print cpu cores
    file = popen("grep 'cpu cores' /proc/cpuinfo", "r");
    fgets(line, MAX_LINE_LEN, file);
    temp = strtok(line, ":");
    temp = strtok(NULL, ":");
    printf("cpu cores: %s", temp);
    fclose(file);
    
    //print linux version
    file = popen("grep 'Linux version' /proc/version", "r");
    fgets(line, MAX_LINE_LEN, file);
    temp = strstr(line, "Linux version ") + strlen("Linux version ");
    printf("Linux version: %s", temp);
    fclose(file);
    
    //print total memory
    file = popen("grep 'MemTotal' /proc/meminfo", "r");
    fgets(line, MAX_LINE_LEN, file);
    temp = strtok(line, ":"); 
    temp = strtok(NULL, ":");
    printf("MemTotal: %s", temp);
    fclose(file);
    
    //print formatted uptime
    file = popen("cat /proc/uptime", "r");
    fgets(line, MAX_LINE_LEN, file);
    temp = strtok(line, " "); //isolate first number (total uptime)
    format_dates(temp); //converts to formatted string and updates temp
    printf("Uptime: %s", temp);
    fclose(file);
}

void format_dates(char* point){
    //converts time in seconds to formatted time string
    int uptime = atoi(point);
    int days = uptime/86400;
    int hours = (uptime % 86400)/3600;
    int minutes = (uptime % 3600)/60;
    int seconds = uptime % 60;
    
    //updates value pointed to by point with formatted string
    snprintf(point, MAX_LINE_LEN, "%d days, %d hours, %d minutes, %d seconds\n", days, hours, minutes, seconds);
}




