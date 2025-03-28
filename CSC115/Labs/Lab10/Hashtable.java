public class Hashtable{
    
private static final int TABLE_SZ = 7; // a prime number

	Student[] table;
	int count;  // number of Students in the table

	public Hashtable() {
		table = new Student[TABLE_SZ];
		count = 0;
	}



	/* MethodName: insertCollisions
	 * Purpose: insert (or update entry) s in this Hashtable with no collision handling strategy
	 * Parameters: Student - s
	 * Throws:  TableFullException - if inserting a new key into a full table
	 *          CollisionException - if inserting a new key into table at index that is full
	 * Returns: nothing
	 */
	public void insertCollisions(Student s) throws TableFullException, CollisionException {
		try{
			int position = findAndGetIndex(s.getSID()); 
			table[position] = s;
		}catch (KeyNotFoundException e){
			int hashcode = s.hashCode();
			int index = hashcode % TABLE_SZ;
			
			if(count == table.length){
				throw new TableFullException();
			}
			
			if(table[index] != null){ 
				throw new CollisionException();
			}
			table[index] = s;
			count++;
		}
	}

	/* MethodName: getCollisions
	 * Purpose: find Student with sid in this Hashtable with no collision handling and returns their grade
	 * Parameters: String - sid
	 * Throws:  KeyNotFoundException  - if Student with sid is not found in table
	 * Returns: int - the grade of Student with sid
	 */
	public int getCollisions(String sid) throws KeyNotFoundException{ 
		int index = findAndGetIndex(sid);
		int grade = table[index].getGrade();
		return grade;
	}

	/* MethodName: findAndGetIndex
	 * Purpose: finds the index of a Student with sid in this Hashtable with no collision handling 
	 * and returns it
	 * Parameters: String - sid
	 * Throws:  KeyNotFoundException  - if Student with sid is not found in table
	 * Returns: int - the index of Student with sid
	 */
	private int findAndGetIndex(String sid) throws KeyNotFoundException{
		int hashcode = sid.hashCode();
		int index = hashcode % TABLE_SZ;
		if(table[index]!= null && table[index].getSID().equals(sid)){
			return index;
		}else{
			throw new KeyNotFoundException();
		}
	}

	/* MethodName: findAndGetIndex
	 * Purpose: finds the index of a Student with sid in this Hashtable with collision handling and returns it
	 * Parameters:  int - cur (the current index)
	 * 				String - sid
	 * 				int - startIndex (the starting index)
	 * Throws:  KeyNotFoundException  - if Student with sid is not found in table
	 * Returns: int - the index of Student with sid
	 */
	private int findAndGetIndex(int cur, String sid, int startIndex) throws KeyNotFoundException{
		if(cur == startIndex){
			throw new KeyNotFoundException();
		}
		if(cur==table.length){
			cur = 0;
		}
		if(table[cur]!= null && table[cur].getSID().equals(sid)){
			return cur;
		}
		return findAndGetIndex(cur+1, sid, startIndex);
	}

	/* MethodName: insertLinearProbing
	 * Purpose: insert (or update entry) s in this Hashtable with Linear Probing to handle collisions
	 * Parameters: Student - s
	 * Throws: TableFullException  - if inserting a new key into a full table
	 * Returns: nothing
	 */
	public void insertLinearProbing(Student s) throws TableFullException{
		try{
			int position = findAndGetIndex(s.getSID()); //update if already there
			table[position] = s;
			return;
		}catch (KeyNotFoundException e){
			int hashcode = s.hashCode();
			int index = hashcode % TABLE_SZ;

			if(table[index] != null){ //if index is full find next open
				int openIndex = getOpenIndex(index+1, s, index); 
				if(openIndex == -1){
					throw new TableFullException(); //if there is no space in the table
				}
				index = openIndex; 
			}
			table[index] = s; 
			count++;
		}
	}
	
	/* MethodName: getOpenIndex
	 * Purpose: finds the first open index after a given index
	 * Parameters:  int - index (the current index)
	 * 				Student - s
	 * 				int - startIndex (the starting index)
	 * Returns: int - the first open index in the table, returns -1 if no open index
	 */
	private int getOpenIndex(int index, Student s, int startIndex){
		if(index == startIndex){
			return -1;
		}
		if(index == table.length){
			index = 0;
		}
		if(table[index] == null){
			return index;
		}
		return getOpenIndex(index+1, s, startIndex);
	}

	/* MethodName: getLinearProbing
	 * Purpose: find Student with sid in this Hashtable that uses Linear Probing and returns their grade
	 * Parameters: String - sid
	 * Throws:  KeyNotFoundException  - if Student with sid is not found in table
	 * Returns: int - the grade of Student with sid
	 */
	public int getLinearProbing(String sid) throws KeyNotFoundException{
		int hashcode = sid.hashCode();
		int index = hashcode % TABLE_SZ;

		if(table[index] == null){
			throw new KeyNotFoundException();
		}

		if(!table[index].getSID().equals(sid)){
			index = findAndGetIndex(index+1, sid, index);
		}
		return table[index].getGrade();
	}

	/*
	 * Purpose: returns the number of elements in this Hashtable
	 * Parameters: none
	 * Returns: int - the number of elements
	 */
	public int size() {
		return count;
	}

	/*
	 * Purpose: returns a String reprensentation of elements
	 *      in this Hashtable separated by newlines
	 * Parameters: none
	 * Returns: String - the representation
	 */
	public String toString() {
		String s = "";

		for(int i=0; i<TABLE_SZ; i++) {
			if (table[i] != null) {
				s  += table[i] + "\n";
			}
		}
		
		return s;
	}
    

}
