/*c program to reverse the bits of a given number */

#include<stdio.h>
#include<stdlib.h>
#define int_bits (sizeof(int)*8)
/*void printnbinary(unsigned int );*/
/*print data in binary*/
void printbinary(unsigned int n)
{
	short int i;
	for (i = (int_bits - 1); i >= 0; i--)
		(n & (1 <<  i)) ? printf(" 1 ") : printf(" 0 ");
}

/*unsigned int reversebits(unsigned int );*/
unsigned int reversebits(unsigned int num)
{
	unsigned int j = 0, tmp = 0;
	int num_loop = (int_bits - 1);
	for (j = 0; j < num_loop; j++) {
		tmp |= num & 1;
		num >>= 1;
		tmp <<= 1;
		/*if((num & (1 << j)));
		  {tmp |=1 << ((int_bits-1) - j);}*/ 
	}
	return tmp;
}

int main()
{
	unsigned int num = 0, rev = 0;
	printf("\nenter the number: ");
	scanf("%u", &num);
	printf("\n\nbinary data is : ");
	printbinary(num);
	rev = reversebits(num);
	printf("\n\nreverse of data is: ");
	printbinary(rev);
	return 0;
}
