import java.util.List;

public class SubarrayTester {
    public static void main(String[] args) {
        // Test cases
        int[][] A = {
            {1, 2, 3, 4, 5},
            {5, 6, 7, 8, 9},
            {1, 2, 3, 2, 3, 4}
        };

        int[][] B = {
            {2, 3},
            {2, 3},
            {2, 3}
        };

        boolean[] expectedResults = {true, false, true};
        int[][] expectedIndices = {
            {1},
            {},
            {1, 3}
        };

        // Test the method for each test case
        for (int i = 0; i < A.length; i++) {
            Object[] result = SubarrayChecker.isSubarray(A[i], B[i]);
            boolean expectedResult = expectedResults[i];
            int[] expectedIndex = expectedIndices[i];
            
            boolean resultMatch = (boolean) result[0] == expectedResult;
            boolean indicesMatch = true;
            if (resultMatch && expectedResult) {
                List<Integer> indices = (List<Integer>) result[1];
                if (indices.size() != expectedIndex.length) {
                    indicesMatch = false;
                } else {
                    for (int j = 0; j < indices.size(); j++) {
                        if (!indices.get(j).equals(expectedIndex[j])) {
                            indicesMatch = false;
                            break;
                        }
                    }
                }
            }
            
            if (resultMatch && indicesMatch) {
                System.out.println("Test case " + (i+1) + ": PASSED");
            } else {
                System.out.println("Test case " + (i+1) + ": FAILED");
            }
        }
    }
}
