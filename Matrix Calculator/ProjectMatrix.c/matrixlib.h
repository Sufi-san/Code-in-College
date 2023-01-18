void addMat()
{
    int row1, col1, row2, col2;

    printf("Rows of MatA = ");
    scanf("%d", &row1);
    printf("Columns of MatA = ");
    scanf("%d", &col1);
    printf("\nRows of MatB = ");
    scanf("%d", &row2);
    printf("Columns of MatB = ");
    scanf("%d", &col2);
    float a[row1][col1], b[row2][col2];
    if (row1 == row2 && col1 == col2)
    {
        for (int i = 0; i < row1; i++)
        {
            for (int j = 0; j < col1; j++)
            {
                printf("a[%d][%d] = ", i + 1, j + 1);
                scanf("%f", &a[i][j]);
            }
        }
        printf("\n");
        for (int i = 0; i < row2; i++)
        {
            for (int j = 0; j < col2; j++)
            {
                printf("b[%d][%d] = ", i + 1, j + 1);
                scanf("%f", &b[i][j]);
            }
        }

        printf("\nMatrix A:\n");
        for (int i = 0; i < row1; i++)
        {
            for (int j = 0; j < col1; j++)
            {
                printf(" %.2f", a[i][j]);
            }
            printf("\n");
        }
        printf("\nMatrix B:\n");
        for (int i = 0; i < row2; i++)
        {
            for (int j = 0; j < col2; j++)
            {
                printf(" %.2f", b[i][j]);
            }
            printf("\n");
        }

        printf("\nMatrix A + Matrix B: \n");
        for (int i = 0; i < row1; i++)
        {
            for (int j = 0; j < col1; j++)
            {
                printf(" %.2f", a[i][j] + b[i][j]);
            }
            printf("\n");
        }
        printf("\n");
    }
    else
        printf("\nOperation not possible.");
}

void subtMat()
{
    int row1, col1, row2, col2;

    printf("Rows of MatA = ");
    scanf("%d", &row1);
    printf("Columns of MatA = ");
    scanf("%d", &col1);
    printf("\nRows of MatB = ");
    scanf("%d", &row2);
    printf("Columns of MatB = ");
    scanf("%d", &col2);
    float a[row1][col1], b[row2][col2];
    if (row1 == row2 && col1 == col2)
    {
        for (int i = 0; i < row1; i++)
        {
            for (int j = 0; j < col1; j++)
            {
                printf("a[%d][%d] = ", i + 1, j + 1);
                scanf("%f", &a[i][j]);
            }
        }
        printf("\n");
        for (int i = 0; i < row2; i++)
        {
            for (int j = 0; j < col2; j++)
            {
                printf("b[%d][%d] = ", i + 1, j + 1);
                scanf("%f", &b[i][j]);
            }
        }

        printf("\nMatrix A:\n");
        for (int i = 0; i < row1; i++)
        {
            for (int j = 0; j < col1; j++)
            {
                printf(" %.2f", a[i][j]);
            }
            printf("\n");
        }
        printf("\nMatrix B:\n");
        for (int i = 0; i < row2; i++)
        {
            for (int j = 0; j < col2; j++)
            {
                printf(" %.2f", b[i][j]);
            }
            printf("\n");
        }

        printf("\nMatrix A - Matrix B: \n");
        for (int i = 0; i < row1; i++)
        {
            for (int j = 0; j < col1; j++)
            {
                printf(" %.2f", a[i][j] - b[i][j]);
            }
            printf("\n");
        }
        printf("\n");
    }
    else
        printf("\nOperation not possible.");
}

