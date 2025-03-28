public class StudentLinkedList implements StudentList {

	StudentNode head;
	int count;

	public StudentLinkedList() {
		head = null;
		count = 0;
	}

	public void add(Student s) {
		StudentNode n = new StudentNode(s);
		StudentNode cur = head;
		
		if (head == null){
			head = n;
		}else{
			for (int i=0; i<count-1; i++){
				cur = cur.next;
			}
			cur.next = n;
		}
		count ++;
	}

	public int size() {
		return count;
	}

	public void removeFront() {
		if (head!= null){
			if (head.next == null){
				head = null;
			}else{
				head = head.next;
			}
			count--;
		}
	}

	public boolean contains(Student s) {
		boolean inList = false;
		StudentNode cur = head;
		StudentNode n = new StudentNode(s);
		
		for (int i=0; i<count; i++){
			if (cur.getData().equals(n.getData())){
				inList = true;
				break;
			}
			cur = cur.next;
		}

		return inList;
	}
	
	/*
	 * Purpose: returns a String reprensentation of elements
	 *      in this list separated by newlines
	 * Parameters: none
	 * Returns: String - the representation
	 */
	public String toString() {
		// DO NOT CHANGE THIS METHOD - it is correct
		// Changing it will result in your code getting
		// a score of 0 from the autograder for this lab
		
		String s = "";
		StudentNode tmp = head;

		while(tmp != null) {
			s  += tmp.getData() + "\n";
			tmp = tmp.next;
		}

		return s;
	}
}
