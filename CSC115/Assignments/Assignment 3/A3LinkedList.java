// Name: Jay Robertson
// Student number: v0105218

public class A3LinkedList implements A3List {
	private A3Node head;
	private A3Node tail;
	private int length;
	
	public A3LinkedList() {
		head = null;
		tail = null;
		length = 0;
	}

	public int size() {
		return length;
	}

	public A3Node getHead(){
		return head;
	}
	
	public boolean isEmpty() {
		return length==0;
	}
	
	public void addFront(String s) {
		A3Node n = new A3Node(s);
		if (head == null){
			tail = n;
		}else{
			n.next = head;
			head.prev = n;
		}
		head = n;
		length ++;
	}

	public void addBack(String s) {
		A3Node n = new A3Node(s);
		if (tail ==null){
			head = n;
		}else{
			tail.next = n;
			n.prev = tail;
		}
		tail = n;
		length++;
	}
	
	public void removeFront() {
		if (head != null){
			if (head.next == null){
				head = null;
				tail = null;
			}else{
				head = head.next;
				head.prev = null;
			}
			length--;
		}
	}
	
	public void removeBack() {
		if (tail!=null){
			if (head.next == null){
				head = null;
				tail = null;
			}else{
				tail = tail.prev;
				tail.next = null;
			}
			length--;
		}
	}
	
	public void removeAt(int pos) {
		A3Node cur = head;

		if (pos == 0){
			removeFront();
		}else if(pos==length-1){
			removeBack();
		}else if(head != null && pos<(length-1)){
			for (int i=0; i<pos-1; i++){
				cur = cur.next;
			}
			cur.next = cur.next.next;
			cur.next.prev = cur;
			length --;
		}	
	}

	public A3LinkedList mergeSorted(A3LinkedList other) {
		A3LinkedList merged = new A3LinkedList();
		
		A3Node thisCur = head; 
		A3Node otherCur = other.getHead();

		if (thisCur == null){
			merged = other;
		}else if (otherCur == null){
			merged = this;
		}else{
			while(thisCur!=null || otherCur!=null){
				if (otherCur == null || thisCur.comesBefore(otherCur)){
					merged.addBack(thisCur.getData()); 
					thisCur = thisCur.next;
				}else{
					merged.addBack(otherCur.getData());
					otherCur = otherCur.getNext();
				}
			}
		}
		return merged;
	}
	
	/*
	 * Purpose: return a string representation of the list 
	 *          when traversed from front to back
	 * Parameters: none
	 * Returns: nothing
	 *
	 * USED TO HELP YOU WITH DEBUGGING
	 * DO NOT CHANGE THIS METHOD
	 */
	public String frontToBack() {
		String result = "{";
		A3Node cur = head;
		while (cur != null) {
			result += cur.getData();
			cur = cur.next;
		}
		result += "}";
		return result;
	}
	
	/*
	 * Purpose: return a string representation of the list 
	 *          when traversed from back to front
	 * Parameters: none
	 * Returns: nothing
	 *
	 * USED TO HELP YOU WITH DEBUGGING
	 * DO NOT CHANGE THIS METHOD
	 */
	public String backToFront() {
		String result = "{";
		A3Node cur = tail;
		while (cur != null) {
			result += cur.getData();
			cur = cur.prev;
		}
		result += "}";
		return result;
	}
}
	