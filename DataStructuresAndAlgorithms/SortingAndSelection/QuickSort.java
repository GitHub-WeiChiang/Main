
/**
 * 
 * @author ChiangWei
 * @date 2020/4/16
 *
 */

import java.util.Comparator;
import java.util.LinkedList;
import java.util.Queue;

public class QuickSort {
	public static void main(String[] args) {
		Comparator<Integer> comp = new Comparator<>() {
			public int compare(Integer arg0, Integer arg1) {
				return arg0.compareTo(arg1);
			}
		};
		
		Queue<Integer> queue = new LinkedList<>();
		queue.add(0); queue.add(6); queue.add(3);
		queue.add(7); queue.add(1); queue.add(8);
		queue.add(4); queue.add(5); queue.add(2);
		quickSort(queue, comp);
		for (Integer i : queue) {
			System.out.println(i);
		}
	}

	public static <K> void quickSort(Queue<K> S, Comparator<K> comp) {
		int n = S.size();
		if (n < 2) {
			return;
		}
		K pivot = S.peek();
		Queue<K> L = new LinkedList<>();
		Queue<K> E = new LinkedList<>();
		Queue<K> G = new LinkedList<>();
		while (!S.isEmpty()) {
			K element = S.poll();
			int c = comp.compare(element, pivot);
			if (c < 0) {
				L.add(element);
			} else if (c == 0) {
				E.add(element);
			} else {
				G.add(element);
			}
		}
		quickSort(L, comp);
		quickSort(G, comp);
		while (!L.isEmpty()) {
			S.add(L.poll());
		}
		while (!E.isEmpty()) {
			S.add(E.poll());
		}
		while (!G.isEmpty()) {
			S.add(G.poll());
		}
	}
}
