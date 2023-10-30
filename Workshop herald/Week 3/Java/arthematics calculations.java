import java.util.*;
public class maths
{
public static float addition(float a, float b){
    float sum = a+b;
    return (sum);
}
public static float subtraction(float a, float b){
    float sub = a-b;
    return(sub);
}
public static float multiplication(float a, float b){
    float mult = a*b;
    return(mult);
}
public static float division(float a, float b){
    float div = a/b;
    return(div);
}
public static float truncated_division(float a, float b){
    float tdiv = a%b;
    return(tdiv);
}
public static float modulus(float a, float b){
    float mod = a%=b;
    return(mod);
}
public static void main(String[] arg){
    Scanner number = new Scanner(System.in);
    System.out.print("Enter a number");
    int num1= number.nextInt();
    System.out.print("Enter another number");
    int num2= number.nextInt();
    System.out.println("The sum is " + addition(num1,num2));
    System.out.println("The difference is " + subtraction(num1,num2));
    System.out.println("The product is " + multiplication(num1,num2));
    System.out.println("The division is " + division(num1,num2));
    System.out.println("The Truncated Division is " + truncated_division(num1, num2));
    System.out.println("The Modulus is " + modulus(num1,num2));
    
}
}