void detMat()
{
    int i, j, choice, row, col;
    float Dmt;
    printf("Select Dimension of Matrix:(Enter 1 or 2)\n");
    printf("1. 2 X 2\n2. 3 X 3\n");
    scanf("%d", &choice);
    switch (choice)
    {
    case 1:
        row = 2;
        col = 2;
        break;
    case 2:
        row = 3;
        col = 3;
        break;
    default:
        printf("\nInvalid choice.\n");
        break;
    }

    float a[row][col];
    printf("\nEnter the elements of the matrix:\n");
    for (i = 0; i < row; i++)
    {
        for (j = 0; j < col; j++)
        {
            printf("a[%d][%d] = ", i + 1, j + 1);
            scanf("%f", &a[i][j]);
        }
    }
    printf("\nThe Entered Matrix is:\n");
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            printf(" %.2f", a[i][j]);
        }
        printf("\n");
    }
    if (row == 2 && col == 2)
    {
        Dmt = (a[0][0] * a[1][1]) - (a[0][1] * a[1][0]);
    }
    else if (row == 3 && col == 3)
    {
        Dmt = a[0][0] * ((a[1][1] * a[2][2]) - (a[1][2] * a[2][1])) - a[0][1] * ((a[1][0] * a[2][2]) - (a[1][2] * a[2][0])) + a[0][2] * ((a[1][0] * a[2][1]) - (a[1][1] * a[2][0]));
    }
    printf("\nThe determinant for the given matrix is:\n%.2f", Dmt);
}

void transMat()
{
    int i, j, row, col;
    printf("Rows of Matrix = ");
    scanf("%d", &row);
    printf("Columns of Matrix = ");
    scanf("%d", &col);

    float a[row][col], transpose[row][col];
    printf("Enter elements of matrix:\n");
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            printf("a[%d][%d] = ", i + 1, j + 1);
            scanf("%f", &a[i][j]);
        }
    }
    printf("\nThe Entered Matrix is:\n");
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            printf(" %.2f", a[i][j]);
        }
        printf("\n");
    }
    printf("\nThe transpose of the matrix is:\n");
    for (int i = 0; i < col; i++)
    {
        for (int j = 0; j < row; j++)
        {
            transpose[i][j] = a[j][i];
            printf(" %.2f", transpose[i][j]);
        }
        printf("\n");
    }
}
void multMat()
{
    int i, j, row1, col1, row2, col2, k;

    printf("Rows of MatA = ");
    scanf("%d", &row1);
    printf("Columns of MatA = ");
    scanf("%d", &col1);
    printf("\nRows of MatB = ");
    scanf("%d", &row2);
    printf("Columns of MatB = ");
    scanf("%d", &col2);

    float a[row1][col1], b[row2][col2], p[row1][col2];

    if (col1 == row2)
    {
        printf("\nEnter elements of Matrix A:\n");
        for (i = 0; i < row1; i++)
        {
            for (j = 0; j < col1; j++)
            {
                printf("a[%d][%d] = ", i + 1, j + 1);
                scanf("%f", &a[i][j]);
            }
        }
        printf("\nEnter elements of Matrix B:\n");
        for (i = 0; i < row2; i++)
        {
            for (j = 0; j < col2; j++)
            {
                printf("b[%d][%d] = ", i + 1, j + 1);
                scanf("%f", &b[i][j]);
            }
        }
        printf("\nMatrix A:\n");
        for (int i = 0; i < row1; i++)
        {
            for (int j = 0; j < col1; j++)
            {
                printf(" %.2f", a[i][j]);
            }
            printf("\n");
        }
        printf("\nMatrix B:\n");
        for (int i = 0; i < row2; i++)
        {
            for (int j = 0; j < col2; j++)
            {
                printf(" %.2f", b[i][j]);
            }
            printf("\n");
        }
        printf("\nMatrix A * Matrix B: \n");
        for (i = 0; i < row1; i++)
        {
            for (j = 0; j < col2; j++)
            {
                p[i][j] = 0;
                for (k = 0; k < col1; k++)
                {
                    p[i][j] += a[i][k] * b[k][j];
                }
                printf(" %.2f", p[i][j]);
            }
            printf("\n");
        }
    }
    else
        printf("\nOperation not possible.");
}

