/*
 * Lab2Tester.java
 *
 * A tester for the methods in Lab2.java
 *
 */
import java.util.Arrays;

public class Lab2Tester {
    
	private static int testPassCount = 0;
	private static int testCount = 0;

	// for approximate comparison of floating point numbers
	private static final double THRESHOLD = 0.01;

	public static void main(String[] args) {
		
		testGetHigherGradeStudent();
		testIsGradeAbove();
		testGetClasslist();
		testCountAbove();
		testGetClassAverage();
		testRegisterStudent();

		System.out.println("Passed " + testPassCount + " / " + testCount + " tests");
	}
	
	public static void testGetHigherGradeStudent() {
		Student s0  = new Student("abc", 50);
		Student s1a = new Student("def", 56);
		Student s1b = new Student("xyz", 56);
		Student s2  = new Student("xyz", 99);

		Student result;

		result = Lab2.getHigherGradeStudent(s0,s1a);
		//System.out.println("should be  " + s1a + " is " + result);
		displayResults(result.equals(s1a), "testGetHigherGradeStudent");

		result = Lab2.getHigherGradeStudent(s1a,s0);
		//System.out.println("should be  " + s1a + " is " + result);
		displayResults(result.equals(s1a), "testGetHigherGradeStudent");

		result = Lab2.getHigherGradeStudent(s1b,s1a);
		//System.out.println("should be  " + s1b + " is " + result);
		displayResults(result.equals(s1b) && result == s1b, "testGetHigherGradeStudent");

		result = Lab2.getHigherGradeStudent(s1b,s2);
		//System.out.println("should be  " + s2 + " is " + result);
		displayResults(result.equals(s2), "testGetHigherGradeStudent");
	
	}

	public static void testIsGradeAbove() {
		Student s0  = new Student("abc", 50);
		Student s1a = new Student("def", 56);
		Student s1b = new Student("xyz", 56);
		Student s2  = new Student("xyz", 99);

		boolean result;

		result = Lab2.isGradeAbove(s0,50);
		//System.out.println("should be  " + false + " is " + result);
		displayResults(result == false, "testIsGradeAbove - grade 50");

		result = Lab2.isGradeAbove(s1a,50);
		//System.out.println("should be  " + true + " is " + result);
		displayResults(result == true, "testIsGradeAbove - grade 50");

		result = Lab2.isGradeAbove(s1b,60);
		//System.out.println("should be  " + false + " is " + result);
		displayResults(result == false, "testIsGradeAbove - grade 60");

		result = Lab2.isGradeAbove(s2, 98);
		//System.out.println("should be  " + true + " is " + result);
		displayResults(result == true, "testIsGradeAbove - grade 98");


	}

	public static void testGetClasslist() {
		// NOTE: the Arrays library has been imported for you.
		//       you can use the Arrays.equals method to compare
		//       2 arrays of String objects as String has a equals method
		// The API for Arrays.equals:
		//       equals(Object[] a, Object[] a2)
		//       Returns true if the two specified arrays are equal to one another.

		Student s0  = new Student("abc", 50);
		Student s1a = new Student("def", 56);
		Student s1b = new Student("xyz", 56);
		Student s2  = new Student("xyz", 99);

		Student[] students1 = {s0};
		Student[] students2 = {s0, s1a};
		Student[] students3 = {s0, s1a, s1b};
		Student[] students4 = {s0, s1a, s1b, s2};

		String[] expected1 = {"abc"};
		String[] expected2 ={"abc", "def"};
		String[] expected3 ={"abc", "def", "xyz"};
		String[] expected4 ={"abc", "def", "xyz", "xyz"};

		String[] result;

		result = Lab2.getClasslist(students1);
		displayResults(Arrays.equals(result, expected1), "testGetClasslist - 1 elements");

		result = Lab2.getClasslist(students2);
		displayResults(Arrays.equals(result, expected2), "testGetClasslist - 2 elements");

		result = Lab2.getClasslist(students3);
		displayResults(Arrays.equals(result, expected3), "testGetClasslist - 3 elements");

		result = Lab2.getClasslist(students4);
		displayResults(Arrays.equals(result, expected4), "testGetClasslist - 4 elements");
	}


