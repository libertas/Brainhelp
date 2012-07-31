OBJECT=brainhelp


brainhelp:brainhelp.py $(Library)
	cp brainhelp.py $(OBJECT)
	chmod +x brainhelp

install:
	cp ./brainhelp /usr/local/bin/brainhelp

clean:
	rm $(OBJECT) $(Library)
