
/**
 * 
 * @author ChiangWei
 * @date 2020/4/16
 *
 */

import java.util.Comparator;
import java.util.LinkedList;
import java.util.Queue;

public class QuickSortInPlace {
	public static void main(String[] args) {
		Comparator<Integer> comp = new Comparator<>() {
			public int compare(Integer arg0, Integer arg1) {
				return arg0.compareTo(arg1);
			}
		};
		
		Integer[] arr = new Integer[] {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
		quickSortInPlace(arr, comp, 0, arr.length - 1);
		for (Integer i : arr) {
			System.out.println(i);
		}
	}

	private static <K> void quickSortInPlace(K[] S, Comparator<K> comp, int a, int b) {
		if (a >= b) {
			return;
		}
		int left = a;
		int right = b - 1;
		K pivot = S[b];
		K temp;
		while (left <= right) {
			while (left <= right && comp.compare(S[left], pivot) < 0) {
				left++;
			}
			while (left <= right && comp.compare(S[right], pivot) > 0) {
				right--;
			}
			if (left <= right) {
				temp = S[left];
				S[left] = S[right];
				S[right] = temp;
				left++;
				right--;
			}
		}
		temp = S[left];
		S[left] = S[b];
		S[b] = temp;
		quickSortInPlace(S, comp, a, left - 1);
		quickSortInPlace(S, comp, left + 1, b);
	}
}
