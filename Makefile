CC = cc
CFLAGS = -O2 -march=native -std=c99
objects = brainhelp.o
destination = /usr/local/bin/brainhelp
bh_destination = /usr/local/bin/bh

brainhelp:brainhelp.o
	$(CC) -o brainhelp $(CFLAGS) $(objects)


.PHONY:clean indent install uninstall
clean:
	-rm $(objects)
	-rm brainhelp

indent:
	indent -npro -kr -i8 -ts8 -sob -l80 -ss -ncs -cp1 -o brainhelp.c brainhelp.c

install:brainhelp bh.py
	cp brainhelp $(destination)
	cp bh.py $(bh_destination)
	chmod +x $(bh_destination)

uninstall:
	-rm $(destination)
	-rm $(bh_destination)
