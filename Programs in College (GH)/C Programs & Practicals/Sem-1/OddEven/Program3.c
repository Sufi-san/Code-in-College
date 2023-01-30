#include<stdio.h>
#include<conio.h>
void main()
{
	int n;
	printf("Enter the number to be checked:");
	scanf("%d",&n);
	if(n&1 == 1)
	{
		printf("\n The entered number is odd.");
	}
	else
	{
		printf("\n The entered number is even.");
	}
	getch();
}
