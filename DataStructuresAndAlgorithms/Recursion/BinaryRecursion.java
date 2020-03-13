/**
 * 
 * @author ChiangWei
 * @date 2020/3/13
 *
 */

public class BinaryRecursion {
	public static void main(String[] args) {
		int[] data = new int[] {1, 2, 3, 4, 5};
		System.out.println(binarySum(data, 0, data.length - 1));
	}
	
	public static int binarySum(int[] data, int low, int high) {
		if (low > high) return 0;
		else if (low == high) return data[low];
		else {
			int mid = (low + high) / 2;
			return binarySum(data, low, mid) + binarySum(data, mid + 1, high);
		}
	}
}
