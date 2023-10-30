import java.util.*;
public class Name{
public static void  program( String name ){
    System.out.println("Hello World. My name is "+ name);
}
public static void main(String[] arg){
    Scanner input = new Scanner(System.in);
    System.out.print("Enter your name :" );
    String name  = input.next();
    program(name);
}
}