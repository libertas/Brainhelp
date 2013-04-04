CC = cc
CFLAGS = -O2 -march=native -std=c99
objects = brainhelp.o
destination = /usr/local/bin/brainhelp
bh_destination = /usr/local/bin/bh
bf_destination = /usr/local/bin/bf #bf interpreter

brainhelp:$(objects) bf
	$(CC) -o brainhelp $(CFLAGS) $(objects)

bf:bf.c
	$(CC) -o bf $(CFLAGS) bf.c 2>/dev/null

.PHONY:clean indent install uninstall
clean:
	-rm $(objects)
	-rm brainhelp
	-rm bf

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
