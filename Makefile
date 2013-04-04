CC = cc
CFLAGS = -O2 -march=native -std=c99
LEX = lex
objects = brainhelp.o
destination = /usr/local/bin/brainhelp
bh_destination = /usr/local/bin/bh
bf_destination = /usr/local/bin/bf #bf interpreter

brainhelp:$(objects) bf brainhelp_pre
	$(CC) -o brainhelp $(CFLAGS) $(objects)

brainhelp_pre:brainhelp_pre.c
	$(CC) -o brainhelp_pre $(CFLAGS) brainhelp_pre.c

brainhelp_pre.c:preprocessor.l
	$(LEX) -o brainhelp_pre.c preprocessor.l

bf:bf.c
	$(CC) -o bf $(CFLAGS) bf.c 2>/dev/null

.PHONY:clean indent install uninstall
clean:
	-rm $(objects) brainhelp
	-rm bf
	-rm brainhelp_pre.c brainhelp_pre

indent:
	indent -npro -kr -i8 -ts8 -sob -l80 -ss -ncs -cp1 -o brainhelp.c brainhelp.c
	indent -npro -kr -i8 -ts8 -sob -l80 -ss -ncs -cp1 -o bf.c bf.c

install:brainhelp bh.py bf
	cp brainhelp $(destination)
	cp bh.py $(bh_destination)
	chmod +x $(bh_destination)
	cp bf $(bf_destination)

uninstall:
	-rm $(destination)
	-rm $(bh_destination)
	-rm $(bf_destination)
