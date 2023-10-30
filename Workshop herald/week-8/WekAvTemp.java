import java.util.Hashtable;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
public class WekAvTemp
{
    public static int getWeekendAverageTemp(Hashtable weekTemp){
        Set days = weekTemp.keySet();
        int sat = (int)weekTemp.get("sat");
        int sun = (int)weekTemp.get("sun");
        int avWeeknd = (sat+sun)/2;
        return avWeeknd;
    }
    public static void main(String[] args){
        Hashtable daysTemp = new Hashtable();
        daysTemp.put("sun", 70);
        daysTemp.put("mon", 80);
        daysTemp.put("tue", 90);
        daysTemp.put("wed", 85);
        daysTemp.put("thu", 75);
        daysTemp.put("fri", 70);
        daysTemp.put("sat", 75);
        int av = getWeekendAverageTemp(daysTemp);
        System.out.println("The average tempreature over the weekend is: "+av);
    }
}
