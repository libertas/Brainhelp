CC = cc
CFLAGS = -O2 -march=native -std=c99
LEX = lex
objects = brainhelp.o
destination = /usr/local/bin/brainhelp
bh_destination = /usr/local/bin/bh
awibh_destination = /usr/local/bin/awibh

all:brainhelp awibh

brainhelp:$(objects)
	$(CC) -o brainhelp $(CFLAGS) $(objects)

awibh:awibh.c
	$(CC) -o awibh $(CFLAGS) awibh.c

awibh.c:examples/awibh.bh
	./brainhelp examples/awibh.bh awibh.bf
	$(CC) -o awibh $(CFLAGS) awibh.c
	./awibh <awibh.bf >awibh.c
	rm awibh.bf

.PHONY:clean indent install uninstall
clean:
	-rm $(objects) brainhelp
	-rm awibh

indent:
	indent -npro -kr -i8 -ts8 -sob -l80 -ss -ncs -cp1 -o brainhelp.c brainhelp.c

install:all
	cp brainhelp $(destination)
	cp bh.py $(bh_destination)
	chmod +x $(bh_destination)
	cp awibh $(awibh_destination)

uninstall:
	-rm $(destination)
	-rm $(bh_destination)
	-rm $(awibh_destination)
