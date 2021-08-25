/**
 * 
 * @author ChiangWei
 * @date 2020/2/21
 *
 */

package Sample1;

import java.util.ArrayList;

public class PancakeHouseMenuIterator implements Iterator {
	ArrayList items;
	int position = 0;
	
	public PancakeHouseMenuIterator(ArrayList items) {
		this.items = items;
	}
	
	public Object next() {
		Object menuItem = items.get(position);
		position = position + 1;
		return menuItem;
	}
	
	public boolean hasNext() {
		if (position >= items.size()) {
			return false;
		}
		else {
			return true;
		}
	}
}
