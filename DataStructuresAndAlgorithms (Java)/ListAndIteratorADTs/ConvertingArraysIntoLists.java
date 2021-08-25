/**
 * 
 * @author ChiangWei
 * @date 2020/3/22
 *
 */

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class ConvertingArraysIntoLists {
	public static void main(String[] args) {
		Integer[] arr = {1, 2, 3, 4, 5};
		List<Integer> listArr = Arrays.asList(arr);
		for (int i: listArr) {
			System.out.println(i);
		}
		
		Collections.shuffle(listArr);
		for (int i: listArr) {
			System.out.println(i);
		}
	}
}
