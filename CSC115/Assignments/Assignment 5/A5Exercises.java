public class A5Exercises {

	/*
	 * Purpose: get the number of occurrences of toFind in theList
	 * Parameters: List<T> theList - the list to search through
	 *             T toFind - the target search value
	 * Returns: int - the number of occurrences of toFind found
	 */
	public static<T> int countMatches(List<T> theList, T toFind) {
		int i = 0;
		return countMatchesRec(theList, toFind, i);
	}

	public static<T> int countMatchesRec(List<T> theList, T toFind, int i) {
		if(i >= theList.size()){
			return 0;
		}else{
			if(theList.get(i).equals(toFind)){
				return 1+countMatchesRec(theList, toFind, i+1);
			}else{
				return countMatchesRec(theList, toFind, i+1);
			}
		}
	}
	
	/*
	 * Purpose: change all occurrences of x to y in the given list
	 * Parameters: List<T> theList - the list to search through
	 *			   T x - the value to change
	 *			   T y = the value to change all x's to
	 * Returns: void - nothing
	 */
	public static<T> void changeXToY(List<T> theList, T x, T y) {
		int i = 0;
		changeXToYRec(theList, x, y, i);
	}

	public static<T> void changeXToYRec(List<T> theList, T x, T y, int i) {
		if(i < theList.size()){
			if(theList.get(i).equals(x)){
				theList.change(i, y);
			}
			changeXToYRec(theList, x, y, i+1);
		}
	}
		
	/* 
	 * Purpose: determines if all values in the list are equivalent
	 * Parameters: List<T> theList - the list
	 * Returns: boolean - true unless any values in the list are 
	 *                    different from one another
	 */
	public static<T> boolean allEqual(List<T> theList) {
		if (theList.isEmpty()) {
			return true;
		} else {
			int i = 0;
			return allEqualRec(theList, i);
		}
	}
	
	public static<T> boolean allEqualRec(List<T> theList, int i){
		if(i+1 >= theList.size()){
			return true;
		}else{
			if(!theList.get(i).equals(theList.get(i+1))){
				return false;
			}else{
				return allEqualRec(theList, i+1);
			}
		}
	}	
	
	/*
	 * Purpose: get the range of values in the given list
	 * Parameters: List<Integer> theList - the list of Integers
	 * Returns: int - the range of values
	 */
	public static int rangeOfValues(List<Integer> theList) {
		if (theList.size() == 0) {
			return 0;
		} else {
			return rangeOfValuesRec(theList, 1, theList.get(0), theList.get(0));
		}
	}
	
	/*
	 * Complete the design of the recursive helper below
	 */
	
	/*
	 * Purpose: get the range of values in the given list from index i onward
	 * Parameters: List<Integer> theList - the list of Integers
	 *             int i - the current index
	 *             Integer min - the smallest value found so far
	 *             Integer max - the largest value found so far
	 * Returns: int - the range of values
	 */
	public static int rangeOfValuesRec(List<Integer> theList, int i, Integer min, Integer max) {
		if(i >= theList.size()){
			return (max-min + 1);
		}else{
			if(theList.get(i) > max){
				max = theList.get(i);
			}else if(theList.get(i)< min){
				min = theList.get(i);
			}
			return rangeOfValuesRec(theList, i+1, min, max);
		
		}
	}
}