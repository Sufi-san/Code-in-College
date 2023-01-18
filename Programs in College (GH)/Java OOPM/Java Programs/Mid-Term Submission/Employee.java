import java.util.Scanner;

public class Employee {

  Scanner sc = new Scanner(System.in);
  int empID;
  String empContactNumber, empName;

  void enterInfo() {
    System.out.println("Enter Employee Information\n");
    System.out.println("Enter Employee ID");
    empID = sc.nextInt();
    sc.nextLine();
    System.out.println("Enter Employee Name");
    empName = sc.nextLine();
    System.out.println("Enter Contact Number");
    empContactNumber = sc.nextLine();
    System.out.println("\n\n");
  }

  void showInfo() {
    System.out.println("Employee ID: " + empID);
    System.out.println("Employee Name: " + empName);
    System.out.println("Emp Contact no: " + empContactNumber + "\n");
  }
}
