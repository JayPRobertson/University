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
    assert( val != NULL); //tests if condition is true, else stops execution

    node_t *temp = (node_t *)emalloc(sizeof(node_t));

    temp->word = strdup(val);
    temp->next = NULL;

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
    //initiallize empty variables
    node_t *prev = NULL;
    node_t *curr = NULL;
    
    //determine where in linked list new node should be inserted (using prev, cur)
    if (list == NULL) {
        return new; //if list is empty, make new node and don't do formatting
    }
    
    for (curr = list; curr != NULL; curr = curr->next) {
        //in assignment 3, need to modify following comparison for cases where
        //comparing str vs comparing int
        if (strcmp(new->word, curr->word) > 0) {
            //if word comes after the current one, check prev
            prev = curr;
        } else {
            break;
        }
    }
    
    //update link fields
    new->next = curr;

    if (prev == NULL) {
        return (new);
    } else {
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



void apply(node_t *list,
           void (*fn)(node_t *list, void *),
           void *arg)
{
    for ( ; list != NULL; list = list->next) {
        (*fn)(list, arg);
    }
}
