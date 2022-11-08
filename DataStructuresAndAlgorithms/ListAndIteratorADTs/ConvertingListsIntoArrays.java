/**
 * 
 * @author ChiangWei
 * @date 2020/3/22
 *
 */

import java.util.ArrayList;

public class ConvertingListsIntoArrays {
	public static void main(String[] args) {
		ArrayList<Integer> al = new ArrayList<Integer>();
		al.add(0);
		al.add(1);
		al.add(2);
		
		Object[] object = al.toArray();
		for (Object i: object) {
			System.out.println(i);
		}
		
		Integer[] integer = new Integer[10];
		integer = al.toArray(integer);
		for (Integer i: integer) {
			System.out.println(i);
		}
	}
}
