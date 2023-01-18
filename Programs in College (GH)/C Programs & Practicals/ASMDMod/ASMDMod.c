#include<stdio.h>
#include<conio.h>
#include<math.h>
void main()
{
    int a,b,result;
    char choice;
    printf("Enter the two numbers(Press Enter after each entry.):");
    scanf("%d %d",&a,&b);
    printf(" + add\n - subtract\n * multiply\n / divide\n %% modulus\n Enter symbol to perform operation:");
    choice=getche();
    printf("\n");
    switch(choice)
    {
    	case'+':result=a+b;
    	printf("Sum= %d",result);
    	break;
    	case'-':result=a-b;
    	printf("Difference= %d",result);
    	break;
    	case'*':result=a*b;
    	printf("Product= %d",result);
    	break;
    	case'/':result=a/b;
    	printf("Quotient= %d",result);
    	break;
    	case'%':result=a%b;
    	printf("Remainder= %d",result);
    	break;
    	default:printf("Invalid Choice");
	}
	getch();
}
