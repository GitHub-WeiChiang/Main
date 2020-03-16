/**
 * 
 * @author ChiangWei
 * @date 2020/3/16
 * @other use adapter pattern
 *
 */

public class ImplementingAStackWithASinglyLinkedList<E> {
	public static void main(String[] args) {
		ImplementingAStackWithASinglyLinkedList<Integer> stack = new ImplementingAStackWithASinglyLinkedList<>();
		System.out.println(stack.isEmpty());
		stack.push(1);
		stack.push(2);
		System.out.println(stack.size());
		System.out.println(stack.top());
		System.out.println(stack.pop());
		System.out.println(stack.pop());
		System.out.println(stack.size());
	}
	
	private SinglyLinkedLists<E> list = new SinglyLinkedLists<>();
	
	public ImplementingAStackWithASinglyLinkedList() {
		
	}
	
	public int size() {
		return list.size();
	}
	
	public boolean isEmpty() {
		return list.isEmpty();
	}
	
	public void push(E element) {
		list.addFirst(element);
	}
	
	public E top() {
		return list.first();
	}
	
	public E pop() {
		return list.removeFirst();
	}
}
