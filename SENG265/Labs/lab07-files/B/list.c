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


node_t *new_node(char *val) {
    assert( val != NULL);

    node_t *temp = (node_t *)emalloc(sizeof(node_t)); //using emalloc
    //give emalloc the type data you want to reserve space for

    strncpy(temp->word, val, MAX_WORD_LEN); //copy value of val to word
    //space for word is defined in list.h
    temp->next = NULL;

    return temp;
}


node_t *add_front(node_t *list, node_t *new) { 
    //arguments: pointer to start of list, instance of new node
    new->next = list; //ref to next elem in list is the current list
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


node_t *peek_front(node_t *list) {
    return list;
}


node_t *remove_front(node_t *list) {
    if (list == NULL) {
        return NULL;
    }

    return list->next;
}



void apply(node_t *list,
           void (*fn)(node_t *list, void *),
           void *arg)
{
    for ( ; list != NULL; list = list->next) {
        (*fn)(list, arg);
    }
}
