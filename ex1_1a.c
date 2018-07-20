/* A C program to calculate the sum of every third integer using for loop. */
#include<stdio.h>

int main()
{
	int sum = 0;
	int i = 0;

	for (i = 2; i < 100; i++) {
		sum = sum + i;
		i = i + 2;
	}

	printf("The sum is : %d", sum);
}
