/** @file q_array_rotate.c
 *  @brief Submission program for Lab 04.
 *  @author Mike Z.
 *  @author Felipe R.
 *  @author Hausi M.
 *  @author Jose O.
 *  @author Saasha J.
 *  @author Victoria L.
 *  @author Robertson J.
 *
 */
#include <stdio.h>
#include <stdlib.h>

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
int main(int argc, char *argv[]){

        // variable to store the final answer
        int factorial = 1;

        // check that the number of arguments is correct
	if (argc != 2) {
 		printf("Incorrect number of arguments");
  		exit(1);
	}

        // takes the command line input and converts it into int.
        int num = atoi(argv[1]);
	
	//check that the argument is a number
	if ((num == 0) && (argv[1] != "0")){
		printf("Argument not an integer");
		exit(1);
	}
	
       for (int i=1; i <= num; i++){
		factorial *= i;
	} 

        printf("%d\n", factorial); // %d\n sepcifies to print out a number
	return 0;
}
