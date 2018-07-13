/*c program to find sum of digits of a given number*/

#include <stdio.h>
int main()
{
	int num, sum = 0, rem = 0;
	printf(" enter the number : ");
	scanf(" %d ", &num);
	while (num != 0) {
		rem = num % 10;
		num /= 10;
		sum += rem;
	}
	printf("sum of the digit in number = %d\n", sum);
}
