/**
 * 
 * @author ChiangWei
 * @date 2020/4/7
 *
 */

public class FindBrute {
	public static void main(String[] args) {
		System.out.println(FindBrute.findBrute(new String("ABABABAB").toCharArray(), new String("ABABABAB").toCharArray()));
		System.out.println(FindBrute.findBrute(new String("ABABABCB").toCharArray(), new String("CB").toCharArray()));
		System.out.println(FindBrute.findBrute(new String("ABABABAB").toCharArray(), new String("AD").toCharArray()));
	}
	
	public static int findBrute(char[] text, char[] pattern) {
		int n = text.length;
		int m = pattern.length;
		for (int i = 0; i <= n - m; i++) {
			int k = 0;
			while (k < m && text[i + k] == pattern[k]) k++;
			if (k == m) return i;
		}
		return -1;
	}
}
