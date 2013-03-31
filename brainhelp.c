#include <stdio.h>
#include <string.h>
#define INPUT_LENGTH 256

FILE *fpin, *fpout;

int go(int place)
{
	static int here = 0;
	int steps;
	steps = place - here;
	if (steps > 0) {
		fprintf(fpout, ">>>");
		for (int i = 0; i < steps; i++)
			fprintf(fpout, "+");
		fprintf(fpout, "[->[-<<<+>>>]<[->+<]<[->+<]>>]<<<\n");
		here += steps;
	} else if (steps < 0) {
		steps = 0 - steps;
		fprintf(fpout, ">>>");
		for (int i = 0; i < steps; i++)
			fprintf(fpout, "+");
		fprintf(fpout, "[-<[-<+>]>[-<+>]<<<[->>>+<<<]>>]<<<\n");
		here -= steps;
	}
	return 0;
}

int on_mov()
{
	int obj, sub;
	fscanf(fpin, "%d", &obj);
	fscanf(fpin, "%d", &sub);
	go(sub);
	fprintf(fpout, "[->+>+<<]>[-<+>]<\n");
	go(obj);
	fprintf(fpout, ">>[-<<+>>]<<\n");
	return 0;
}

int main(int argc, char **argv)	//USAGE: brainhelp [INPUT] [OUTPUT]
{
	//checking args
	if (argc != 3) {
		fpin = stdin;
		fpout = stdout;
	} else if ((fpin = fopen(argv[1], "r")) == 0){
		fpout = fopen(argv[2], "w");
	}
	else {
		fprintf(stderr, "brainhelp:input error\n");
		return 1;
	}

	//starting
	char buffer[INPUT_LENGTH];	// [pointer][helper][data][steps]
	while (fscanf(fpin, "%s", buffer)) {
		if (strcmp(buffer, "mov") == 0)
			on_mov();
	}

	//ending
	fclose(fpin);
	fclose(fpout);
	return 0;
}
