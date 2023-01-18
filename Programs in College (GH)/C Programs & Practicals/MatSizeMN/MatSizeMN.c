#include<stdio.h>
#include<conio.h>
void main()
{
	int m,n,i,j,a[10][10],b[10][10],c[10][10];
	printf("Enter the number of rows and columns:");
	scanf("%d%d",&m,&n);
	printf("Enter the elements of Matrix 1:\n");
	for(i=0;i<=m-1;i++)
	{
		for(j=0;j<=n-1;j++)
		{
			printf("Enter a value :");
			scanf("%d",&a[i][j]);
		}
	}
	printf("Enter the elements of Matrix 2:\n");
	for(i=0;i<=m-1;i++)
	{
		for(j=0;j<=n-1;j++)
		{
			printf("Enter a value :");
			scanf("%d",&b[i][j]);
		}
	}
		for(i=0;i<=m-1;i++)
	{
		for(j=0;j<=n-1;j++)
		{
			c[i][j]=a[i][j]+b[i][j];
		}
	}
	printf("The sum of the two matrices is: \n");
		for(i=0;i<=m-1;i++)
	{
		for(j=0;j<=n-1;j++)
		{
			printf("%d\t",c[i][j]);
		}
		printf("\n");
	}
	getch();
}
