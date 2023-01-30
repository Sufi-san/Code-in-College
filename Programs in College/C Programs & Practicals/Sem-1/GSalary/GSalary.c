#include<stdio.h>
#include<conio.h>
void main()
{
	float bs,gs;
	printf("Enter the basic salary:");
	scanf("%f",&bs);
	if(bs>=10000)
	{
		gs=bs*(110/100)+bs*(20/100)+500;
		printf("Gross salary = %f",gs);
	}
	else if(bs>=5000)
	{
	    gs=bs*(100/100)+bs*(15/100)+400;
	    printf("Gross salary = %f",gs);
	}
	else
	{
		gs=bs*(90/100)+bs*(10/100)+300;
		printf("Gross salary = %f",gs);
	}
	getch();
}
