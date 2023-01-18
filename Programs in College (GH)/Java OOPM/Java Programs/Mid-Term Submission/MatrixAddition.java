import java.util.Scanner;

public class MatrixAddition {

  static void printArrays(int arr[][]) {
    int r = arr[0].length;
    int c = arr[0].length;
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        System.out.print(" " + arr[i][j]);
      }
      System.out.println();
    }
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int row, col;
    System.out.println("Enter no of rows and columns for matrix: ");
    row = sc.nextInt();
    col = sc.nextInt();
    int a[][] = new int[row][col];
    int b[][] = new int[row][col];
    int c[][] = new int[row][col];
    System.out.println("Enter elements of matrix A: ");
    for (int i = 0; i < row; i++) {
      for (int j = 0; j < col; j++) {
        a[i][j] = sc.nextInt();
      }
    }
    System.out.println("Enter elements of matrix B: ");
    for (int i = 0; i < row; i++) {
      for (int j = 0; j < col; j++) {
        b[i][j] = sc.nextInt();
      }
    }
    for (int i = 0; i < row; i++) {
      for (int j = 0; j < col; j++) {
        c[i][j] = a[i][j] + b[i][j];
      }
    }
    System.out.println("Matrix C:");
    printArrays(c);
  }
}
