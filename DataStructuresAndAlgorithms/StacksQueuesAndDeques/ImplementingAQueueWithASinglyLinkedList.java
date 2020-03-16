/**
 * 
 * @author ChiangWei
 * @date 2020/3/16
 *
 */

public class ImplementingAQueueWithASinglyLinkedList<E> {
	public static void main(String[] args) {
		ImplementingAQueueWithASinglyLinkedList<Integer> queue = new ImplementingAQueueWithASinglyLinkedList<>();
		queue.enqueue(1);
		queue.enqueue(2);
		queue.enqueue(3);
		queue.enqueue(4);
		queue.enqueue(5);
		while (!queue.isEmpty()) System.out.println(queue.dequeue());
	}
	
	private SinglyLinkedLists<E> list = new SinglyLinkedLists<>();
	
	public ImplementingAQueueWithASinglyLinkedList() {
		
	}
	
	public int size() {
		return list.size();
	}
	
	public boolean isEmpty() {
		return list.isEmpty();
	}
	
	public void enqueue(E element) {
		list.addLast(element);
	}
	
	public E first() {
		return list.first();
	}
	
	public E dequeue() {
		return list.removeFirst();
	}
}
