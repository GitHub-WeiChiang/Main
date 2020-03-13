/**
 * 
 * @author ChiangWei
 * @date 2020/3/13
 *
 */

public class PitfallsOfRecursion {
	public static void main(String[] args) {
		int[] data;
		data = new int[] {0, 1, 2, 3, 4, 5};
		System.out.println(uniqueBad(data, 0, data.length - 1));
		data = new int[] {0, 1, 2, 3, 4, 4};
		System.out.println(uniqueBad(data, 0, data.length - 1));
		
		System.out.println(fibonacciBad(4));
		System.out.println(fibonacciGood(4)[0]);
	}
	
	public static boolean uniqueBad(int[] data, int low, int high) {
		if (low >= high) return true;
		else if (!uniqueBad(data, low, high - 1)) return false;
		else if (!uniqueBad(data, low + 1, high)) return false;
		else return data[low] != data[high];
	}
	
	public static long fibonacciBad(int n) {
		if (n <= 1) return n;
		else return fibonacciBad(n - 2) + fibonacciBad(n - 1);
	}
	
	public static long[] fibonacciGood(int n) {
		if (n <= 1) {
			long[] answer = {n, 0};
			return answer;
		}
		else {
			long[] temp = fibonacciGood(n - 1);
			long[] answer = {temp[0] + temp[1], temp[0]};
			return answer;
		}
	}
}
