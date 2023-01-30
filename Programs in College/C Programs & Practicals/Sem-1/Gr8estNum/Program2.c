#include<stdio.h>
#include<conio.h>
void main()
{
	int a,b,c,greatest;
	printf("Enter the three numbers(Press Enter after each entry):");
	scanf("%d%d%d",&a,&b,&c);
	greatest = (a>b)?((a>c)?a:c):((b>c)?b:c);
	printf("The largest number entered is : %d",greatest);
	getch();
}
