/*c script to calculate the sum of every 3rd integer i=2 and i=100 using for
  loop*/

#include<stdio.h>

int main()
{
	int sum = 0, i = 2;
	for (i = 2; i < 100; i++)
	{
		sum += i;
		i += 2;
	}
	printf("sum of every third integer:%d\n", sum);
}
