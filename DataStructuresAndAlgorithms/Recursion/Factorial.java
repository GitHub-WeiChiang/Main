/**
 * 
 * @author ChiangWei
 * @date 2020/3/10
 *
 */

public class Factorial {
	public static void main(String[] agrs) {
		System.out.println(factorial(5));
	}
	
	public static int factorial(int n) throws IllegalArgumentException {
		if (n < 0) throw new IllegalArgumentException();
		else if (n == 0) return 1;
		else return n * factorial(n - 1);
	}
}
