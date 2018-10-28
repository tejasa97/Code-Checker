/*c program to print binary of a given number */
#include<stdio.h>
/*int convert(int);*/
int convert(int num)
{
	if (num != 0)
		return num % 2 + 10 * convert(num / 2);
	else
		return 0;
}
int main()
{
	int num, bin, rev;
	printf("\nenter the number: ");
	scanf("%d", &num);
	bin = convert(num);
	printf("the binary equivalent of %d is %d.", num, bin);
	printf("\n");
}


