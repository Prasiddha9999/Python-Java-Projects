import java.util.*;
public class Multiple
{
        public static void main(String[] args){
            
            Scanner input = new Scanner(System.in);
            System.out.print("Enter a number :" );
            Float number1 = input.nextFloat();
            
            System.out.print("Enter another number : ");
            Float number2 = input.nextFloat();
            
            Float sum = number1 + number2;
            Float dif = number1 - number2;
            Float mult= number1 * number2;
            Float div = number1 / number2;
            Float mod = number1 % number2;

            System.out.println("Addition : "+ sum);
            System.out.println("Subtraction : "+ dif);
            System.out.println("Multiplication : "+ mult);
            System.out.format("Division : %.02f \n", div);
            System.out.println("Modulus : "+ mod);
            
            
            
        }
}
