import java.util.ArrayList;
import java.util.List;
import java.io.File;
import java.util.*;
import java.util.Hashtable;
import java.util.Iterator;
public class part
{
    public static Hashtable addDailyTemp (Hashtable dicTemp, String day, int temp){
        Iterator<String> it = dicTemp.keySet().iterator();
        while(it.hasNext()){
         if (dicTemp.containsKey(day)){
                it.next();
                dicTemp = dicTemp;
            } else {
                dicTemp.put(day, temp);
                break;
            }
        }
        return dicTemp;
    }
    public static void moderateDays(Hashtable dicc){
        Set dayz = dicc.keySet();
        List dayList = new ArrayList();
        int itt = 0;
        int tot = 0;
        int avg = 0;
        for (Object k : dayz){
            if ((int)dicc.get(k) > 70 && (int)dicc.get(k) < 79){
                dayList.add(k);
                tot = (tot + (int)dicc.get(k));
                avg = avg + 1;
            }
        }
        System.out.print("Days: ");
        for (int i = 0; i < dayList.size(); i++){
            System.out.print(dayList.get(i) + ", ");
        }
        System.out.print(tot/avg);
    }
    public static void main(String[] args){
        Scanner inpDay = new Scanner(System.in);
        System.out.println("Enter Day: ");
        String day1 = inpDay.nextLine();
        Scanner inpTemp = new Scanner(System.in);
        System.out.println("Enter Temp: ");
        int temp1 = inpTemp.nextInt();
        Hashtable daysAndTemps = new Hashtable();
        daysAndTemps.put("sun", 71);
        daysAndTemps.put("mon", 78);
        daysAndTemps.put("tue", 60);
        daysAndTemps.put("wed", 72);
        daysAndTemps.put("thu", 40);
        System.out.println(daysAndTemps);
        Hashtable out = addDailyTemp(daysAndTemps, day1, temp1);
        System.out.println("The updated Dictionary is: " +out);
        moderateDays(out);
    }
}
