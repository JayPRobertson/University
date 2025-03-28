import java.util.*;
import java.lang.Math.*;

/*
 * An implementation of a binary search tree. This tree stores 
 * both keys and values associated with those keys.
 *
 * More information about binary search trees can be found here:
 * http://en.wikipedia.org/wiki/Binary_search_tree
 */
class BinarySearchTree <K extends Comparable<K>, V>  {

	public static final int BST_PREORDER  = 1;
	public static final int BST_POSTORDER = 2;
	public static final int BST_INORDER   = 3;

	// These are package friendly for the TreeView class
	BSTNode<K,V> root;
	int	count;

	public BinarySearchTree () {
		root = null;
		count = 0;
	}

	
	/* Purpose: Insert a new key-value element into the tree.  
	 *          If the key already exists in the tree, update 
	 *          the value stored at that node with the new value.
	 * Parameters: K key - the key for which the BST is ordered
     *	 		   V value - the value to associate with the key
	 * Returns: nothing
	 * Pre-Conditions: the tree is a valid binary search tree
	 */

	public void insert(K key, V value){
        if(key == null || value == null){
			return;
		}
		if(root == null){
            root =  new BSTNode<K,V>(key, value);
			count++;
        }else{
            boolean didUpdate = insertRec(root, key, value);
			if(didUpdate==false){
				count++;
			}
        }
    }

    private boolean insertRec(BSTNode<K,V> cur, K key, V value){
        if(key.compareTo(cur.key) == 0){
			cur.value = value;
			return true;
		}else if (key.compareTo(cur.key) > 0){
	        if (cur.left != null){
                insertRec(cur.left, key, value);
            }else{
               cur.left = new BSTNode<K,V>(key, value);
            }
        }else{
            if (cur.right !=null){
                insertRec(cur.right, key, value);
            }else{
                cur.right = new BSTNode<K,V>(key, value);
            }
        }
		return false;
	}

	/* 	
	 * Purpose: Get the value of the given key. 
	 * Parameters: K key - the key to search for
	 * Returns: V - the value associated with the key
	 * Pre-conditions: the tree is a valid binary search tree
	 * Throws: KeyNotFoundException if key isn't in the tree
	 */
	public V find (K key) throws KeyNotFoundException {
		V found = findRec(root, key);
		if(found == null){
			throw new KeyNotFoundException();
		}
		return found;
	}

    private V findRec(BSTNode<K,V> cur, K key) {
        if(cur == null){
            return null;
        }
        if(key.compareTo(cur.key)== 0){
            return cur.value;
        }

        if(cur.key.compareTo(key) < 0){
            return findRec(cur.left, key);
        }else{
			return findRec(cur.right, key);
		}
    }

	/* 	
	 * Purpose: Get the number of nodes in the tree.
	 * Parameters: none
	 * Returns: int - the number of nodes in the tree. 
	 */
	public int size() {
		return count; 
	}

	/*
	 * Purpose: Remove all nodes from the tree.
	 * Parameters: none
	 * Returns: nothing
	 */
	public void clear() {
		root = null;
		count = 0;
	}

	/* 
	 * Purpose: Get the height of the tree. 
	 * Parameters: none
	 * Returns: int - the height of the tree
	 * Example: We define height as being the number of 
	 * arrows that need to be followed on the path from 
	 * the root to the deepest leaf node. This means that 
	 * a tree with one node (just the root) has height 0,
	 * and an empty tree (root is null) has height -1.
	 *
	 * See the assignment PDF and the test program for examples.
	 */
	public int height() {
		return heightRec(root);
	}

	private int heightRec(BSTNode<K,V> cur) {
		if(cur == null){
			return -1;
		}else{
			return 1+ Math.max(heightRec(cur.left), heightRec(cur.right));
		}
	}

	/* 
	 * Purpose: Return a list of all the key-value Entry elements 
	 *          stored in the tree using a level-order traversal.
	 * Parameters: None
	 * Returns: List<Entry<K,V>> - a list of key-value entries
	 *
	 * Example: A level order traversal of a tree cannot be done 
	 *          without the help of a secondary data structure.
	 *
	 *          It is commonly implemented using a queue of nodes 
	 *          as the secondary data structure. You will still be 
	 *          adding the "visited" elements to l as you do in the 
	 *          other traversal methods but you will create an 
	 *          additional q to hold nodes still to visit. This is
	 *          similar to what we did in the worksheet on tree traversals.
	 *
	 * From wikipedia (they call it breadth-first), the algorithm 
	 * for level order is:
	 *
	 *  levelorder()
	 *      q = empty queue
	 *      q.enqueue(root)
	 *      while not q.empty do
	 *          node := q.dequeue()
	 *          visit(node)
	 *          if node.left != null then
	 *                q.enqueue(node.left)
	 *          if node.right != null then
	 *                q.enqueue(node.right)
	 *
	 * Note that you can use the Java LinkedList as a Queue
	 * and then use only the removeFirst() and addLast() methods on q
	 */
	public List<Entry<K,V>>	entryList() {
		// list to add all the nodes to
		List<Entry<K,V> > l = new LinkedList<Entry<K,V>>();
		
		// queue of nodes that need to be added
		LinkedList<BSTNode<K,V>> q = new LinkedList<BSTNode<K,V> >();
		
		q.addLast(root);
		while (q.size() != 0){
			BSTNode<K,V> first= q.removeFirst();
	        if (first.right != null){
				q.addLast(first.right);
			  }
			if (first.left != null){
				q.addLast(first.left);
			}  
			
			l.add(new Entry<K,V>(first.key, first.value));
		}

		return l;
	}

	/* 	
	 * Purpose: Get a list of all the key-value entries stored in the tree
	 * Parameters: int whichTraversal - the type of traversal to perform:
	 * Returns: List<Entry<K,V>> - a list of key-value entries
	 * Example: The list will be constructed by performing a traversal
	 * specified by the parameter whichTraversal.
	 * 
	 * If whichTraversal is:
	 *	 BST_PREORDER	perform a pre-order traversal
	 *	 BST_POSTORDER	perform a post-order traversal
	 *	 BST_INORDER	perform an in-order traversal
	 */
	public List<Entry<K,V> > entryList (int which) {
		List<Entry<K,V> > entries = new LinkedList<Entry<K,V> >();

		if (which == BST_PREORDER) {
			preOrderRec(root, entries);
		}
		else if (which == BST_INORDER) {
			inOrderRec(root, entries);
		}
		else if (which == BST_POSTORDER) {
			postOrderRec(root, entries);
		}
		return entries;
	}

	private void inOrderRec (BSTNode<K,V> cur, List <Entry<K,V>> entries) {
		if(cur == null){
			return;
		}
		
		Entry<K,V> curEntry = new Entry<K,V>(cur.key, cur.value);
		inOrderRec(cur.right, entries);
		entries.add(curEntry);
		inOrderRec(cur.left, entries);
		

	}

	private void preOrderRec (BSTNode<K,V> cur, List <Entry<K,V>> entries) {
		if(cur == null){
			return;
		}
		
		Entry<K,V> curEntry = new Entry<K,V>(cur.key, cur.value);
		entries.add(curEntry);
		preOrderRec(cur.right, entries);
		preOrderRec(cur.left, entries);
	}

	private void postOrderRec (BSTNode<K,V> cur, List <Entry<K,V>> entries) {
		if(cur == null){
			return;
		}
		
		Entry<K,V> curEntry = new Entry<K,V>(cur.key, cur.value);
		postOrderRec(cur.right, entries);
		postOrderRec(cur.left, entries);
		entries.add(curEntry);
	}

}