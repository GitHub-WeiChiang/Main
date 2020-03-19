/**
 * 
 * @author ChiangWei
 * @date 2020/3/19
 *
 */

import java.util.ArrayList;
import java.util.Iterator;

public class TheIterableInterfaceAndJavasForEachLoop {
	public static void main(String[] args) {
		ArrayList<String> al1 = new ArrayList<>();
		al1.add("AAA");
		al1.add("BBB");
		al1.add("CCC");
		for (String str: al1) System.out.println(str);
		
		System.out.println();
		
		ArrayList<String> al2 = new ArrayList<>();
		al2.add("AAA");
		al2.add("BBB");
		al2.add("CCC");
		Iterator<String> iterator = al2.iterator();
		while(iterator.hasNext()) {
			if (iterator.next() == "AAA") iterator.remove();
		}
		for (String str: al2) System.out.println(str);
	}
}
