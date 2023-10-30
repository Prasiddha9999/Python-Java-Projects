import java.util.*;
import java.io.File;
import java.io.IOException;
import java.io.FileWriter;
import java.util.Collections;
public class AllTestImp
{
public static void main(String[] args) {
    List num = new ArrayList(Arrays.asList(23, 16, 14, 33, 19, 6, 1));
    int iter = 0;
    List emp = new ArrayList();
    while (num.size()>iter){
    if ((int)num.get(iter) % 2 != 0){
        emp.add(num.get(iter));
    }
        iter = iter + 1;
    }
    System.out.println("Ques 1 " + emp);
    int ind = 0;
    while (num.size() > ind){
    if ((int)num.get(ind) == 19){
    System.out.println("The index is: " + ind);
    }
    ind = ind + 1;
    }
    System.out.println("\n" + "2.)");
    List num1 = new ArrayList(Arrays.asList(1,2,3,"four"));
    System.out.println(num1);
    List<Integer> nums = new ArrayList(Arrays.asList(12, 56, 72, 33, 1, 7));
    System.out.println("List is " + nums);
    int sum = 0;
    for (int numbers : nums){
        sum = sum + numbers;
    }
    System.out.println("The sum is " + sum);
    try{
        File nf = new File("datafile2.txt");
        nf.createNewFile();
        FileWriter outputFile = new FileWriter(nf);
        outputFile.write("This is just a test");
        
    if (nf.exists()){
        System.out.println("Exists");
    }
    }
    catch(IOException e){
        System.out.println("An error has occure");
    }
    List fruits = new ArrayList(Arrays.asList("apple", "banana", "pear", "cherry"));
    fruits.remove(0);
    fruits.add(0, "Grapefruit");
    System.out.println(fruits);
    fruits.remove(2);
    fruits.add(2, "Date");
    fruits.add("Orange");
    System.out.println(fruits);
    System.out.println("\n3.)\n");
    List lst = new ArrayList(Arrays.asList(4, 21, 17,7, 9, 1, 13, 45));
    List splicLst = new ArrayList(lst.subList(4, 8));
    System.out.println("The max in the aforementioned second half of the collection is " + Collections.max(splicLst));
    List numsx = new ArrayList(Arrays.asList(12, 56, 72, 33, 1, 7));
    System.out.println("List is "+numsx);
    int itt = 0;
    int add = 0;
    while (numsx.size()>itt){
    add = add + (int)numsx.get(itt);
    itt = itt + 1;
    }
    System.out.println("The total is " +add);
    System.out.println("using a for loop");
    int adder = 0;
    for (int i = 0; i < numsx.size(); i++){
    adder = adder + (int)numsx.get(i);
    }
    System.out.println("The total is " +adder);
    System.out.println("Using a for range");
    List adddd = new ArrayList();
    for (int i = 0; i < numsx.size(); i++){
        adddd.add(numsx.get(i));
    }
    System.out.println(adddd);
    List evOth = new ArrayList();
    for (int i = 0; i < numsx.size(); i++){
    if (i % 2 == 0){
    evOth.add(numsx.get(i));
    }
    System.out.println(evOth);
    }
    }   
}
