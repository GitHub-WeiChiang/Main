/**
 * 
 * @author ChiangWei
 * @date 2020/4/15
 *
 */

import java.util.Comparator;
import java.util.LinkedList;
import java.util.Queue;

public class LinkedListsBasedImplementationOfMergeSort {
	public static void main(String[] args) {
		Comparator<Integer> comp = new Comparator<>() {
			public int compare(Integer arg0, Integer arg1) {
				return arg0.compareTo(arg1);
			}
		};
		
		Queue<Integer> queue = new LinkedList<>();
		queue.add(0);	queue.add(3);
		queue.add(1);	queue.add(9);
		queue.add(6);	queue.add(4);
		queue.add(5);	queue.add(2);
		queue.add(7);	queue.add(8);
		mergeSort(queue, comp);
		for (Integer i : queue) {
			System.out.print(i);
		}
	}

	public static <K> void merge(Queue<K> S1, Queue<K> S2, Queue<K> S, Comparator<K> comp) {
		while (!S1.isEmpty() && !S2.isEmpty()) {
			if (comp.compare(S1.peek(), S2.peek()) < 0) {
				S.add(S1.poll());
			} else {
				S.add(S2.poll());
			}
		}
		while (!S1.isEmpty()) {
			S.add(S1.poll());
		}
		while (!S2.isEmpty()) {
			S.add(S2.poll());
		}
	}

	public static <K> void mergeSort(Queue<K> S, Comparator<K> comp) {
		int n = S.size();
		if (n < 2) {
			return;
		}
		Queue<K> S1 = new LinkedList<>();
		Queue<K> S2 = new LinkedList<>();
		while (S1.size() < n / 2) {
			S1.add(S.poll());
		}
		while (!S.isEmpty()) {
			S2.add(S.poll());
		}
		mergeSort(S1, comp);
		mergeSort(S2, comp);
		merge(S1, S2, S, comp);
	}
}
