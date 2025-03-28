CC = gcc
CFLAGS = -Wall -Wextra -g

OBJ1 = fetch-info.o
OBJ2 = pipe4.o

all: $(OBJ1) $(OBJ2)
	$(CC) $(CFLAGS) -o fetch-info $(OBJ1)
	$(CC) $(CFLAGS) -o pipe4 $(OBJ2)

fetch-info: $(OBJ1)
	$(CC) $(CFLAGS) -o fetch-info $(OBJ1)

pipe4: $(OBJ2)
	$(CC) $(CFLAGS) -o pipe4 $(OBJ2)

fetch-info.o: fetch-info.c
	$(CC) $(CFLAGS) -c fetch-info.c

pipe4.o: pipe4.c
	$(CC) $(CFLAGS) -c pipe4.c

clean:
	rm -f $(OBJ1) fetch-info
	rm -f $(OBJ2) pipe4
