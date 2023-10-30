    import java.util.*;
public class ScientificNotation{
        public static void main(String[] args){
            
            Scanner input = new Scanner(System.in);
            System.out.print("Enter a number :" );
            Float number1 = input.nextFloat();
            
            System.out.print("Enter another number : ");
            Float number2 = input.nextFloat();

            Float div = number1 / number2;

            System.out.printf("Division : %6.3e \n", div);
        
            
        }
}