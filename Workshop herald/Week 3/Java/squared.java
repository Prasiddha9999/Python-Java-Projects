import java.util.*;
public class root
{
public static int sroot(int s)
{
    int sr = s*s;
    return(sr);
}
public static void main(String[] arg)
{
    Scanner number= new Scanner(System.in);
    System.out.print("Enter a number : ");
    int a = number.nextInt();
    System.out.print("The square root is " + sroot(a) );
}
}