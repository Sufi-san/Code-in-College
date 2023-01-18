public class Area {

  public static void main(String[] args) {
    AreaClass shape1 = new AreaClass(5);
    shape1.getArea(5);
    System.out.println();
    AreaClass shape2 = new AreaClass(5, 6);
    shape2.getArea(5, 6);
    System.out.println();
    AreaClass shape3 = new AreaClass(20, 20, 20);
    shape3.getArea(20, 20);
    System.out.println();
  }
}
