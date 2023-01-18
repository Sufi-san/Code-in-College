#include <stdio.h> 

void main()
{
    int i,j,row1,col1,row2,col2,k;
  
    printf("Rows of MatA = ");
    scanf("%d",&row1);
    printf("Columns of MatA = ");
    scanf("%d",&col1);
    printf("\nRows of MatB = ");
    scanf("%d",&row2);
    printf("Columns of MatB = ");
    scanf("%d",&col2);
    
    int a[row1][col1],b[row2][col2],p[row1][col2];

    if(col1 == row2)
    {
    printf("\nEnter elements of matrix 1:\n");
    for(i = 0;i<row1;i++)
    {
        for(j = 0;j<col1;j++)
        {
            printf("a[%d][%d] = ",i+1,j+1);
            scanf("%d",&a[i][j]);
        }
    }
    printf("\nEnter elements of matrix 2:\n");
    for(i = 0;i<row2;i++)
    {
        for(j = 0;j<col2;j++)
        {
            printf("b[%d][%d] = ",i+1,j+1);
            scanf("%d",&b[i][j]);
        }
    }
    printf("Product of both matrices: \n");
    for(i = 0;i<row1;i++)
    {
        for(j = 0;j<col2;j++)
        {
            p[i][j]=0;
            for( k = 0;k < col1;k++)
            {
            p[i][j]+=a[i][k]*b[k][j];
            }
            printf(" %d",p[i][j]);
        }
        printf("\n");
    }
    }
    else
    printf("\nOperation not possible.");
}
