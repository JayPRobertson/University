/* 
    CSC 225 - 24SP - Assignment 3
    Last Name: Robertson
    First Name: Jay
    Student Number: V01005218
*/

import java.io.*;
import java.util.*;

public class SubarrayChecker {
    public static Object[] isSubarray(int[] A, int[] B){
        //Assume B.length >0
        List<Integer> indices = new ArrayList<>();
        boolean isSubarray = false;
        int length = A.length - B.length;

        if(B.length == 1){ //general method doesn't work for B of length 1
            for(int i=0; i<=length; i++){
                if(A[i] == B[0]){
                    indices.add(i);
                    isSubarray = true;
                }
            }
            return new Object[]{isSubarray, indices};
        }

        for(int i=0; i<=length; i++){ 
            //iterate through all indicies that could give A[i] = B[0]
            if(B[0] == A[i] && B[1] == A[i+1]){
                try{
                    for(int j=i+2; (j-i)<=B.length; j++){ 
                        //encode intential error at end of loop to trigger alternate condition in catch
                        if(A[j] != B[j-i]){ //checks if cur elem not the same
                            break; 
                        }
                    }
                }catch (ArrayIndexOutOfBoundsException e){ //INTENTIONAL ERROR!
                    indices.add(i);
                    isSubarray = true;
                    i += (B.length-1); //jump to next possible location-1
                }
            }
        }
        
        return new Object[]{isSubarray, indices};
    }

    /*
        Calculates the time and space complexity of your algorithm.
        Time complexity: O(n^2)
        Space complexity: O(n^2)
    */

    public static void main(String[] args) {
       /* 
            Read input from STDIN. Print output to STDOUT.
	
   	        To conveniently test your algorithm, you can run your solution with any of the tester input files using:
            java SubarrayChecker inputX.txt
	        where X is 1, 2, ..., 6.

            The array size is from 5, 10, ..., 5000.
            You should capture the time taken using built in commands.
            Find the result/output for different input sizes and then plot it in a graph.
            Write a small paragraph about what you observed experimentally and what was your 
            analytical/theoretical analysis of time complexity.  
	    */
        long startTimeMillis = System.currentTimeMillis();
        
        try{
            String filename = args[0];
            File txtFile = new File(filename); //open file
            Scanner scanLines = new Scanner(txtFile);

            while (scanLines.hasNextLine()) {
                int[] A = makeIntArray(scanLines.nextLine().split(" "));
                int[] B = makeIntArray(scanLines.nextLine().split(" "));
                
                Object[] results = isSubarray(A, B);
                //System.out.println(results[0]);
                //System.out.println(results[1]);
            }

            scanLines.close(); //close file

        }catch(ArrayIndexOutOfBoundsException e){
            System.out.println("Index out of bounds");
        }catch (FileNotFoundException e) {
            System.out.println("File not found");
        }

        long endTimeMillis = System.currentTimeMillis();
        long elapsedTimeMillis = endTimeMillis - startTimeMillis;
        System.out.println(elapsedTimeMillis);
    }

    public static int[] makeIntArray(String[] strArr){
        //convert all values in a str[] to ints, making a new int[]
        int[] newArr = new int[strArr.length];
        for (int i =0; i<strArr.length; i++){
            newArr[i] = Integer.parseInt(strArr[i]);
        }
        return newArr;
    }
}
