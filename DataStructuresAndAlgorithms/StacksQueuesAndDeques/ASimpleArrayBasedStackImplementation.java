/**
 * 
 * @author ChiangWei
 * @date 2020/3/15
 *
 */

public class ASimpleArrayBasedStackImplementation<E> {
	public static void main(String[] args) {
		ASimpleArrayBasedStackImplementation<Integer> stack = new ASimpleArrayBasedStackImplementation<>();
		System.out.println(stack.isEmpty());
		stack.push(1);
		stack.push(2);
		System.out.println(stack.size());
		System.out.println(stack.top());
		System.out.println(stack.pop());
		System.out.println(stack.pop());
		System.out.println(stack.size());
	}
	
	public static final int CAPACITY = 1000;
	private E[] data;
	private int t = -1;
	
	public ASimpleArrayBasedStackImplementation() { 
		this(CAPACITY); 
	}
	
	public ASimpleArrayBasedStackImplementation(int capacity) {
		data = (E[]) new Object[capacity];
	}
	
	public int size() {
		return t + 1;
	}
	
	public boolean isEmpty() {
		return t == -1;
	}
	
	public void push(E e) throws IllegalStateException {
		if (size() == data.length) throw new IllegalStateException("Stack is full");
		data[++t] = e;
	}
	
	public E top() {
		if (isEmpty()) return null;
		return data[t];
	}
	
	public E pop() {
		if (isEmpty()) return null;
		E answer = data[t];
		data[t] = null;
		t--;
		return answer;
	}
}
