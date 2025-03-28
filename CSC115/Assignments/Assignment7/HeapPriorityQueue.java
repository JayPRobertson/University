/*
* HeapPriorityQueue.java
*
* An implementation of a minimum PriorityQueue using a heap.
* based on the implementation in "Data Structures and Algorithms
* in Java", by Goodrich and Tamassia
*
* This implementation will throw a Runtime, HeapEmptyException
*	if the heap is empty and removeMin is called.
*
* This implementation will throw a Runtime, HeapFullException
*	if the heap is full and insert is called.
*
*/
public class HeapPriorityQueue<T extends Comparable<T>> implements PriorityQueue<T> {

	protected final static int DEFAULT_SIZE = 10000;
	
	protected T[] storage;
	protected int currentSize;
	
	// Feel free to change rootIndex to 0 if you want to 
	// use 0-based indexing (either option is fine)
	private static final int rootIndex = 0;

	/*
	 * Constructor that initializes the array to hold DEFAULT_SIZE elements
	 */
	@SuppressWarnings({"unchecked"})
	public HeapPriorityQueue(Class<T> dataType) {
		// Creating generics arrays in Java is not very clean. The following 
		// two lines allocate the generic array for you based on whether you
		// have selected to store the root at index 0 or 1 above.
		if (rootIndex == 0) {
			storage = (T[]) java.lang.reflect.Array.newInstance(dataType, DEFAULT_SIZE);
		} else {
			storage = (T[]) java.lang.reflect.Array.newInstance(dataType, DEFAULT_SIZE+1);
		}
		currentSize = 0;
	}
	
	/*
	 * Constructor that initializes the array to hold size elements
	 */
	@SuppressWarnings({"unchecked"})
	public HeapPriorityQueue(Class<T> clazz, int size) {
		// Creating generics arrays in Java is not very clean. The following 
		// two lines allocate the generic array for you based on whether you
		// have selected to store the root at index 0 or 1 above.
		if (rootIndex == 0) {
			storage = (T[]) java.lang.reflect.Array.newInstance(clazz, size);
		} else {
			storage = (T[]) java.lang.reflect.Array.newInstance(clazz, size+1);
		}
		currentSize = 0;
	}

	public void insert (T element) throws HeapFullException {
		if(currentSize >= storage.length){
			throw new HeapFullException();
		}
		storage[currentSize] = element;
		bubbleUp(currentSize);
		currentSize++;
    }
	
	private void bubbleUp(int index) {
		int parentIndex = (index-1)/2;
		if(index > rootIndex){
			if(storage[parentIndex].compareTo(storage[index])>0){
				swap(index, parentIndex);
				bubbleUp(parentIndex);
			}
		}
	}
			
	public T removeMin() throws HeapEmptyException {
		if(isEmpty()){
			throw new HeapEmptyException();
		}
		T x = storage[rootIndex];
		if(currentSize == 1){
			storage[rootIndex] = null;
			currentSize --;
		}else{
			swap(rootIndex, currentSize-1);
			currentSize--;
			bubbleDown(rootIndex);
		}

		return x;
	}

	private void swap(int x, int y){
		T q = storage[y];
		storage[y] = storage[x];
		storage[x] = q;

	}
	
	private void bubbleDown(int index) {
		if(currentSize > 1 && !isLeaf(index)){
			int smallChild = minChildIndex(index);
			if(storage[smallChild].compareTo(storage[index])<0){
				swap(index, smallChild);
				bubbleDown(smallChild);
			}
		}
	}

	private boolean isLeaf(int index){
		return 2*index+1 > currentSize-1;
	}

	private int minChildIndex(int index){ 
		//PRECONDITION: assumes storage[index] is not a Leaf
		int leftIndex = 2*index+1;
		int rightIndex = 2*index+2;
		if(rightIndex > currentSize-1 ||storage[rightIndex].compareTo(storage[leftIndex])>0){
			return leftIndex;
		}else{
			return rightIndex;
		}
	}

	public boolean isEmpty(){
		return currentSize == 0; 
	}
	
	public boolean isFull() {
		return currentSize >= storage.length;
	}
	
	public int size () {
		return currentSize;
	}

	public String toString() {
		String s = "";
		String sep = "";
		
		for (int i = 0; i < currentSize; i++) {
				s += sep + storage[i];
				sep = " ";				
			}
		return s;
	}
}
