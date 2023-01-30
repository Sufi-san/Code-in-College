#include <stdio.h>
#include <conio.h>
int main()
{
    int n, m, i, u;
    int p[20], w[20];
    float x[20];
    float optimal = 0.0;
    printf("Enter number of objects:");
    scanf("%d", &n);
    printf("Enter capacity of KnapSack:");
    scanf("%d", &m);
    printf("Enter profits in decreasing order of Pi/Wi: \n");
    for (i = 1; i <= n; i++)
        scanf("%d", &p[i]);
    printf("Enter Weights in decreasing order of Pi/Wi: \n");
    for (i = 1; i <= n; i++)
        scanf("%d", &w[i]);
    for (i = 1; i <= n; i++)
        x[i] = 0.0;
    u = m;
    for (i = 1; i <= m; i++)
    {
        if (w[i] > u)
            break;
        else
            x[i] = 1.0;
        u = u - w[i];
    }
    if (i <= n)
        x[i] = (float)u / w[i];
    printf("The x values are\n");
    for (i = 1; i <= n; i++)
        printf("%f\t", x[i]);
    for (i = 1; i <= n; i++)
        optimal = optimal + p[i] * x[i];
    printf("\nOptimal Solution is %f", optimal);
    getch();
}