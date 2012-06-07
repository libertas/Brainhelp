CC=gcc
Library=Brainhelp_Shared.so
CC_FLAGS=-o $(Library) -fpic -shared -O2
OBJECT=brainhelp


brainhelp:brainhelp.py $(Library)
	cp brainhelp.py $(OBJECT)
	chmod +x brainhelp

$(Library):Shared.c
	$(CC) $(CC_FLAGS)

clean:
	rm $(OBJECT) $(Library)
