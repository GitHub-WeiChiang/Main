/**
 * 
 * @author ChiangWei
 * @date 2020/3/16
 *
 */

import java.util.LinkedList;
import java.util.Queue;

public class TheJosephusProblem {
	public static void main(String[] args) {
		String[] a1 = {"Alice", "Bob", "Cindy", "Doug", "Ed", "Fred"};
		String[] a2 = {"Gene", "Hope", "Irene", "Jack", "Kim", "Lance"};
		String[] a3 = {"Mike", "Roberto"};
		System.out.println("First winner is " + josephus(buildQueue(a1), 3));
		System.out.println("Second winner is " + josephus(buildQueue(a2), 10));
		System.out.println("Third winner is " + josephus(buildQueue(a3), 7));

	}
	
	public static <E>Queue<E> buildQueue(E a[]) {
		Queue<E> queue = new LinkedList<>();
		for (int i = 0; i < a.length; i++) queue.add(a[i]);
		return queue;
	}
	
	public static <E>E josephus(Queue<E> queue, int k) {
		if (queue.isEmpty()) return null;
		while (queue.size() > 1) {
			for (int i = 0; i < k - 1; i++) queue.add(queue.poll());
			E e = queue.poll();
			System.out.println(e + " is out");
		}
		return queue.poll();
	}
}
