CC = cc
CFLAGS = -O2 -march=native -std=c99
objects = brainhelp.o
destination = /usr/local/bin/brainhelp

brainhelp:brainhelp.o
	$(CC) -o brainhelp $(CFLAGS) $(objects)


.PHONY:clean indent install uninstall
clean:
	-rm $(objects)
	-rm brainhelp

indent:
	indent -npro -kr -i8 -ts8 -sob -l80 -ss -ncs -cp1 -o brainhelp.c brainhelp.c

install:brainhelp
	cp brainhelp $(destination)

uninstall:
	rm $(destination)
