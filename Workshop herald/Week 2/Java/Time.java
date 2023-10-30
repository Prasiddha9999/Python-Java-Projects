import java.util.Scanner;
public class Time
{
    public static void main(String[] args)
    {
        
        Scanner in = new Scanner(System.in);
        
        System.out.print("Enter seconds : ");

        int seconds = in.nextInt(); 

        int p1 = seconds % 60;
        int p2 = seconds / 60;
        int p3 = p2 % 60;

        p2 = p2 / 60;

        System.out.print("Hour:Min:Sec - " +p2 + ":" + p3 + ":" + p1);
        System.out.print("\n");
    }  
}
