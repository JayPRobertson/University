public class QueueRefBased implements Queue {

	private QueueNode front;
	private QueueNode back;
	
	// no numElements for this implementation
	private int count;

	public QueueRefBased() {
		front = null;
		back = null;
		count = 0;
	}

	public int size() {		
		return count;			
	}

	public boolean isEmpty() {
		return front==null;
	}

	public void enqueue (int value) {
		QueueNode val = new QueueNode(value);

		if (isEmpty()){
			front = val;
			back = val;
		}else{
			back.setNext(val);
			back = val;
		}
		count ++;
	}

	public int dequeue() {
		int oldFront = 0;
		
		if (!isEmpty()){
			oldFront = front.getValue();
			front = front.next;
			count --;
		}

		return oldFront;
	}

	public int peek()  {
		return front.getValue();
	}

	public void makeEmpty() {
		front = null;
		back = null;
		count = 0;
	}
}
