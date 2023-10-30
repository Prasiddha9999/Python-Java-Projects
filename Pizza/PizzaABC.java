//Pizza A

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



//PizzaB

import java.util.*;


public class Pizza{
	
	static boolean checkNum(String s) {
		if (s.isEmpty())
		{
			return false;
		}
		
		try {
			int temp = Integer.parseInt(s);
		}
		catch(Exception e)
		{
			return false;
		}
		return true;
		
	}
    
    public static void main(String[] args) {
    	String snum_ppl;
    	String snum_pizza;
    	String snum_slices;
    	
    	Scanner sc = new Scanner(System.in);
    	System.out.println("Enter the number of people:");
    	do {
    		snum_ppl = sc.next();
    		if(!checkNum(snum_ppl))
    		{
    			System.out.println("Number of people should be a number. Enter Again!");
    		}
    	}while(!checkNum(snum_ppl));
    	int num_ppl = Integer.parseInt(snum_ppl);
    	
    	
    	
    	System.out.println("Enter the number of pizzas:");
    	do {
    		snum_pizza = sc.next();
    		if(!checkNum(snum_pizza))
    		{
    			System.out.println("Number of pizza should be a number. Enter Again!");
    		}
    	}while(!checkNum(snum_pizza));
    	int num_pizza= Integer.parseInt(snum_pizza);
    	
    	
    	System.out.println("Enter the number of slices per pizza:");
    	do {
    		snum_slices= sc.next();
    		if(!checkNum(snum_slices))
    		{
    			System.out.println("Number of slices should be a number. Enter Again!");
    		}
    	}while(!checkNum(snum_slices));
    	int num_slices = Integer.parseInt(snum_slices);
    	
    	
    	
    	
    	int total_slices = num_pizza * num_slices;
    	
    	int leftovers = total_slices % num_ppl;
    	int each = total_slices/num_ppl;
    	
    	System.out.println("Each person gets "+each+" slices.");
    	System.out.println("There are "+leftovers+" leftover slices.");
    	
    }
}

//PizzaC

import java.util.*;


public class Pizza {
	
	static boolean checkNum(String s) {
		if (s.isEmpty())
		{
			return false;
		}
		
		try {
			int temp = Integer.parseInt(s);
		}
		catch(Exception e)
		{
			return false;
		}
		return true;
		
	}
    
    public static void main(String[] args) {
    	String snum_ppl;
    	String snum_pizza;
    	String snum_slices;
    	
    	Scanner sc = new Scanner(System.in);
    	System.out.println("Enter the number of people:");
    	do {
    		snum_ppl = sc.next();
    		if(!checkNum(snum_ppl))
    		{
    			System.out.println("Number of people should be a number. Enter Again!");
    		}
    	}while(!checkNum(snum_ppl));
    	int num_ppl = Integer.parseInt(snum_ppl);
    	
    	
    	
    	System.out.println("Enter the number of pizzas:");
    	do {
    		snum_pizza = sc.next();
    		if(!checkNum(snum_pizza))
    		{
    			System.out.println("Number of pizza should be a number. Enter Again!");
    		}
    	}while(!checkNum(snum_pizza));
    	int num_pizza= Integer.parseInt(snum_pizza);
    	
    	
    	System.out.println("Which size of pizza would you like to choose?:\n1. Small(4 slices)\t2. Medium(8 slices)\t3. Large(12 slices)");
    	int num_slices=0;
    	int choice = sc.nextInt();
    	switch (choice) {
		case 1:
			num_slices=4;
			break;
		case 2:
			num_slices=8;
			break;
		case 3:
			num_slices=12;
			break;
		default:
			System.out.println("Error in choice!");
			break;
		} 	
    	
    	
    	
    	int total_slices = num_pizza * num_slices;
    	
    	int leftovers = total_slices % num_ppl;
    	int each = total_slices/num_ppl;
    	
    	System.out.println("Each person gets "+each+" slices.");
    	System.out.println("There are "+leftovers+" leftover slices.");
    	
    }
}

