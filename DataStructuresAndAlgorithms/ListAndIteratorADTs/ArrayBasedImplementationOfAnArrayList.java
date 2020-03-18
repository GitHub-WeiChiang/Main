/**
 * 
 * @author ChiangWei
 * @date 2020/3/18
 * @other In c++ and old java, "array list" is called "vector".
 *
 */

public class ArrayBasedImplementationOfAnArrayList<E> {
	public static void main(String[] args) {
		ArrayBasedImplementationOfAnArrayList<Integer> list = new ArrayBasedImplementationOfAnArrayList<>(5);
		list.add(0, 4);
		list.add(0, 3);
		list.add(0, 2);
		list.add(0, 1);
		list.add(0, 0);
		System.out.println(list);
		list.set(3, 5);
		list.set(4, 5);
		System.out.println(list);
		list.remove(0);
		System.out.println(list);
		list.remove(3);
		System.out.println(list);
	}
	
	public static final int CAPACITY = 16;
	private E[] data;
	private int size = 0;
	
	public ArrayBasedImplementationOfAnArrayList() {
		this(CAPACITY);
	}
	
	public ArrayBasedImplementationOfAnArrayList(int capacity) {
		data = (E[])new Object[capacity];
	}
	
	public int size() {
		return size;
	}
	
	public boolean isEmpty() {
		return size == 0;
	}
	
	public E get(int i) throws IndexOutOfBoundsException {
		checkIndex(i, size);
		return data[i];
	}
	
	public E set(int i, E e) throws IndexOutOfBoundsException {
		checkIndex(i, size);
		E temp = data[i];
		data[i] = e;
		return temp;
	}
	
	public void add(int i, E e) throws IndexOutOfBoundsException, IllegalStateException {
		checkIndex(i, size + 1);
		if (size == data.length) throw new IllegalStateException("Array is full");
		for (int k = size - 1; k >= i; k--) data[k + 1] = data[k];
		data[i] = e;
		size++;
	}
	
	public E remove(int i) throws IndexOutOfBoundsException {
		checkIndex(i, size);
		E temp = data[i];
		for (int k = i; k < size - 1; k++) data[k] = data[k + 1];
		data[size - 1] = null;
		size--;
		return temp;
	}
	
	protected void checkIndex(int i, int n) throws IndexOutOfBoundsException {
		if (i < 0 || i >= n) throw new IndexOutOfBoundsException("Illegal index: " + i);
	}
	
	public String toString() {
		String str = "";
		for (int i = 0; i < data.length; i++) str += data[i] + " ";
		return str;
	}
}
