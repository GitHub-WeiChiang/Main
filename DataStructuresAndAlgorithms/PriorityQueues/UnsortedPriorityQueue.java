/**
 * 
 * @author ChiangWei
 * @date 2020/3/30
 *
 */

import java.util.Comparator;

public class UnsortedPriorityQueue<K, V> extends AbstractPriorityQueue<K, V> {
	public static void main(String[] args) {
		UnsortedPriorityQueue<Integer, Integer> upq = new UnsortedPriorityQueue<>();
		upq.insert(1, 1);
		upq.insert(5, 5);
		upq.insert(2, 2);
		upq.insert(4, 4);
		upq.insert(3, 3);
		System.out.println(upq.min().getKey());
		upq.removeMin();
		System.out.println(upq.min().getKey());
		upq.removeMin();
		System.out.println(upq.min().getKey());
		upq.removeMin();
		System.out.println(upq.min().getKey());
		upq.removeMin();
		System.out.println(upq.min().getKey());
		upq.removeMin();
	}
	
	private PositionalList<Entry<K, V>> list = new LinkedPositionalList<>();
	
	public UnsortedPriorityQueue() {
		super();
	}
	
	public UnsortedPriorityQueue(Comparator<K> comp) {
		super(comp);
	}
	
	private Position<Entry<K, V>> findMin() {
		Position<Entry<K, V>> small = list.first();
		for (Position<Entry<K, V>> walk : list.positions()) {
			if (compare(walk.getElement(), small.getElement()) < 0) {
				small = walk;
			}
		}
		return small;
	}
	
	public Entry<K,V> insert(K key, V value) throws IllegalArgumentException {
		checkKey(key);
		Entry<K, V> newest = new PQEntry<>(key, value);
		list.addLast(newest);
		return newest;
	}
	
	public Entry<K, V> min() {
		if (list.isEmpty()) return null;
		return findMin().getElement();
	}
	
	public Entry<K, V> removeMin() {
		if (list.isEmpty()) return null;
		return list.remove(findMin());
	}
	
	public int size() {
		return list.size();
	}
}
