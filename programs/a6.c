/* c program to print multiplication table of given number */

#include<stdio.h>

int main()
{
	int n, i;
	printf("enter the number: ");
	scanf(" %d ", &n);
	for (i = 1; i <= 10; i++)
		printf("\n %d * %d = %d", n, i, n * i);
	printf("\n");
}
