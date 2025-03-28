/*
 * ArrayBasedBinaryTree.java
 *
 * An array-based BinaryTree meant to store values of type Integer
 */
public class ArrayBasedBinaryTree implements BinaryTree {
    private static final int CAPACITY = 5;
    protected Integer[] data;
    protected int root;
    protected int size;
    
	public ArrayBasedBinaryTree() {
		data = new Integer[CAPACITY];
		root = 1;
		size = 0;

		// allocate space for data array.
		// What index are you choosing the root to be?
		// initialize your size as the number of elements in the empty tree
	}

	/*
	 * Purpose: inserts the given value into data at next available
	 *  position in a level-order traversal
	 *  The tree remains complete after insertion.
	 * Parameters: Integer value - value to insert
	 * Returns: nothing
	 */
	public void insert(Integer value){
		System.out.println("size: " + size);
		if(size+1>= data.length){
			expandAndCopy();	
		}
		data[size+1] = value;
		size++;
		
		// NOTE: The underlying data structure is an array,
		//  but we are just USING the array to store the data.
		//  The way we traverse the data will expose its binary tree structure
	}

	protected void expandAndCopy() {
		Integer[] newData = new Integer[data.length*2];
		for(int i=1; i<data.length; i++) {
			newData[i] = data[i];
		}
		data = newData;
	}

	/*
	 * Purpose: calculates and returns the index of t's left child
	 * Parameters: int t - index of current element in this ArrayBasedBinaryTree
	 * Returns: int - index of left child
	 */
	protected int getLeft(int t) {
		return t*2;
	}

	/*
	 * Purpose: calculates and returns the index of t's right child
	 * Parameters: int t - index of current element in this ArrayBasedBinaryTree
	 * Returns: int - index of right child
	 */
	protected int getRight(int t) {
		return (t*2)+1;
	}


	public void inOrder(){
		inOrderRec(root);
	}

	public void inOrderRec(int t){
		if(t >= size+1){
			return;
		}
		inOrderRec(getLeft(t));
		System.out.println(data[t]);
		inOrderRec(getRight(t));
	}

	public void preOrder(){
		preOrderRec(root);
	}

	public void preOrderRec(int t){
		if(t >= size+1){
			return;
		}
		System.out.println(data[t]);
		inOrderRec(getLeft(t));
		inOrderRec(getRight(t));
	}


	public void postOrder(){
		postOrderRec(root);
	}

	public void postOrderRec(int t){
		if(t >= size+1){
			return;
		}
		inOrderRec(getLeft(t));
		inOrderRec(getRight(t));
		System.out.println(data[t]);
	
	}


	public int height() {
		return heightRec(root);
	}

	/*
	 * Purpose: computes and returns the height of a 
	 *          binary tree rooted at index t 
	 * Parameters: TreeNode t - the BinaryTree
	 * Returns: int - the height
	 * NOTE: a BinaryTree with no nodes is height -1
	 *       a BinaryTree with just a root is height 0
	 *
	 *       the height of a node in a tree is equal to 
	 *       1 + the height of its largest subtree
	 */
	protected int heightRec(int t) {
		if (t >= size+1) {
            return 0;
        }else if(size == 0){
			return -1;
		}
		return 1+max(heightRec(getLeft(t)), heightRec(getRight(t))); 
	}

	public int max(int x, int y){
		if(x>=y){
			return x;
		}else{
			return y;
		}
	}
	
	/*
	 * Purpose: returns a String reprensentation of a in-order traversal
	 *     of this ArrayBasedBinaryTree
	 * Parameters: none
	 * Returns: String - the representation
	 */
	// written for you - do not change
	// NOTICE: we use the helper methods to get the index of the left/right
	//   children of the current position in the tree.
	// This method will not work until you have completed those methods correctly.
	public String toString() {
		return toString(root);
	}

	private String toString(int t) {
        if (t >= size+1) {
            return "";
        } 
        String s = "";
        s += toString(getLeft(t));
        s += data[t] + " ";
        s += toString(getRight(t));

        return s;
	}

	public static void main(String[] args) {
		ArrayBasedBinaryTree myTree = new ArrayBasedBinaryTree();

		//             ` 2
		//             /    \
		//            /      \
		//           /        \
		//          /          \  
		//         3             4
		//       /   \         /  
		//      5     6       7    

		System.out.println();
		for(int i=2; i<8; i++) {
			myTree.insert(i);
			System.out.println(myTree.toString());
		}
		System.out.println("in");
		myTree.inOrder();
		System.out.println("pre");
		myTree.preOrder();
		System.out.println("post");
		myTree.postOrder();
		
		System.out.println("height");
		System.out.println(myTree.height());
		
		System.out.println("toString\n" + myTree);
	}
    
}
