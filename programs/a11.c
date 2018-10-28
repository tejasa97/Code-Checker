/* c program to find given number is perfect number or not*/

#include<stdio.h>
int main()
{
	int num, sum = 0, i, temp;
	printf(" enter the number:");
	scanf(" %d ", &num);
	temp = num;
	for (i = 1; i <= temp - 1; i++) {
		if (temp % i == 0)
			sum += i;
	}
	if (sum == num)
		printf("\nentered number is perfect number");
	else
		printf("\nentered number is not perfect number");
	printf("\n");
}
