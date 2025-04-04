public class QueueRefBased<T> implements Queue<T> {

    private QueueNode<T> front;
    private QueueNode<T> back;

    public QueueRefBased() {
        front = null;
        back = null;
    }

    public int size() {
        int count = 0;
        QueueNode<T> tmp = front;

        while (tmp != null) {
            count++;
            tmp = tmp.next;
        }
        return count;
    }


    public boolean isEmpty() {
        return front == null;
    }


    public void enqueue (T element) {
        QueueNode<T> nn = new QueueNode<T>(element);
        if (front == null) {
            front = nn;
            back = nn;
        } else {
            back.next = nn;
            back = nn;
        }
    }

    public T dequeue() throws StackEmptyException{
        if(front == null){
            throw new StackEmptyException("thrown in dequeue()");
        }
        
        T val = front.getValue();
        front = front.next;
        if (front == null)
            back = null;

        return val;
    }

    public T peek() throws StackEmptyException{
        if(front == null){
            throw new StackEmptyException("thrown in peek()");
        }

        T val = front.getValue();
        return val;
    }

    public void makeEmpty() {
        front = null;
        back = null;
    }
}
