#include<stdio.h>
#include<conio.h>
void main()
{
	int a=0,b=1,c,i,n;
	printf("Enter the number of terms to be displayed from the Fibonacci series:");
	scanf("%d",&n);
	printf("\n Fibonacci Series(%d terms) : \n0\n1\n",n);
	for(i=1;i<=n-2;i++)
	{
		c = a+b;
		printf("%d\n",c);
		a=b;
		b=c;
	}
	getch();
}
