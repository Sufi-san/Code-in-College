# include <stdio.h> 

int main()
{
    int i,j,row,col;
    printf("Rows of Matrix = ");
    scanf("%d",&row);
    printf("Columns of Matrix = ");
    scanf("%d",&col);

    int a[row][col],transpose[row][col];
    printf("Enter elements of matrix:\n");
    for(int i = 0;i<row;i++)
    {
        for(int j = 0;j<col;j++)
        {
            printf("a[%d][%d] = ",i+1,j+1);
            scanf("%d",&a[i][j]);
        }
    }
    printf("The matrix is as follows:\n");
    for(int i = 0;i<row;i++)
    {
        for(int j = 0;j<col;j++)
        {
            printf(" %d",a[i][j]);
        }
        printf("\n");
    }
     printf("The transpose of the matrix is:\n");
    for(int i = 0;i<col;i++)
    {
        for(int j = 0;j<row;j++)
        {
           transpose[i][j] = a[j][i];   
           printf(" %d",transpose[i][j]);
        }
       printf("\n");
    }
    return 0;
}