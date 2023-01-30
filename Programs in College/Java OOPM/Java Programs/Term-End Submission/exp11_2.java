//program on final keyword
import java.util.*;
import java.lang.*;
import java.io.*;
class exp11_2 {
 final int val;
 exp11_2() {
 val = 60;
 }
 void method() {
 System.out.println(val);
 }
 public static void main(String args[]) {
 exp11_2 S1 = new exp11_2();
 S1.method();
 }
}