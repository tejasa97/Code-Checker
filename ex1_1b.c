/* C Program to calculate the sum of every third integer using while loop */

#include <stdio.h>

int main()
{
	int sum = 0, i = 2;

	while (i < 100){
		sum = sum+i;
		i = i + 3;
	}
	printf("The sum is : %d\n", sum);

}
