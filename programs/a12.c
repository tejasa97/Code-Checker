/*c program to print entered year is leap year or not*/

#include<stdio.h>
int main()
{
	int num;
	printf("enter the year");
	scanf(" %d ", &num);
	if (num % 4 == 0) {
		if (num % 100 == 0) {
			if (num % 400 == 0)
				printf("entered year is leap year\n");
			else
				printf("entered year is not a leap year\n");
		} else
			printf("entered year is leap year\n");
	} else
		printf("entered year is not a leap year\n");
}
