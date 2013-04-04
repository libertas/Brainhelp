#include <stdio.h>
#include <string.h>
#define INPUT_LENGTH 256
#define PRINT_LENGTH (INPUT_LENGTH*INPUT_LENGTH)

FILE *fpin = NULL, *fpout = NULL;

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

int bf_clean(int obj)
{
	go(obj);
	fprintf(fpout, "[-]");
	return 0;
}

int p2rd(int obj)
{
	go(obj);
	fprintf(fpout, "[->+>+<<]>[-<+>]<\n");
	return 0;
}

int rd2p(int obj)
{
	go(obj);
	fprintf(fpout, ">>[-<<+>>]<<\n");
	return 0;
}

int bf_movp(int obj, int sub)
{
	p2rd(sub);
	bf_clean(obj);
	rd2p(obj);
	return 0;
}

int bf_addp(int obj, int sub)
{
	p2rd(sub);
	go(obj);
	fprintf(fpout, ">>[-<<+>>]<<\n");	//add rd to p
	return 0;
}

int bf_add(int obj, int number)
{
	go(obj);
	for (int i = 0; i < number; i++)
		fprintf(fpout, "+");
	fprintf(fpout, "\n");
	return 0;
}

int bf_subp(int obj, int sub)
{
	p2rd(sub);
	go(obj);
	fprintf(fpout, ">>[-<<->>]<<\n");
	return 0;
}

int bf_sub(int obj, int number)
{
	go(obj);
	for (int i = 0; i < number; i++)
		fprintf(fpout, "-");
	fprintf(fpout, "\n");
	return 0;
}

int bf_mov(int obj, int number)	//move the number into the memory
{
	bf_clean(obj);
	bf_add(obj, number);
	return 0;
}

int bf_putc(int obj)
{
	go(obj);
	fprintf(fpout, ".\n");
	return 0;
}

int bf_getc(int obj)
{
	go(obj);
	fprintf(fpout, ",\n");
	return 0;
}

int bf_not(int obj)
{
	go(obj);
	fprintf(fpout, "[->+<]+>[<[-]>[-]]<\n");
	return 0;
}

int bf_print(char *msg)
{
	fprintf(fpout, ">");
	for (int i = 0; i < strlen(msg); i++) {
		for (char j = 0; j < msg[i]; j++)
			fprintf(fpout, "+");
		fprintf(fpout, ".");
		fprintf(fpout, "[-]");
	}
	fprintf(fpout, "++++++++++.[-]<\n");
	return 0;
}

int stack[PRINT_LENGTH] = { 0 };

int stack_c = 0;
int push(int p)
{
	stack[stack_c] = p;
	stack_c++;
	return 0;
}

int pop()
{
	stack_c--;
	return stack[stack_c];
}

int bf_if(int addr)
{
	go(addr);
	fprintf(fpout, "if[\n");
	push(addr);
	return 0;
}

int bf_endif()
{
	int addr = pop();
	go(addr);
	fprintf(fpout, "[-]]endif\n");
	return 0;
}

int bf_loop(int addr)
{
	go(addr);
	fprintf(fpout, "loop[\n");
	push(addr);
	return 0;
}

int bf_endloop()
{
	int addr = pop();
	go(addr);
	fprintf(fpout, "]endloop\n");
	return 0;
}

int bf_code(char *code)
{
	fprintf(fpout, "\nhard writted:%s\n", code);
	return 0;
}

int main(int argc, char **argv)	//USAGE: brainhelp [INPUT] [OUTPUT]
{
	//checking args
	if (argc != 3) {
		fpin = stdin;
		fpout = stdout;
	} else if ((fpin = fopen(argv[1], "r")) != 0) {
		fpout = fopen(argv[2], "w");
	} else {
		fprintf(stderr, "brainhelp:input error\n");
		return 1;
	}

	//starting
	char buffer[INPUT_LENGTH];	// [pointer][helper][data][steps]
	// [rp]         [rh]    [rd]    [rs]
	while (1) {
		fscanf(fpin, "%s", buffer);

		if (strcmp(buffer, "") == 0 || strcmp(buffer, "end") == 0)
			break;

		else if (strcmp(buffer, "movp") == 0) {
			int sub, obj;
			fscanf(fpin, "%d,%d", &obj, &sub);
			bf_movp(obj, sub);
		}

		else if (strcmp(buffer, "mov") == 0) {
			int obj, number;
			fscanf(fpin, "%d,%d", &obj, &number);
			bf_mov(obj, number);
		}

		else if (strcmp(buffer, "clean") == 0) {
			int obj;
			fscanf(fpin, "%d", &obj);
			bf_clean(obj);
		}

		else if (strcmp(buffer, "addp") == 0) {
			int obj, sub;
			fscanf(fpin, "%d,%d", &obj, &sub);
			bf_addp(obj, sub);
		}

		else if (strcmp(buffer, "add") == 0) {
			int obj, number;
			fscanf(fpin, "%d,%d", &obj, &number);
			bf_add(obj, number);
		}

		else if (strcmp(buffer, "subp") == 0) {
			int obj, sub;
			fscanf(fpin, "%d,%d", &obj, &sub);
			bf_subp(obj, sub);
		}

		else if (strcmp(buffer, "sub") == 0) {
			int obj, number;
			fscanf(fpin, "%d,%d", &obj, &number);
			bf_sub(obj, number);
		}

		else if (strcmp(buffer, "putc") == 0) {
			int obj;
			fscanf(fpin, "%d", &obj);
			bf_putc(obj);
		}

		else if (strcmp(buffer, "getc") == 0) {
			int obj;
			fscanf(fpin, "%d", &obj);
			bf_getc(obj);
		}

		else if (strcmp(buffer, "not") == 0) {
			int obj;
			fscanf(fpin, "%d", &obj);
			bf_not(obj);
		}

		else if (strcmp(buffer, "if") == 0) {
			int obj;
			fscanf(fpin, "%d", &obj);
			bf_if(obj);
		}

		else if (strcmp(buffer, "endif") == 0) {
			bf_endif();
		}

		else if (strcmp(buffer, "loop") == 0) {
			int obj;
			fscanf(fpin, "%d", &obj);
			bf_loop(obj);
		}

		else if (strcmp(buffer, "endloop") == 0) {
			bf_endloop();
		}

		else if (strcmp(buffer, "print") == 0) {
			char msg[PRINT_LENGTH];
			fscanf(fpin, " %[^\n]", msg);
			bf_print(msg);
		}

		else if (strcmp(buffer, "bfcode") == 0) {
			char msg[PRINT_LENGTH];
			fscanf(fpin, " %[^\n]", msg);
			bf_code(msg);
		}

		else {
			fprintf(stderr,"Error:%s\n", buffer);
			break;
		}

		for (int i = 0; i < INPUT_LENGTH; i++)
			buffer[i] = (char)0;
	}

	//ending
	return 0;
}
