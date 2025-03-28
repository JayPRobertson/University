import java.lang.Math;
import java.util.LinkedList;
/*
 * RefBasedBinaryTree.java
 *
 * A ref-based BinaryTree meant to store values of type Integer
 */
public class RefBasedBinaryTree implements BinaryTree {
    protected TreeNode root;
    
    public RefBasedBinaryTree() {
        this.root = null;
    }
    
    public void insert(Integer value){
        if (root==null) {
            root = new TreeNode(value);
        } else {
            insert(null, root, value);
		}
        
    }
    // not a balanced insert
    private void insert(TreeNode parent, TreeNode t, Integer value) {
        if (t==null) {
            if(parent.getLeft()==null) {
                parent.setLeft(new TreeNode(value));
			} else {
                parent.setRight(new TreeNode(value));
			}            
        }  else {
            int htLeft = height(t.getLeft());
            int htRight = height(t.getRight());
            if (htLeft>htRight) {
                insert(t, t.getRight(), value);
			} else {
                insert(t, t.getLeft(), value);
			}
        }
    }
    
    private int height(TreeNode t) {
        if (t==null) {
            return -1;
		} else {
            int highest = Math.max(height(t.getLeft()), height(t.getRight()));
            return 1 + highest;
        }
    }

     /*
    * Method name: sum
    * Purpose: computes the sum of all elements in this BinaryTree
    * Parameters: none
    * Returns: int – the sum
    */
    public int sum(){
        return sum(root);
    }

    private int sum(TreeNode t){
        if(t == null){
            return 0;
        }else{
            return t.getValue() + sum(t.getLeft())+ sum(t.getRight());
        }
    }

    /*
    * Method name: find
    * Purpose: determines whether val is in this BinaryTree
    * Parameters: int val
    * Returns: boolean – true if val is found, false otherwise
    */
    public boolean find(int val) { 
        return find(root, val) > 0;
    }
    
    private int find(TreeNode cur, int val) {
        if(cur == null){
            return 0;
        }
        if(cur.getValue() == val){
            return 1;
        }
        return 0 + find(cur.getLeft(), val) + find(cur.getRight(), val);
    }

    /*
    * Method name: getMax
    * Purpose: gets and returns the largest value in this BinaryTree
    * Parameters: none
    * Throws: TreeEmptyException if called on an empty tree
    * Returns: int – the largest value
    */
    public int getMax() throws TreeEmptyException{
        if(root == null){
            throw new TreeEmptyException();
        }else{
            return getMaxRec(root, 0);
        }
    }

    private int getMaxRec(TreeNode cur, int highest){ //DOESN'T WORK!!!!
        if (cur == null){
            return highest;
        }
        if(cur.getValue() > highest){
            highest = cur.getValue();
        }
        return Math.max(getMaxRec(cur.getLeft(), highest), getMaxRec(cur.getRight(), highest));
    }
    
    /*
     * Purpose: prints the value at each TreeNode in this BinaryTree
     *          following an in-order traversal
     * Parameters: none
     * Returns: Nothing
     */
    public void inOrder(){
        inOrder(root);
        System.out.println();
    }
    
    /*
     * Purpose: prints the value at each TreeNode in t,
     *          following an in-order traversal
     * Parameters: TreeNode t
     * Returns: Nothing
     */
    private void inOrder(TreeNode t){
        if (t==null) {
            return;
        } else {
            inOrder(t.getLeft());
            System.out.print(t.getValue() + " ");
            inOrder(t.getRight());
        }
    }
    
    /*
     * Purpose: prints the value at each TreeNode in this BinaryTree
     *          following a pre-order traversal
     * Parameters: none
     * Returns: Nothing
     */
    public void preOrder(){
        preOrder(root);
        System.out.println();
    }
    
    /*
     * Purpose: prints the value at each TreeNode in t,
     *          following a pre-order traversal
     * Parameters: TreeNode t
     * Returns: Nothing
     */
    private void preOrder(TreeNode t){
        if (t==null) {
            return;
        } else {
            System.out.print(t.getValue() + " ");
            preOrder(t.getLeft());
            preOrder(t.getRight());
        }
    }
    
    /*
     * Purpose: prints the value at each TreeNode in this BinaryTree
     *          following a post-order traversal
     * Parameters: none
     * Returns: Nothing
     */
    public void postOrder(){
        postOrder(root);
        System.out.println();
    }
    
    /*
     * Purpose: prints the value at each TreeNode in t,
     *          following a post-order traversal
     * Parameters: TreeNode t
     * Returns: Nothing
     */
    private void postOrder(TreeNode t){
        if (t==null) {
            return;
        } else {
            postOrder(t.getLeft());
            postOrder(t.getRight());
            System.out.print(t.getValue() + " ");
        }
    }
    
    /*
     * Purpose: returns a String reprensentation of this BinaryTree
     * Parameters: none
     * Returns: String - the representation
     */
    public String toString() {
        return toString(root);
    }
    
    private String toString(TreeNode t) {
        if(t==null) {
            return "";
        } else {
            String s = "";
            
            s += toString(t.getLeft());
            s += t.getValue() + " ";
            s += toString(t.getRight());
            
            return s;
        }
    }
    
    
    public static void main(String[] args) {
        // use these trees to test the methods you will implement in Part II
        RefBasedBinaryTree emptyTree = new RefBasedBinaryTree();
        RefBasedBinaryTree myTree = new RefBasedBinaryTree();
        RefBasedBinaryTree newTree = new RefBasedBinaryTree();

        for(int i=2; i<8; i++) {
            myTree.insert(i);
        }

        newTree.insert(11);

        System.out.println("in");
        myTree.inOrder();
        System.out.println("pre");
        myTree.preOrder();
        System.out.println("post");
        myTree.postOrder();

        System.out.println("\nPrinting sum:");
        System.out.println("should be 0: " +emptyTree.sum());
        System.out.println("should be 27: " +myTree.sum());
        System.out.println("should be 11: " +newTree.sum());

        System.out.println("\nPrinting find:");
        System.out.println("should be true: " +myTree.find(2));
        System.out.println("should be false: " +myTree.find(8));
        System.out.println("should be true: " +myTree.find(7));
        System.out.println("should be true: " +newTree.find(11));
        System.out.println("should be false: " +newTree.find(0));
        System.out.println("should be false: " +emptyTree.find(2));

        System.out.println("\nPrinting getMax:");
        try{
            int x = emptyTree.getMax();
            System.out.println(x);
        }catch (TreeEmptyException e){
            System.out.println("Tree is empty when it should be.");
        }

        try{
            int x = myTree.getMax();
            System.out.println("should be 7: "+x);
        }catch (TreeEmptyException e){
            System.out.println("Tree is empty when it shouldn't be!");
        }

        try{
            int x = newTree.getMax();
            System.out.println("should be 11: "+x);
        }catch (TreeEmptyException e){
            System.out.println("Tree is empty when it shouldn't be!");
        }
    }
    
}
