/**
 * 
 * @author ChiangWei
 * @date 2020/3/19
 *
 */

import java.util.ArrayList;
import java.util.Iterator;

public class Iterators {
	public static void main(String[] args) {
		ArrayList<String> al = new ArrayList<>();
		al.add("AAA");
		al.add("BBB");
		al.add("CCC");
		
		Iterator<String> iterator = al.iterator();
		while (iterator.hasNext()) {
			String value = iterator.next();
			System.out.println(value);
		}
	}
}
