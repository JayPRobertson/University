public class A2Exercises {

	/*
	 * Purpose: get the number of followers of the more popular influencer
	 * Parameters: Influencer person1, Influencer person2
	 * Returns: the number of followers of the more popular influencer
	 */
	public static int highestFollowers (Influencer person1, Influencer person2) {
		int followers = person1.getFollowers();
		if (person1.getFollowers() < person2.getFollowers()){
			followers = person2.getFollowers();
		}
		return followers;
	}
	
	/*
	 * Purpose: get the Influencer with the most followers
	 * Parameters: Influencer[] array - the array of aliases
	 * Returns: Influencer - the alias with the most followers
	 *
	 * Note: if two aliases have the same number of followers, 
	 *       the one who comes first in the array is returned
	 *       (ie. the element with lowest index number)
	 *
	 * Preconditions: The array is not empty
	 */
	public static Influencer mostFollowers (Influencer[] array) {
		Influencer most = array[0];
		for (int i=1; i< array.length; i++){
			if (most.getFollowers() < array[i].getFollowers()){
				most = array[i];
			}
		}		
		return most;
	}
	
	/*
	 * Purpose: get a count of the number of podcasts in the
	 *          array with a shorter duration than the one given
	 * Parameters: Podcast[] array, int duration
	 * Returns: int - the number of podcasts in the array 
	 *                with a shorter duration than the
	 *                duration given
	 */
	public static int numberShorterThan(Podcast[] array, int duration) {
		int count = 0;
		for (int i=0; i< array.length; i++){
			if (array[i].isShorterThan(duration)){
				count ++;
			}
		}
		return count;
	}

	/*
	 * Purpose: get a count of the number of podcasts in
	 *          which toFind is one of the hosts
	 * Parameters: Podcast[] array, Influencer toFind
	 * Returns: int - the number of podcasts in the array 
	 *                that have toFind as a host
	 */	
	public static int numberWithInfluencer(Podcast[] array, Influencer toFind) {
		int count = 0;
		for (int i=0; i< array.length; i++){
			if (array[i].hasHost(toFind)){
				count ++;
			}
		}
		return count;
	}
	
	/*
	 * Purpose: get the podcast found in the given array hosted
	 *          by influencers who have the highest average followers
	 * Parameters: Podcast[] array - the array of podcasts
	 * Returns: Podcast - the podcast with hosts who have the highest
	 *                    average number of followers
	 *
	 * Note: if two podcast's hosts have the same average followers
	 *       the podcast that comes first in the array is 
	 *       is returned (ie. with the lowest index number)
	 *
	 * Preconditions: The array is not empty
	 */
	public static Podcast highestAverageFollowers(Podcast[] array) {
		Podcast highest = array[0];

		for (int i=1; i< array.length; i++){
			if (array[i].averageFollowers() > highest.averageFollowers()){
				highest = array[i];
			}
		}
		return highest;
	}
	
}