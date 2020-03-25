import java.util.Iterator;

/**
 * 
 * @author ChiangWei
 * @date 2020/3/23
 *
 */

public abstract class AbstractTree<E> implements Tree<E> {
	public boolean isInternal(Position<E> p) {
		return numChildren(p) > 0;
	}
	
	public boolean isExternal(Position<E> p) {
		return numChildren(p) == 0;
	}
	
	public boolean isRoot(Position<E> p) {
		return p == root();
	}
	
	public boolean isEmpty() {
		return size() == 0;
	}
	
	public int depth(Position<E> p) {
		if (isRoot(p)) return 0;
		else return 1 + depth(parent(p));
	}
	
	private int heightBad() {
		int h = 0;
		for (Position<E> p : positions()) {
			if (isExternal(p)) {
				h = Math.max(h, depth(p));
			}
		}
		return h;
	}
	
	public int height(Position<E> p) {
		int h = 0;
		for (Position<E> c : children(p)) {
			h = Math.max(h, 1 + height(c));
		}
		return h;
	}
	
	private class ElementIterator implements Iterator<E> {
		Iterator<Position<E>> posIterator = positions().iterator();
		
		public boolean hasNext() {
			return posIterator.hasNext();
		}
		
		public E next() {
			return posIterator.next().getElement();
		}
		
		public void remove() {
			posIterator.remove();
		}
	}
	
	public Iterator<E> iterator() {
		return null;
	}
	
	public Iterable<Position<E>> positions() {
		return null;
	}
}