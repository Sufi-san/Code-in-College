#include<stdio.h>
#include<conio.h>
#define Pi 3.142
int main()
{
	float radius,Area,circumference,diameter;
	printf("Enter the radius of circle :");
	scanf("%f",&radius);
	diameter = 2 * radius;
	circumference = 2 * Pi * radius;
	Area = Pi *radius *radius;
	printf("\nDiameter of circle = %f",diameter);
	printf("\nCircumference of circle = %f",circumference);
	printf("\nArea of circle = %f",Area);
	
	getch();
}
