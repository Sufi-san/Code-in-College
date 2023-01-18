#include<stdio.h> 
#include<conio.h> 
void main()
{ 
int a,b; 
void swap(int *p1, int *p2); 
printf("Enter two numbers:"); 
scanf("%d %d", &a, &b); 
printf("The values of a and b in the main function before calling the swap function are %d and %d \n",a,b); 
swap(&a, &b); 
printf("The values of a and b in the main function after calling the swap function are %d and %d \n" ,a ,b); 
getch();
}
void swap(int *pl,int *p2) 
{
int temp;
temp=*pl; 
*pl=*p2; 
*p2=temp; 
printf("The values of a and b in the swap function after swapping are %d and %d \n",*pl,*p2);
}
