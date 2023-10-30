import java.util.*;
public class Divisionfloat{
        public static void main(String[] args){
            
            Scanner input = new Scanner(System.in);
            System.out.print("Enter a number :" );
            float number1 = input.nextInt();
            
            System.out.print("Enter another number : ");
            float number2 = input.nextInt();

            float div = number1 / number2;

            System.out.printf("Division of a and b is : %.2f \n", div);
        
            
        }
}