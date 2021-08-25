/**
 * 
 * @author ChiangWei
 * @date 2020/3/4
 *
 */

public class CircularlyLinkedLists<E> {
	private static class Node<E> {
		private E element;
		private Node<E> next;
		public Node(E e, Node<E> n) {
			element = e;
			next = n;
		}
		public E getElement() { return element; }
		public Node<E> getNext() { return next; }
		public void setNext(Node<E> n) { next = n; }
	}
	
	private Node<E> tail = null;
	private int size = 0;
	public CircularlyLinkedLists() {}
	
	public int size() {
		return size;
	}
	
	public boolean isEmpty() {
		return size == 0;
	}
	
	public E first() {
		if (isEmpty()) return null;
		return tail.getNext().getElement();
	}
	
	public E last() {
		if (isEmpty()) return null;
		return tail.getElement();
	}
	
	public void rotate() {
		if (tail != null) {
			tail = tail.getNext();
		}
	}
	
	public void addFirst(E e) {
		if (size == 0) {
			tail = new Node<>(e, null);
			tail.setNext(tail);
		}
		else {
			Node<E> newest = new Node<>(e, tail.getNext());
			tail.setNext(newest);
		}
		size++;
	}
	
	public void addLast(E e) {
		addFirst(e);
		tail = tail.getNext();
	}
	
	public E removeFirst() {
		if (isEmpty()) return null;
		Node<E> head = tail.getNext();
		if (head == tail) tail = null;
		else tail.setNext(head.getNext());
		size--;
		return head.getElement();
	}
	
	public String toString() {
		String str = "";
		Node<E> temp = tail.getNext();
		for (int i = 0; i < size; i++) {
			str += temp.getElement();
			temp = temp.getNext();
		}
		return str;
	}
	
	public static void main(String[] args) {
		CircularlyLinkedLists<Character> circularlyLinkedLists = new CircularlyLinkedLists<>();
		for (int i = 0; i < 5; i++) circularlyLinkedLists.addLast((char)('A' + i));
		System.out.println(circularlyLinkedLists);
		circularlyLinkedLists.removeFirst();
		circularlyLinkedLists.removeFirst();
		circularlyLinkedLists.removeFirst();
		System.out.println(circularlyLinkedLists);
		circularlyLinkedLists.addFirst('Z');
		System.out.println(circularlyLinkedLists);
	}
}
