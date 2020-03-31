/**
 * 
 * @author ChiangWei
 * @date 2020/3/31
 *
 */

public class SortingWithAPriorityQueue {
	public static <E> void pqSort(PositionalList<E> s, PriorityQueue<E, ?> p) {
		int n = s.size();
		for (int j = 0; j < n; j++) {
			E element = s.remove(s.first());
			p.insert(element, null);
		}
		for (int j = 0; j < n; j++) {
			E element = p.removeMin().getKey();
			s.addLast(element);
		}
	}
}
