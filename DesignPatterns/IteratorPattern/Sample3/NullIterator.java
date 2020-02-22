/**
 * 
 * @author ChiangWei
 * @date 2020¦~2¤ë22¤é
 *
 */

package Sample3;

import java.util.Iterator;

public class NullIterator implements Iterator {
	public Object next() {
		return null;
	}

	public boolean hasNext() {
		return false;
	}

	public void remove() {
		throw new UnsupportedOperationException();
	}
}
