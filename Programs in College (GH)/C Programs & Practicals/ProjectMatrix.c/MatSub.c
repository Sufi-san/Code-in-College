#include <stdio.h> 

void main()
{
    int i = 0,j = 0,row1,col1,row2,col2,a[i][j],b[i][j];
  
    printf("Rows of MatA = ");
    scanf("%d",&row1);
    printf("Columns of MatA = ");
    scanf("%d",&col1);
    printf("\nRows of MatB = ");
    scanf("%d",&row2);
    printf("Columns of MatB = ");
    scanf("%d",&col2);
    if(row1 == row2 && col1 == col2)
    {
    for(i = 0;i<row1;i++)
    {
        for(j = 0;j<col1;j++)
        {
            printf("a[%d][%d] = ",i+1,j+1);
            scanf("%d",&a[i][j]);
        }
    }
    printf("\n");
    for(int i = 0;i<row2;i++)
    {
        for(int j = 0;j<col2;j++)
        {
            printf("b[%d][%d] = ",i+1,j+1);
            scanf("%d",&b[i][j]);
        }
    }
    printf("Difference of both matrices: \n");
    for(i = 0;i<row1;i++)
    {
        for(j = 0;j<col1;j++)
        {
            printf(" %d",a[i][j]-b[i][j]);
        }
        printf("\n");
    }
    }
    else
    printf("\nOperation not possible.");
}