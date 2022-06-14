CC=gcc
CFLAGS=-Wall -pedantic -Wextra -std=c99 -O2 -fPIE
all: amdctl
%.o: %.c
	$(CC) -c -o $@ $< $(CFLAGS)
