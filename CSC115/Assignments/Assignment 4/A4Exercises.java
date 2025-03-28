public class A4Exercises {

	/*
	 * Purpose: gets the number of buildings in the given list
	 * Parameters: List bList - the list of buildings
	 * Returns: int - the number of buildings in the given list
	 */
	public static int buildingsCount(List bList) {
		return bList.size();
	}
	
	/*
	 * Purpose: gets the total number of inhabitants living 
	 *          in all the buildings in the given list
	 * Parameters: List bList - the list of buildings
	 * Returns: int - the number of inhabitants across all buildings
	 */
	public static int inhabitantsCount(List bList) {
		int result = 0;
		for (int i=0; i<buildingsCount(bList); i++){
			result += bList.get(i).getNumberOfInhabitants();
		}
		return result;
	}
	
	/*
	 * Purpose: get the number of buildings into the list b is
	 * Parameters: List bList - the list of buildings
	 *             Building b - the building to find
	 * Returns: int - the distance the first occurrence of 
	 *                b is from the start of the list, or 
	 *                -1 if b is not found in bList
	 */
	public static int distanceAway(List bList, Building b) {
		int distance = -1;
		int i = 0;

		while (distance == -1 && i<buildingsCount(bList)){
			if (bList.get(i).equals(b)){
				distance = i;
			}
			i++;
		}
		return distance;
	}
	
	/*
	 * Purpose: get the distance the tallest building is 
	 *          from the start of the list
	 * Parameters: List bList - the list of buildings
	 * Returns: int - the distance the tallest building
	 *                is from the start of the list
	 */
	public static int distanceToTallest(List bList) {
		if (bList.size()==0){
			return 0;
		}else{
			Building tallest = bList.get(0);
			for (int i=1; i<bList.size(); i++){
				if (bList.get(i).getNumberOfStories() > tallest.getNumberOfStories()){
					tallest = bList.get(i);
				}
			}
			return distanceAway(bList, tallest);
		}
		
	}

	/*
	 * Purpose: get the number of buildings visible 
	 *          from the beginning of the list 
	 * Parameters: List bList - the list of buildings
	 * Returns: int - the number of buildings visible
	 * 
	 * Note: Read through the assignment PDF for more information
	 */
	public static int numberVisible(List bList) {
		int count = 0;
		int curTallest = 0;

		for(int i=0; i<bList.size(); i++){
			if(bList.get(i).getNumberOfStories() > curTallest){
				count ++;
				curTallest = bList.get(i).getNumberOfStories();
			}
		}
		return count;
	}
		


}