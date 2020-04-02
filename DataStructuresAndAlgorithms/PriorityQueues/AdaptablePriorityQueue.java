/**
 * 
 * @author ChiangWei
 * @date 2020/4/2
 *
 */

public interface AdaptablePriorityQueue<K, V> {
	public abstract void remove(Entry<K, V> entry) throws IllegalArgumentException;
	public abstract void replaceKey(Entry<K, V> entry, K key) throws IllegalArgumentException;
	public abstract void replaceValue(Entry<K, V> entry, V value) throws IllegalArgumentException;
}
