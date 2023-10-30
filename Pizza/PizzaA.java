import java.util.*;


public class Pizza {
    
    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	System.out.println("Enter the number of people:");
    	int num_ppl = sc.nextInt(); 
    	System.out.println("Enter the number of pizzas:");
    	int num_pizza = sc.nextInt();
    	System.out.println("Enter the number of slices per pizza:");
    	int num_slices = sc.nextInt();
    	int total_slices = num_pizza * num_slices;
    	
    	int leftovers = total_slices % num_ppl;
    	int each = total_slices/num_ppl;
    	
    	System.out.println("Each person gets "+each+" slices.");
    	System.out.println("There are "+leftovers+" leftover slices.");
    	
    }
}