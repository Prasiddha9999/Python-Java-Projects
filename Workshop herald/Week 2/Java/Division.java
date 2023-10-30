import java.util.*;
public class Division{
        public static void main(String[] args){
            
            Scanner input = new Scanner(System.in);
            System.out.print("Enter a number :" );
            int number1 = input.nextInt();
            
            System.out.print("Enter another number : ");
            int number2 = input.nextInt();

            int div = number1 / number2;

            System.out.printf("Division of a and b is : %.2f \n", div);
        
            
        }
}