void scalMultMat()
{
    int i, j, row, col;
    float k;
    printf("Rows of Matrix = ");
    scanf("%d", &row);
    printf("Columns of Matrix = ");
    scanf("%d", &col);

    float a[row][col];

    printf("\nEnter the scalar for multiplication:");
    scanf("%f", &k);
    printf("Enter elements of matrix:\n");
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            printf("a[%d][%d] = ", i + 1, j + 1);
            scanf("%f", &a[i][j]);
        }
    }
    printf("\nThe Entered Matrix is:\n");
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            printf(" %.2f", a[i][j]);
        }
        printf("\n");
    }
    printf("\nThe result of multiplication of Matrix by Scalar is:\n");
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            printf(" %.2f", k * a[i][j]);
        }
        printf("\n");
    }
}

void invMat()
{
    int i, j, choice, row, col;
    float Dmt;
    printf("Select Dimension of Matrix:(Enter 1 or 2)\n");
    printf("1. 2 X 2\n2. 3 X 3\n");
    scanf("%d", &choice);
    switch (choice)
    {
    case 1:
        row = 2;
        col = 2;
        break;
    case 2:
        row = 3;
        col = 3;
        break;
    default:
        printf("\nInvalid choice.\n");
        break;
    }

    float a[row][col];
    printf("\nEnter the elements of the matrix:\n");
    for (i = 0; i < row; i++)
    {
        for (j = 0; j < col; j++)
        {
            printf("a[%d][%d] = ", i + 1, j + 1);
            scanf("%f", &a[i][j]);
        }
    }
    printf("\nThe Entered Matrix is:\n");
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            printf(" %.2f", a[i][j]);
        }
        printf("\n");
    }
    if (row == 2 && col == 2)
    {
        Dmt = (a[0][0] * a[1][1]) - (a[0][1] * a[1][0]);
    }
    else if (row == 3 && col == 3)
    {
        Dmt = a[0][0] * ((a[1][1] * a[2][2]) - (a[1][2] * a[2][1])) - a[0][1] * ((a[1][0] * a[2][2]) - (a[1][2] * a[2][0])) + a[0][2] * ((a[1][0] * a[2][1]) - (a[1][1] * a[2][0]));
    }
    if (Dmt == 0)
    {
        printf("\nThe matrix is singular, and does not have an inverse.\n");
    }
    else if (row == 2 && col == 2)
    {
        float inv[row][col], adj[row][col];

        adj[0][0] = a[1][1];
        adj[0][1] = -a[0][1];
        adj[1][0] = -a[1][0];
        adj[1][1] = a[0][0];

        for (i = 0; i < row; i++)
        {
            for (j = 0; j < col; j++)
            {
                inv[i][j] = (adj[i][j]) / Dmt;
            }
        }
        printf("\n The Inverse of given matrix is:\n");
        for (i = 0; i < row; i++)
        {
            for (j = 0; j < col; j++)
            {
                printf(" %.2f", inv[i][j]);
            }
            printf("\n");
        }
    }
    else if (row == 3 && col == 3)
    {
        float inv[row][col], adj[row][col];

        adj[0][0] = (a[1][1] * a[2][2] - a[1][2] * a[2][1]);
        adj[0][1] = -((a[0][1] * a[2][2] - a[0][2] * a[2][1]));
        adj[0][2] = (a[0][1] * a[1][2] - a[0][2] * a[1][1]);
        adj[1][0] = -((a[1][0] * a[2][2] - a[1][2] * a[2][0]));
        adj[1][1] = (a[0][0] * a[2][2] - a[0][2] * a[2][0]);
        adj[1][2] = -((a[0][0] * a[1][2] - a[0][2] * a[1][0]));
        adj[2][0] = (a[1][0] * a[2][1] - a[1][1] * a[2][0]);
        adj[2][1] = -((a[0][0] * a[2][1] - a[0][1] * a[2][0]));
        adj[2][2] = (a[0][0] * a[1][1] - a[0][1] * a[1][0]);

        for (i = 0; i < row; i++)
        {
            for (j = 0; j < col; j++)
            {
                inv[i][j] = (adj[i][j]) / Dmt;
            }
        }
        printf("\n The Inverse of given matrix is:\n");
        for (i = 0; i < row; i++)
        {
            for (j = 0; j < col; j++)
            {
                printf(" %.2f", inv[i][j]);
            }
            printf("\n");
        }
    }
}
