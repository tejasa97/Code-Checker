/*c program to print Armstrong numbers between 100 to 500 */

#include<stdio.h>

int main()
{
	int num, rem, sum, temp;
	printf(" Armstrong numbers are: ");
	for (num = 100; num <= 500; num++) {
		temp = num;
		sum = 0;
		while (temp != 0) {
			rem = temp % 10;
			temp /= 10;
			sum = sum + (rem * rem * rem);
		}
		if (sum == num)
			printf("%d,", num);
	}
	printf("\n");
}
