import java.util.*;
import java.lang.*;
public class table
{
    public static void multiplicationTable(int a, boolean b){   
    if (b==true){
    for (int h=1; h<11; h++){
        System.out.printf("\t%02d", h);
    }
    for (int j=1; j<=a; j++){
        System.out.printf("\n%02d", j);   
        for (int i=1; i<11; i++){   
        System.out.printf("\t%02d",i*j);
        } 
    }
    }else
    {
    Scanner n = new Scanner(System.in);
    System.out.print("Highest power you want to go : ");
    int num = n.nextInt();
        for (int h=1; h<=num; h++){
        System.out.printf("\t%02d", h);
    }
    for (int j=1; j<=a; j++){
        System.out.printf("\n%02d", j);  
        for (int i=1; i<=num; i++){
        int power = (int)Math.pow(j,i );
        System.out.printf("\t%02d",power);
        } 
    }
    }
}
public static void main(String[] arg){
    Scanner n = new Scanner(System.in);
    boolean b = false;
    System.out.println("\nDo you want a Multiplication table or Power Table");
    System.out.print("Enter True for Multiplication Table and False for Power Table (True/False) : ");
    boolean bn = n.nextBoolean();
    System.out.print("Enter the length of table : ");
    int num= n.nextInt();
    multiplicationTable(num,bn);
}
}