#include<stdio.h>
#include<conio.h>
#include<math.h>
void main()
{
	int i,fact=1,sign=-1;
	float x,numerator,sum,term;
	printf("Enter an angle in degrees:");
	scanf("%f",&x);
	printf("The value of angle %.2lf in radian is %f",x,x*3.142/180);
	x=x*3.142/180;
	term=x;
	sum=term;
	for(i=3;term>=0.0000001;i=i+2)
	{
		fact=fact*i*(i-1);
		numerator=pow(x,i);
		term=numerator/fact;
		sum=sum+sign*term;
		sign=sign*-1;
	}
	printf("\nThe value of sin(%f) is %f",x,sum);
	getch();
}
