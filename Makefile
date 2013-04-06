CC = cc
CFLAGS = -O2 -march=native -std=c99
LEX = lex
objects = brainhelp.o
destination = /usr/local/bin/brainhelp
bh_destination = /usr/local/bin/bh
bf_destination = /usr/local/bin/bf #bf interpreter
awibh_destination = /usr/local/bin/awibh

all:brainhelp bf awibh

brainhelp:$(objects)
	$(CC) -o brainhelp $(CFLAGS) $(objects)

bf:bf.c
	$(CC) -o bf $(CFLAGS) bf.c 2>/dev/null

awibh:examples/awibh.bh
	./brainhelp examples/awibh.bh awibh.bf
	awib <awibh.bf >awibh.c
	$(CC) -o awibh awibh.c
	rm awibh.bf awibh.c

.PHONY:clean indent install uninstall
clean:
	-rm $(objects) brainhelp
	-rm bf
	-rm awibh

indent:
	indent -npro -kr -i8 -ts8 -sob -l80 -ss -ncs -cp1 -o brainhelp.c brainhelp.c
	indent -npro -kr -i8 -ts8 -sob -l80 -ss -ncs -cp1 -o bf.c bf.c

install:all
	cp brainhelp $(destination)
	cp bh.py $(bh_destination)
	chmod +x $(bh_destination)
	cp bf $(bf_destination)
	cp awibh $(awibh_destination)

uninstall:
	-rm $(destination)
	-rm $(bh_destination)
	-rm $(bf_destination)
	-rm $(awibh_destination)
