/*factorial of a given number*/

#include<stdio.h>
/*long factorial(int);*/
long factorial(int x)
{
	int f = 1, i;
	for (i = x; i >= 1; i--)
		f *= i;
	return f;
}

int main()
{
	int a, fact;
	printf("enter any number: ");
	scanf(" %d ", &a);
	fact = factorial(a);
	printf(" factorial value of entered value: %d\n", fact);
}

