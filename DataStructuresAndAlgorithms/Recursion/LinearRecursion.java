/**
 * 
 * @author ChiangWei
 * @date 2020/3/12
 *
 */

public class LinearRecursion {
	public static void main(String[] args) {
		int[] arr = new int[] {1, 2, 3, 4, 5};
		System.out.println(linearSum(arr , arr.length));
		
		reverseArray(arr, 0, arr.length - 1);
		for (int i = 0; i < arr.length; i++) System.out.print(arr[i]);
		System.out.println();
		
		System.out.println(power1(2, 4));
		System.out.println(power2(2, 4));
	}
	
	public static int linearSum(int[] data, int n) {
		if (n == 0) return 0;
		else return linearSum(data, n - 1) + data[n - 1];
	}
	
	public static void reverseArray(int[] data, int low, int high) {
		if (low < high) {
			data[low] ^= data[high];
			data[high] ^= data[low];
			data[low] ^= data[high];
			reverseArray(data, low + 1, high - 1);
		}
	}
	
	public static double power1(double x, int n) {
		if (n == 0) return 1;
		else return x * power1(x , n - 1);
	}
	
	public static double power2(double x, int n) {
		if (n == 0) return 1;
		else {
			double partial = power2(x, n / 2);
			double result = partial * partial;
			if (n % 2 == 1) return result *= x;
			return result;
		}
	}
}
