/*
 * linkedlist.c
 *
 * Based on the implementation approach described in "The Practice 
 * of Programming" by Kernighan and Pike (Addison-Wesley, 1999).
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "emalloc.h"
#include "list.h"


node_t *new_node(char *name, int birth_year) {
    assert( name != NULL);

    node_t *temp = (node_t *)emalloc(sizeof(node_t));

    temp->name       = strdup(name);
    temp->birth_year = birth_year;
    temp->next       = NULL;

    return temp;
}


node_t *add_front(node_t *list, node_t *new) {
    new->next = list;
    return new;
}


node_t *add_end(node_t *list, node_t *new) {
    node_t *curr;

    if (list == NULL) {
        new->next = NULL;
        return new;
    }

    for (curr = list; curr->next != NULL; curr = curr->next);
    curr->next = new;
    new->next = NULL;
    return list;
}

node_t *add_inorder(node_t * list, node_t *new) {
    //initialize empty pointers
    node_t *prev = NULL;
    node_t *curr = NULL;
    
    if (list == NULL){
        return new;
    }
    for (curr = list; curr != NULL; curr = curr->next) {
        if ((new->birth_year) == (curr->birth_year)){
            //if birth years equal, check whose name comes first
            if (strcmp(new->name, curr->name) > 0){
                prev = curr;
            }else{
                break;
            }
        }else if((new->birth_year) > (curr->birth_year)){
                //if given birth year > curr, check next person in list
                prev = curr;
        }else{
            break;
        }
    }
    
    new->next = curr;

    if (prev == NULL) {
        return (new);
    }else{
        prev->next = new;
        return list;
    }
}


node_t *peek_front(node_t *list) {
    return list;
}


node_t *remove_front(node_t *list) {
    if (list == NULL) {
        return NULL;
    }

    return list->next;
}


void apply(node_t *list,void (*fn)(node_t *list, void *),void *arg){
    for ( ; list != NULL; list = list->next) {
        (*fn)(list, arg);
    }
}
