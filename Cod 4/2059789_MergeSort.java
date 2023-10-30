//Name:Prasiddha Regmi
//StudentId:2059789


import java.util.ArrayList;
import java.util.Scanner;

public class MergeSort {
	int n;	//integer type
	ArrayList<Integer> getInput(ArrayList<Integer> al) {
		System.out.println(".........Wellcome to Mergesort Program.........");
		System.out.println();
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter the number of element you want to sort: ");		//get the numbers of element from user
		n = sc.nextInt();
		System.out.println("\nNow, Enter the "+n+" elements to sort ");		//get different number of element to sort
		for (int i = 0; i < n; i++) { 		//looping up to n numbers to add elements
			System.out.print("Enter the index " +i+ " elements : ");
			al.add(sc.nextInt());		//add element which is given by users
		}
		return al; // return all the elements of al
			
	}
	
	void getOutput(ArrayList<Integer> al) {
		if(al.size()==n)// If user complete to input n numbers of element 
		{
		System.out.println("\n....Sorted Array.....");  //print "sorted array"
		for(int i =0; i<al.size();i++)  //looping up to n number of element to print sorted array
		{  
		    System.out.println(al.get(i)+" "); //print the given element by sorting 
		}  
		}
	}
	
	void merge(ArrayList<Integer> al, int beg, int mid, int end) {
		  
		int l = beg;  
		int r = mid+1;  
		ArrayList<Integer> mergedSortedArray = new ArrayList<Integer>();
		  
		 while(l<=mid && r<=end){
	            if(al.get(l)<=al.get(r)){
	                mergedSortedArray.add(al.get(l));
	                l++;
	            }else{
	                mergedSortedArray.add(al.get(r));
	                r++;
	            }
	        }       
		 	// Either of below while loop will execute
	        while(l<=mid){
	            mergedSortedArray.add(al.get(l));
	            l++;
	        }
	        
	        while(r<=end){
	            mergedSortedArray.add(al.get(r));
	            r++;
	        }
	        
	        int i = 0;
	        int j = beg;
	        //Setting sorted array to original one
	        while(i<mergedSortedArray.size()){
	            al.set(j, mergedSortedArray.get(i++));
	            j++;
	        }
	        getOutput(mergedSortedArray);
		
	}
	//function that sorts arr[beg..end] using merge()
	void sort(ArrayList<Integer> al, int beg, int end) {
		//
		if (beg<end)  //condition 
		{  
		int mid = (beg+end)/2;  //Finding the middle point by dividing arraylist
		sort(al, beg, mid);  //Sort first and second halves
		sort(al , mid+1, end);  
		merge(al, beg, mid, end);  //merge the sorted halves
		}  
	}
	
	public static void main(String[] args) {
		ArrayList<Integer> arr = new ArrayList<>();  
		MergeSort ob = new MergeSort();
		arr = ob.getInput(arr);
		if(arr.size()==1)  // if user input the number of element 0 then display without sorted
			ob.getOutput(arr);
		else {
			if(arr.size()==0)
				ob.getOutput(arr);
			else
		ob.sort(arr, 0, arr.size()-1);  	  
	}
}
}
