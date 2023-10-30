import java.util.*;
public class Decimal
{
    public static void decimalpoint(float a, float b)
    {
        float value = a/b;
        System.out.format("The value in decimal point is %.2f", value);
        
    }
    public static void main(String[] arg)
    {
        Scanner data = new Scanner(System.in);
        System.out.print("Enter a number : ");
        int x= data.nextInt();
        System.out.print("Enter a number : ");
        int y= data.nextInt();
        decimalpoint(x,y);
    }
}