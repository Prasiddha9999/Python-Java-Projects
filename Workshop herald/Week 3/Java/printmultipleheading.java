import java.util.*;
public class Cat
{
    public static void printMultilineHeading(String name, int age)
    {
        System.out.print("\n Dear Feline Fanatic,\n Your cat has been arrested for \n 1. Catnapping \n 2. Cat burglary \n 3. Extortion. \nIt will be sentenced to " +age + " years in prison. \n Sincerely," +name);
    }
    public static void main(String[] arg)
    {
        Scanner data = new Scanner(System.in);
        System.out.print("Enter name : ");
        String name= data.next();
        System.out.print("Enter cat's age : ");
        int age= data.nextInt();
        printMultilineHeading(name,age);
    }
}