	public static void testCountAbove() {
		Student s0  = new Student("abc", 50);
		Student s1a = new Student("def", 56);
		Student s1b = new Student("xyz", 56);
		Student s2  = new Student("xyz", 99);

		Student[] students1 = {s0};
		Student[] students2 = {s0, s1a};
		Student[] students3 = {s0, s1a, s1b};
		Student[] students4 = {s0, s1a, s1b, s2};

		int result;

		result = Lab2.countAbove(students1, 49);
		displayResults(result==1, "testCountAbove - 1 elements, threshold 49");

		result = Lab2.countAbove(students2, 40);
		displayResults(result==2, "testCountAbove - 2 elements, threshold 40");

		result = Lab2.countAbove(students3, 56);
		displayResults(result==0, "testCountAbove - 3 elements, threshold 56");

		result = Lab2.countAbove(students4, 57);
		displayResults(result==1, "testCountAbove- 4 elements, threshold 57");

	}

	public static void testGetClassAverage() {
		Student s0 = new Student("abc", 50);
		Student s1 = new Student(); // considered invalid for average average calculation
		Student s2 = new Student("xyz", 99);
		Student s3 = new Student("def", 88);

		Student[] students0 = {};
		Student[] students1 = {s0};
		Student[] students2 = {s0, s1, s2};
		Student[] students3 = {s0, s2, s3};

		double result = 0.0;
		double expected = 0.0;
		
		// Some of you noticed in Lab1 that floating point arithmetic sometimes
		// produces results with many decimals places. We use the threshold
		// (defined as a global variable at the top) to specify the margin 
		// of error we are okay with, and just make sure the expected and 
		// returned results are within the threshold of acceptable error.

		
		result = Lab2.getClassAverage(students0);
		expected = 0;
		displayResults(Math.abs(result-expected)<THRESHOLD, "testGetClassAverage - empty");

		result = Lab2.getClassAverage(students1);
		expected = 50.0;
		displayResults(Math.abs(result-expected)<THRESHOLD, "testGetClassAverage - 1 student");

		result = Lab2.getClassAverage(students2);
		expected = (50 + 99) / 2.0; // because s1 does not have a "real" grade
		displayResults(Math.abs(result-expected)<THRESHOLD, "testGetClassAverage - 3 students, count 2");

		result = Lab2.getClassAverage(students3);
		expected = (50 + 99 + 88) / 3.0;
		displayResults(Math.abs(result-expected)<THRESHOLD, "testGetClassAverage - 3 students, count 3");
        
	}

	public static void testRegisterStudent() {
		Student s0  = new Student("abc", 50);
		Student s1a = new Student("def", 56);
		Student s1b = new Student("xyz", 56);
		Student s2  = new Student("xyz", 99);

		Student[] students1 = {s0};
		Student[] students2 = {s0, s1a};
		Student[] students3 = {s0, s1a, s1b};

		Student[] expected1 = students2;
		Student[] expected2 = {s0, s1a, s0};
		Student[] expected3 = {s0, s1a, s1b, s1b, s2};

		Student[] result;

		result = Lab2.registerStudent(students1, s1a);
		displayResults(Arrays.equals(result, expected1), "testRegisterStudent - 1 elements, 1 added");

		result = Lab2.registerStudent(students2, s0);
		displayResults(Arrays.equals(result, expected2), "testRegisterStudent - 2 elements, same added");

		result = Lab2.registerStudent(students3, s1b);
		result = Lab2.registerStudent(result, s2);
		displayResults(Arrays.equals(result, expected3), "testRegisterStudent - 3 elements, 2 added");
	}
	
	public static void displayResults (boolean passed, String testName) {
		/* There is some magic going on here getting the line number
		 * Borrowed from:
		 * http://blog.taragana.com/index.php/archive/core-java-how-to-get-java-source-code-line-number-file-name-in-code/
		 */
		
		testCount++;
		if (passed) {
			System.out.println ("Passed test: " + testName);
			testPassCount++;
		} else {
			System.out.println ("Failed test: " + testName + " at line "
								+ Thread.currentThread().getStackTrace()[2].getLineNumber());
		}

	}

}
