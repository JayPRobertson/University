CC = gcc
CFLAGS = -Wall -Wextra -g

OBJ1 = feedbackq.o
OBJ2 = queue.o

all: schedule

schedule: $(OBJ1) $(OBJ2)
	$(CC) $(CFLAGS) -o schedule $(OBJ1) $(OBJ2)

feedbackq: $(OBJ2) $(OBJ3)
	$(CC) $(CFLAGS) -o feedbackq $(OBJ2)

feedbackq.o: feedbackq.c $(OBJ3)
	$(CC) $(CFLAGS) -c feedbackq.c

queue.o: queue.c queue.h
	$(CC) $(CFLAGS) -c queue.c

clean:
	rm -rf *.o schedule