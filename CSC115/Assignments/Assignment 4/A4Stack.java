public class A4Stack<T> implements Stack<T> {
	
	private A4Node<T> head;
	// Do NOT add any other fields to this class.
	// You should be able to implement the Stack 
	// interface with just a head field.

	public A4Stack() {
		this.head = null;
	}
	
	public void push(T value) {
		if(value == null){
			popAll();
		}else{
			A4Node<T> val = new A4Node<T>(value);
			if(head == null){
				head = val;
			}else{
				val.setNext(head);
				head = val;
			}
		}
	}
	
	public T pop() {
		T top = null;

		if (head != null){
			top = head.getData();
			head = head.next;
		}
		
		return top;
	}
	
	public void popAll() {
		head = null;
	}
	
	public boolean isEmpty() {
		return head == null;
	}
	
	public T peek() {
		if(head == null){
			return null;
		}
		return head.getData();
	}
	
	// Implemented for you for debugging purposes
	public String toString() {
		String result = "{";
		String separator = "";
		
		A4Node<T> cur = head;
		while (cur != null) {
			result += separator + cur.getData().toString();
			separator = ", ";
			cur = cur.next;
		}
	
		result += "}";
		return result;
	}
}