/* c program to reverse the digit of a given number*/

#include<stdio.h>

int main()
{
	int num, reverse = 0, rem = 0;
	printf("enter the number: ");
	scanf(" %d ", &num);
	while (num != 0) {
		rem = num % 10;
		num /= 10;
		reverse = reverse * 10 + rem;
	}
	printf("reverse of entered number : %d\n", reverse);
}
