import java.lang.Math;
/*
 * RefBasedBinarySearchTree.java
 *
 * A ref-based BinaryTree meant to store values of type Integer
 */
public class RefBasedBinarySearchTree extends RefBasedBinaryTree {

    public void insert(Integer value){
        if(root == null){
            root = new TreeNode(value);
        }else{
            insertRec(root, value);
        }
    }

    private void insertRec(TreeNode cur, Integer value){
        if (value <= cur.getValue()){
	        if (cur.getLeft() != null){
                insertRec(cur.getLeft(), value);
            }else{
               cur.setLeft(new TreeNode(value));
            }
        }else{
            if (cur.getRight() !=null){
                insertRec(cur.getRight(), value);
            }else{
                cur.setRight(new TreeNode(value));
            }
        }
    }
    
    /*
    * Method name: find
    * Purpose: determines whether val is in this BinaryTree
    * Parameters: int val
    * Returns: boolean – true if val is found, false otherwise
    */
    public boolean find(int val) {
        return findRec(root, val);
    }

    private boolean findRec(TreeNode cur, int val) {
        if(cur == null){
            return false;
        }
        if(cur.getValue() == val){
            return true;
        }

        if(cur.getValue()!= val){
            return findRec(cur.getRight(),val);
        }
        return findRec(cur.getRight(), val);
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
            return getMax(root);
        }
    }

    private int getMax(TreeNode cur){
        if(cur.getRight() == null){
            return cur.getValue();
        }else{
            return getMax(cur.getRight());
        }
    }
    

    public static void main(String[] args) {
        // use these trees to test the methods you will implement
        RefBasedBinarySearchTree emptyTree = new RefBasedBinarySearchTree();
        RefBasedBinarySearchTree myTree = new RefBasedBinarySearchTree();
        myTree.insert(2);
        myTree.insert(1);
        myTree.insert(5);
        myTree.insert(7);
        myTree.insert(0);
        myTree.insert(4);
        myTree.insert(6);
        
        System.out.println("in");
        myTree.inOrder();
        System.out.println("pre");
        myTree.preOrder();
        System.out.println("post");
        myTree.postOrder();
        
        System.out.println("toString\n" + myTree);

        System.out.println("\nPrinting sum:");
        System.out.println("should be 0: " +emptyTree.sum());
        System.out.println("should be 25: " +myTree.sum());

        System.out.println("\nPrinting find:");
        System.out.println("should be true: " +myTree.find(2));
        System.out.println("should be false: " +myTree.find(8));
        System.out.println("should be true: " +myTree.find(7));
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
    }
}
