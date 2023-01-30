class Student2 {

  private String name, city;
  private int age;

  public void getData(String x, String y, int t) {
    name = x;
    city = y;
    age = t;
  }

  public void printData() {
    System.out.println("Student name = " + name);
    System.out.println("Student city = " + city);
    System.out.println("Student age = " + age);
  }
}
