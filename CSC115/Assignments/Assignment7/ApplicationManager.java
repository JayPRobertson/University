/*
 * Represents a system to handle incoming job applications for a position at the company
 */
public class ApplicationManager {

	private PriorityQueue<JobApplication> applications;

	/* 
 	 * Constructor that initializes applications to a default-sized priority queue
	 */
	public ApplicationManager() {
		applications = new HeapPriorityQueue<JobApplication>(JobApplication.class);
	}

	/* 
	 * Constructor that initializes applications to a priority queue of given size
	 */
	public ApplicationManager(int size) {
		applications = new HeapPriorityQueue<JobApplication>(JobApplication.class, size);
	}


	/* Purpose: add given job application to applications or prints
	 *          a notification message if no more applications are 
	 *          being accepted for the job (ie. applications is full)
	 * Parameters: JobApplication a - the newest application for the job
	 * Returns: void - nothing
	 */
	public void addApplication(JobApplication a) {
		try{
			applications.insert(a);
		}catch (HeapFullException e){
			System.out.println("Sorry, no more applications are being accepted for this job.");
		}
	}


	/* Purpose: gets the number of applicants who have applied for the job
	 * Parameters: none
	 * Returns: int - number of current applicaitons for the job
	 */
	public int numApplicantsWaiting() {
		return applications.size();
	}


	/* Purpose: removes and returns the next application
	 * Parameters: none
	 * Returns: JobApplication - the next application, 
	 *    or null if there are no more applications left
	 */
	public JobApplication nextApplication() {
		try{
			JobApplication a = applications.removeMin();
			return a;
		}catch (HeapEmptyException e){
			return null;
		}
	}
}

