# include <stdio.h> 

int main()
{
    
    int i,j,row,col,Dmt;
    printf("Rows of Matrix = ");
    scanf("%d",&row);
    printf("Columns of Matrix = ");
    scanf("%d",&col);

    int a[row][col];
    if(row == col)
    {
        printf("Enter the elements of the matrix:\n");
        for(i = 0;i<row;i++)
        {
            for(j = 0;j<col;j++)
            {
              printf("a[%d][%d] = ",i+1,j+1);
              scanf("%d",&a[i][j]);
            }
        }
    }
    else
    printf("Operation not possible.");
    return 0;
}