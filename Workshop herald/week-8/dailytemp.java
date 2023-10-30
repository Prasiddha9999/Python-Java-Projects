import java.util.*;
public class dailytemp
{
    public static void getDailyTemps(){
        int i = 0;
        Hashtable sunSat = new Hashtable();
        Scanner dayInp = new Scanner(System.in);
        Scanner avTempInp = new Scanner(System.in);
        String day;
        int temp;
        while (i < 7){
            System.out.println("Enter day: ");
            day = dayInp.nextLine();
            System.out.println("Enter the av Temp for the day: ");
            temp = avTempInp.nextInt();
            System.out.println("-------------------------------");
            sunSat.put(day, temp);
            i = i + 1;
        }
        System.out.println("-------------------------------");
        System.out.println("The Hashtable: " +sunSat);
    }
    public static void main (String[] args){
        getDailyTemps();
    }
}
