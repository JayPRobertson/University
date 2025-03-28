/*
 * Lab1Part2Tester.java
 *
 * A tester for the methods in your Student class
 *
 */
public class Lab1Part2Tester {

	public static void main(String[] args) {
		testConstructorsAndGetters();
		testSettersAndGetters();
		testToString();
	}

	public static void testConstructorsAndGetters() {

		// 1)
		// Tests constructor with no arguments, getSID and getGrade
		// TODO: once you have completed the getSID and getGrade methods
		// uncomment the following to test your implementation
	
	
		Student s1 = new Student();
		System.out.println("sID of student with default constructor: " + s1.getSID());
		System.out.println("grade of student with default constructor: " + s1.getGrade());

		Student s2 = new Student("V00923094", 85);
		System.out.println("sID of student with custom constructor: " + s2.getSID());
		System.out.println("grade of student with custom constructor: " + s2.getGrade());
	
		
	}

	

	public static void testSettersAndGetters(){
		// 2) 
		// TODO: implement and then call the setSID and setGrade methods
		// Hint: use getSID and getGrade methods to get the updated values
		
		System.out.println("\nOriginal information for student:");
		Student s2 = new Student("V00923094", 85);
		System.out.println("sID of student: " + s2.getSID());
		System.out.println("grade of student: " + s2.getGrade());
		
		System.out.println("\nUpdated information for student:");
		s2.setGrade(12);
		s2.setSID("V12345678");
		System.out.println("sID of student: " + s2.getSID());
		System.out.println("grade of student: " + s2.getGrade());
		
	}

	public static void testToString() {
		// 3)
		// TODO: once you have written toString in the Student class,
		// create a student object and test the toString method

		Student s3 = new Student("V1011121314", 34);
		System.out.println(s3);

	}
	
}
