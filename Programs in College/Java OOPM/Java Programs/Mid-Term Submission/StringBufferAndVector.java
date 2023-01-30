import java.util.*;

public class StringBufferAndVector {

  public static void main(String[] args) {
    Vector<Integer> vector = new Vector<>();
    vector.add(12);
    vector.add(13);
    vector.add(14);
    System.out.println("The given vector to be displayed is: " + vector);
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter String: ");
    String str = sc.nextLine();
    int len = str.length();
    StringBuffer sb = new StringBuffer();
    for (int i = 0; i < len; i++) {
      String c = Character.toString(str.charAt(i));
      if (
        str.charAt(i) == 'a' ||
        str.charAt(i) == 'e' ||
        str.charAt(i) == 'i' ||
        str.charAt(i) == 'o' ||
        str.charAt(i) == 'u' ||
        str.charAt(i) == 'A' ||
        str.charAt(i) == 'E' ||
        str.charAt(i) == 'I' ||
        str.charAt(i) == 'O' ||
        str.charAt(i) == 'U'
      ) {
        continue;
      }
      sb.append(c.toLowerCase());
      sb.append(',');
    }
    System.out.println("Removing vowels we get: " + sb.toString());
  }
}
