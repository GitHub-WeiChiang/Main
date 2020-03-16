/**
 * 
 * @author ChiangWei
 * @date 2020/3/16
 * @other using an array circularly
 *
 */

public class ArrayBasedQueueImplementation<E> {
	public static void main(String[] args) {
		ArrayBasedQueueImplementation<Integer> queue = new ArrayBasedQueueImplementation<>();
		queue.enqueue(1);
		queue.enqueue(2);
		queue.enqueue(3);
		queue.enqueue(4);
		queue.enqueue(5);
		while (!queue.isEmpty()) System.out.println(queue.dequeue());
	}
	
	public static final int CAPACITY = 1000;
	private E[] data;
	private int f = 0;
	private int sz = 0;
	
	public ArrayBasedQueueImplementation() {
		this(CAPACITY);
	}
	
	public ArrayBasedQueueImplementation(int capacity) {
		data = (E[]) new Object[capacity];
	}
	
	public int size() {
		return sz;
	}
	
	public boolean isEmpty() {
		return sz == 0;
	}
	
	public void enqueue(E e) throws IllegalStateException {
		if (sz == data.length) throw new IllegalStateException("Queue is full");
		int avail = (f + sz) % data.length;
		data[avail] = e;
		sz++;
	}
	
	public E first() {
		if (isEmpty()) return null;
		return data[f];
	}
	
	public E dequeue() {
		if (isEmpty()) return null;
		E answer = data[f];
		data[f] = null;
		f = (f + 1) % data.length;
		sz--;
		return answer;
	}
}
