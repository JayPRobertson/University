/* PairSum225.java
   CSC 225 - SPRING 2024

   This template includes some testing code to help verify the implementation.
   To interactively provide test inputs, run the program with
	java PairSum input_file
*/

import java.util.Scanner;
import java.util.Vector;
import java.util.Arrays;
import java.io.File;

public class PairSum{
	/* PairSum225()
		The input array A will contain non-negative integers. The function
		will search the input array A for two elements which sum to 225.
		If such a pair is found, return true. Otherwise, return false.
		The function may modify the array A.

	*/
	/*
	public static boolean pairSum225(int[] A){
		for (int i=0; i<A.length(); i++){
			for (int j=0; j<A.length(); j++){
				if(A[i] + A[j] == 225){
					return true;
			}
		}
		return false; 
	}
	*/
	
	
	public static boolean pairSum225(int[] A){
		HeapSort(A);
		System.out.println();
		int i = 0;
		int k = (A.length)-1;
		
		while (i != k){
			//System.out.println(i);
			int summation = A[i] + A[k];
			if (summation == 225){
				return true;
			}
			if(summation < 225){
				i++;
			}else{
				k++;
			}
		}
		return false;
	}
	
	public static void HeapSort(int[] A){
		int n = A.length;
		for (int i = (n/2)-1; i >= 0; i--) {
			Heapify(A, n, i);
		}
  
		for (int i = (n-1); i >= 0; i--) {
			int temp = A[0];
			A[0] = A[i];
			A[i] = temp;
			Heapify(A, i, 0);
		}
	}
	
	
	public static void Heapify(int A[], int n, int i) {
		int largest = i;
		int l = 2 * i + 1;
		int r = 2 * i + 2;
  
		if (l < n && A[l] > A[largest])
			largest = l;
  
		if (r < n && A[r] > A[largest])
			largest = r;
  
		if (largest != i) {
			int swap = A[i];
			A[i] = A[largest];
			A[largest] = swap;
  
			Heapify(A, n, largest);
		}
	}
	*/
	

	/* main()
	   Contains code to test the PairSum225 function.
	*/
	public static void main(String[] args){
		Scanner s;
		if (args.length > 0){
			try{
				s = new Scanner(new File(args[0]));
			} catch(java.io.FileNotFoundException e){
				System.out.printf("Unable to open %s\n",args[0]);
				return;
			}
			System.out.printf("Reading input values from %s.\n",args[0]);
		}else{
			s = new Scanner(System.in);
			System.out.printf("Enter a list of non-negative integers. Enter a negative value to end the list.\n");
		}
		Vector<Integer> inputVector = new Vector<Integer>();

		int v;
		while(s.hasNextInt() && (v = s.nextInt()) >= 0)
			inputVector.add(v);

		int[] array = new int[inputVector.size()];

		for (int i = 0; i < array.length; i++)
			array[i] = inputVector.get(i);

		System.out.printf("Read %d values.\n",array.length);


		long startTime = System.currentTimeMillis();

		boolean pairExists = pairSum225(array);

		long endTime = System.currentTimeMillis();

		double totalTimeSeconds = (endTime-startTime)/1000.0;

		System.out.printf("Array %s a pair of values which add to 225.\n",pairExists? "contains":"does not contain");
		System.out.printf("Total Time (seconds): %.4f\n",totalTimeSeconds);
	}
}
