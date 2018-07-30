/*c script to calculate the sum of every 3rd integer i=2 and i=100 using for
  loop*/

#include<stdio.h>

int main()
{
	int sum = 0, i = 2;
	for (i = 2; i < 100; i++) {
		sum += i;
		i += 2;
	}
	switch (sum) {
	case 1: printf("If sum is 1");
	break;
	case 2: printf("If sum is 2");
	break;
	default: printf("If none of these");
	//break;
	printf("sum of every third integer:%d\n", sum);
}
