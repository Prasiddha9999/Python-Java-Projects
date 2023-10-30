import java.util.Set;
import java.util.Iterator;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Collections;
public class test
{
    public static Set addVegetable(Set veg, String newVeg){
        veg.add(newVeg);
        return veg;
    }
    public static void main(String[] args){
        Scanner ve = new Scanner(System.in);
        System.out.println("Enter a vegetable: ");
        String veggy = ve.nextLine();
        Set vegg = new HashSet();
        Collections.addAll(vegg,"carrot", "cabbage", "cauliflower", "radish");
        Set outVeg = addVegetable(vegg, veggy);
        if (vegg.contains(veggy)){
            System.out.println("Error: Vegetable Contained!");
        }else{
            System.out.println("The new set is: " +outVeg);
        }
    }
}
