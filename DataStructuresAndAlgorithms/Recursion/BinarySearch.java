/**
 * 
 * @author ChiangWei
 * @date 2020/3/11
 *
 */

public class BinarySearch {
	public static void main(String[] args) {
		int[] arr = new int[] {1, 2, 3, 4, 5};
		System.out.println(binarySearch(arr, 4, 0, arr.length));
	}
	
	public static boolean binarySearch(int[] data, int target, int low, int high) {
		if (low > high) return false;
		else {
			int mid = (low + high) / 2;
			if (target == data[mid]) return true;
			else if (target < data[mid]) return binarySearch(data, target, low, mid - 1);
			else return binarySearch(data, target, mid + 1, high);
		}
	}
}
