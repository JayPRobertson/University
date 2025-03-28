import java.util.*;

public class HashMap<K extends Comparable<K>, V> implements Map<K,V> {

	private List<List<Entry<K,V>>> 	table;
	private int	count;
	private int  tableSize;

	// For Part III
	private long getLoops;
	private long putLoops;
	

	public HashMap() {
		tableSize = 1000003; // prime number
		table = new ArrayList<List<Entry<K,V>>>(tableSize);

		// initializes table as a list of empty lists
		for (int i = 0; i < tableSize; i++) {
			table.add(new LinkedList<Entry<K,V>>());
		}

		count = 0;

		// For Part III:
		resetGetLoops();
		resetPutLoops();
	}

	// For Part III
	public long getGetLoopCount() {
		return getLoops;
	}

	// For Part III
	public long getPutLoopCount() {
		return putLoops;
	}

	// For Part III
	public void resetGetLoops() {
		getLoops = 0;
	}
	
	// For Part III
	public void resetPutLoops() {
		putLoops = 0;
	}

	public boolean containsKey(K key) {
		try{
			get(key);
			return true;
		}catch (KeyNotFoundException e){
			return false;
		}
	}

	public V get (K key) throws KeyNotFoundException {
		int index = Math.abs(key.hashCode()) % tableSize;
		List<Entry<K,V>> listAtIndex = table.get(index);
		int position = getListRec(key, 0, listAtIndex);
		
		return listAtIndex.get(position).getValue();
	}

	private int getListRec(K key, int cur, List<Entry<K,V>> list) throws KeyNotFoundException{
		if(list.size() == 0 || list.get(cur) == null){
			throw new KeyNotFoundException();
		}
		if(list.get(cur).getKey().equals(key)){
			return cur;
		}
		return getListRec(key, cur+1, list);
	}


	public List<Entry<K,V> > entryList() {
		List <Entry<K,V>> resultList = new LinkedList<Entry<K,V>>();
		Iterator<List<Entry<K,V>>> tableIter = table.iterator();
		
		while(tableIter.hasNext()){
			List<Entry<K,V>> aList = tableIter.next();
			Iterator<Entry<K,V>> listIter = aList.iterator();
			while(listIter.hasNext()){
				Entry<K,V> e = listIter.next();
				resultList.add(e);
			}
		}
		return resultList;
	}
	
	public void put (K key, V value){
		Entry insert = new Entry(key, value);
		int index = Math.abs(key.hashCode())%tableSize;
		List<Entry<K,V>> listAtIndex = table.get(index);
		
		boolean didUpdate = putRec(0, insert, listAtIndex);
		if(didUpdate == false){
			count++;
		}
	}
	
	//returns true if a value in list is updated, false otherwise
	private boolean putRec(int cur, Entry insert, List<Entry<K,V>> list){
		if(cur > list.size()-1){
			list.add(insert);
			return false;
		}
		if(list.get(cur).getKey().equals(insert.getKey())){
			list.set(cur, insert);
			return true;
		}
		return putRec(cur+1, insert, list);
	}

	public int size() {
		return count;
	}

    public void clear() {
		for(int i = 0; i < tableSize; i++) {
			table.get(i).clear();
		}
        count = 0;
    }

}