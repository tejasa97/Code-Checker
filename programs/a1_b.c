/*c script to calculate sum of every 3rd integer i=2 and i<100 for do while
loop*/

#include<stdio.h>
int main()
{
	int sum = 0, i = 2;
	do {
		sum += i;
		i += 3;
		} while (i < 100);
	printf("sum of every third integer:%d\n", sum);
}
