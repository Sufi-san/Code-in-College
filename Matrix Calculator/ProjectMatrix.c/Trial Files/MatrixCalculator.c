#include <stdio.h>
#include <math.h>
#include <matrixlib.h>

void mainMenu();

int main()
{
    int choice;
    printf("\n\tWelcome to Matrix Calculator!");
    do
    {
        mainMenu();
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            addMat();
            break;
        case 2:
            subtMat();
            break;
        case 3:
            multMat();
            break;
        case 4:
            scalMultMat();
            break;
        case 5:
            detMat();
            break;
        case 6:
            transMat();
            break;
        case 7:
            invMat();
            break;
        case 8:
            printf("Thank You for using Matrix Calculator\n");
            break;
        default:
            printf("Invalid Choice\n");
        }
    } while (choice != 8);

    return 0;
}

void mainMenu()
{
    printf("\n\n\tChoose an Operation:\n\n\t1.Add Two Matrices\n\t2.Subtract Two Matrices\n\t3.Multiply Two Matrices");
    printf("\n\t4.Multiply Matrix by Scalar\n\t5.Determinant of Matrix\n\t6.Transpose of Matrix\n\t7.Inverse of Matrix\n\t8.Exit\n\n");
}