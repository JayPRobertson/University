public class ArrayBasedBinarySearchTree extends ArrayBasedBinaryTree{
    
    public void insert(Integer value){
        if(data[root] == null){
           data[root] = value;
        }else{
            insertRec(root, value);
        }
        size++;
    }

    private void insertRec(int cur, Integer value){
        if (value <= data[cur]){
	        if (data[getLeft(cur)] != null){
                insertRec(getLeft(cur), value);
            }else{
                data[getLeft(cur)] = value;
            }
        }else{
            if (data[getRight(cur)] !=null){
                insertRec(getRight(cur), value);
            }else{
                data[getRight(cur)] = value;
            }
        }
    }

    public static void main(String[] args) {
        ArrayBasedBinarySearchTree emptyTree = new ArrayBasedBinarySearchTree();
        
        ArrayBasedBinarySearchTree myTree = new ArrayBasedBinarySearchTree();
        myTree.insert(2);
        myTree.inOrder();
        myTree.insert(1);
        myTree.inOrder();
        myTree.insert(5);
        myTree.inOrder();
        myTree.insert(7);
        myTree.inOrder();
        myTree.insert(0);
        myTree.inOrder();
        myTree.insert(4);
        myTree.inOrder();
        myTree.insert(6);
        myTree.inOrder();
        
        System.out.println("in");
        myTree.inOrder();
        System.out.println("pre");
        myTree.preOrder();
        System.out.println("post");
        myTree.postOrder();
        
        System.out.println("toString\n" + myTree);
    }



}
