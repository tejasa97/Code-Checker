/* c program to convert a character lower to upper case and vicaversa */

#include<stdio.h>

int main()
{
	char ch;
	printf("input a character: ");
	scanf(" %c ", &ch);
	/*while( s[c]='\0')
	  ch=s[c];*/
	if (ch >= 'A' && ch <= 'Z')
		ch += 32;
	else if (ch >= 'a' && ch <= 'z')
		ch -= 32;
	printf(" %c\n", ch);
}
