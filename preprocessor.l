%{

#include <stdio.h>
#define LENGTH 256
int stop=0,usedefs=0,defs_c=0;
char defs[LENGTH][LENGTH]={0};
int defs_r[LENGTH];

int if_in_defs(char *text){
	for (int i = 0;i < LENGTH;i++) if(strcmp(defs[i],text)==0) return i;
	return -1;
}

%}
%%

[//] stop=1;

def {
	printf("def");
	usedefs=1;
	}

[\n] {
	stop=0;
	usedefs=0;
	printf("\n");
	}

. {
	if(usedefs==1){
		usedefs=2;
		strcpy(defs[defs_c],yytext);
	}
	if(usedefs==2){
		usedefs=0;
		sscanf("%d",yytext,defs_r+defs_c);
		defs_c++;
	}
	int number=if_in_defs(yytext);
	if(number!=-1) printf("%d",defs_r[number]);
	else continue;
	if(stop!=1) printf("%s",yytext);
	}
%%

int yywrap()
{
	return 1;
}

int main()
{
	yylex();
	return 0;
}
