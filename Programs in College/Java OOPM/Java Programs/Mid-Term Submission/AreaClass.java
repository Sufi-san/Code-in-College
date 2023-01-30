class AreaClass {

  int side1;
  int side2;
  int side3;
  int side4;

  public AreaClass(int a, int b, int c) {
    side1 = a;
    side2 = b;
    side3 = c;
    System.out.println(
      "It is Triangle with sides as \n" +
      a +
      " units," +
      b +
      " units," +
      c +
      " units"
    );
  }

  public AreaClass(int a) {
    side1 = a;
    System.out.println("It is a Square with side as \n" + a + " units");
  }

  public AreaClass(int a, int b) {
    side1 = a;
    side2 = b;
    System.out.println(
      "It is Rectangle with side as \n" + a + " units," + b + " units."
    );
  }

  void getArea(int a) {
    double area = a * a;
    System.out.println("Area of Square is " + area + " sq.units");
  }

  void getArea(double base, double side) {
    double area = 0.5 * base * (side * 1.73) / 2;
    System.out.println("Area of Triangle is " + area + " sq.units");
  }

  void getArea(int a, int b) {
    double area = a * b;
    System.out.println("Area of Rectangle is " + area + " sq.units");
  }
}
