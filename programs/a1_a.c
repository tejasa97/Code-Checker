/*c progrqam to calculate sum of every 3rd integer i=2 to i<100 for while loop*/

#include<stdio.h>
int main()
{
	int i = 2, sum = 0;
	while (i < 100) {
		sum = sum + i;
		i += 3;
	} //Need
	printf("sum of every third integer: %d\n", sum);
}
