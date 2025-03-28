public class LinkedBookList {
	private BookNode head;
	private BookNode tail;

	public LinkedBookList() {
		head = null;
		tail = null;
	}

	public void addFront (Book data) {
		BookNode n = new BookNode(data);
		if (head == null) {
			tail = n;
		}
		n.next = head;
		head = n;
	}

	public void addBack (Book data){
		BookNode n = new BookNode(data);
		if(head == null) {
			head = n;
		} else {
			tail.next = n;
		}
		tail = n;
	}

	public boolean isEmpty() {
		return head == null;
	}

	public Book get (int position) {
		return getRec(head, 0, position);
	}
	
	private Book getRec(BookNode cur, int i, int position) {
		if (i == position) {
			return cur.getData();
		} else {
			return getRec(cur.next, i+1, position);
		}
	}
	
	public Book removeFront() {
		if (head == null) { // list is empty case
			return null; 
		} else if (head == tail) {
			tail = null; // one element case
		}
		
		Book toReturn = head.getData();
		head = head.next;
		return toReturn;		
	}
	
	public Book removeBack() {
		if (head == null) { // list is empty case
			return null; 
		} 
		
		Book toReturn = tail.getData();
		
		if (head == tail) {
			head = null;
			tail = null;
		} else {
			BookNode cur = getTailPrev(head);
			cur.next = null; 
			tail = cur;
		}
		return toReturn;		
	}
	
	private BookNode getTailPrev(BookNode cur) {
		if (cur.next == null) {
			return cur;
		} else {
			return getTailPrev(cur.next);
		}
	}

	/* Purpose: create a string representation of list
	 * Parameters: nothing	 
	 * Returns: String - the string representation of the list
	 */
	public String toString() {
		if (head == null) {
			return "{}";
		} else {
			return "{" + toStringRec(head) + "}";
		}
	}
	
	private String toStringRec(BookNode cur) {
		if (cur == null) {
			return "";
		} else if (cur.next == null) {
			return cur.getData().toString();
		} else {
			return cur.getData().toString() + ", " + toStringRec(cur.next);
		}
	}

	/*
	 * Purpose: Insert all elements from array into this linked list
	 * Parameters: T[] array - the elements to add to this list
	 * Returns void - nothing
	 */
	public void buildFromArray(Book[] array) {
		buildFromArrayRec(array, 0);
	}
	
	private void buildFromArrayRec(Book[] array, int i) {
		if (i == array.length) {
			return;
		} else {
			addBack(array[i]);
			buildFromArrayRec(array, i+1);
		}
	}

	/*
	 * Purpose: get the total number of books in this list
	 * Parameters: none
	 * Returns: int - the number of books in the list
	 */
	public int totalBooks() {
		return totalBooksRec(head);
	}

	public int totalBooksRec(BookNode h){
		if(h == null){
			return 0;
		}else{
			return 1+totalBooksRec(h.next);
		}
	}

	/*
	 * Purpose: get the total number of pages of all books in this list
	 * Parameters: none
	 * Returns: int - the number of pages in all books in the list
	 */
	public int totalPages() {
		return totalPagesRec(head);
	}

	public int totalPagesRec(BookNode h){
		if(h ==null){
			return 0;
		}else{
			return h.getData().getPages() + totalPagesRec(h.next);
		}
	}
	
	/*
	 * Purpose: get the number of books in this list with more
	 *          pages than the given book
	 * Parameters: Book sampleBook - the book to compare pages with
	 * Returns: int - the number of books in this list with more
	 *                pages than sampleBook
	 */
	public int countLongerThan(Book sampleBook) {
		return countLongerThanRec(sampleBook, head);
	}

	public int countLongerThanRec(Book sampleBook, BookNode h){
		if(h == null){
			return 0;
		}else{
			if(h.getData().getPages()> sampleBook.getPages()){
				return 1 + countLongerThanRec(sampleBook, h.next);
			}else{
				return countLongerThanRec(sampleBook, h.next);
			}
		}
	}
		
	/*
	 * Purpose: get the number pages found in all books that come before
	 *          the first occurrence of a book written by authorName
	 * Parameters: String authorName - the name of the target author
	 * Returns: int - the sum of all pages of books in the list that come
	 *                before the first book written by authorName
	 * Preconditions: a book written by authorName is in this list
	 */
	public int pagesBeforeBookByAuthor(String authorName) {
		return pagesBeforeBookByAuthorRec(authorName, head);
	}

	public int pagesBeforeBookByAuthorRec(String authorName, BookNode h){
		if(h == null || h.getData().getAuthor().equals(authorName)){
			return 0;
		}else{
			return h.getData().getPages() + pagesBeforeBookByAuthorRec(authorName, h.next);
		}
	}
	
	/*
	 * Purpose: get the book with the most pages in this list
	 * Parameters: none
	 * Returns: Book - the book with the most pages
	 *
	 * If the largest two books have the same number of pages
	 * the book that is found first in the list is returned
	 */
	public Book longestBook() {
		if (head == null) { //if list is empty
			return null;
		} else if (head.next == null) { //if list only has one element
			return head.getData();
		} else {
			return longestBookRec(head, head.getData());
		}
	}
	
	/*
	 * Complete the design of the recursive helper below
	 */
	 
	/*
	 * Purpose: get the book with the most pages in this list
	 *          from cur onward
	 * Parameters: BookNode cur - the current node
	 *             Book longest - the longest book seen so far
	 * Returns: Book - the book with the most pages
	 *  
	 * If the largest two books have the same number of pages
	 * the book that is found first in the list is returned
	 */
	private Book longestBookRec(BookNode cur, Book longest) {
		if(cur == null){
			return longest;
		}else{
			if(cur.getData().getPages() > longest.getPages()){
				return longestBookRec(cur.next, cur.getData());
			}else{
				return longestBookRec(cur.next, longest);
			}
		}
	}
	
	/*
	 * Purpose: get the number of books in the list between the first 
	 *          two occurrences of books written by authorName
	 * Parameters: String authorName - the name of the target author
	 * Returns int - the number of books in this list found between the
	 *               first two occurrences of books written by authorName
	 * Preconditions - there are at least two books written by authorName
	 *                 in this list
	 */
	public int distanceBetweenBooksByAuthor(String authorName) {
		return distanceBetweenBooksByAuthorRec(head, authorName, false);
	}
	
	/*
	 * Complete the design of the recursive helper below
	 */
	
	/*
	 * Purpose: get the number of books in the list between the first 
	 *          two occurrences of books written by authorName
	 * Parameters: String authorName - the name of the target author
	 *             boolean found - true if the first book by author was found
	 * Returns int - the number of books in this list found between the
	 *               first two occurrences of books written by authorName
	 * Preconditions - there are at least two books written by authorName
	 *                 in this list
	 */
	private int distanceBetweenBooksByAuthorRec(BookNode cur, String authorName, boolean firstBookFound) {
		if(firstBookFound == false){
			if(cur.getData().getAuthor().equals(authorName)){
				return distanceBetweenBooksByAuthorRec(cur.next, authorName, true);
			}else{
				return distanceBetweenBooksByAuthorRec(cur.next, authorName, false);
			}
		}else{
			if(cur.getData().getAuthor().equals(authorName)){
				return 0;
			}else{
				return 1 + distanceBetweenBooksByAuthorRec(cur.next, authorName, true);
			}
		}
	}


}