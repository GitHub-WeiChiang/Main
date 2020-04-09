/**
 * 
 * @author ChiangWei
 * @date 2020/4/7
 *
 */

import java.util.HashMap;
import java.util.Map;

public class FindBoyerMoore {
	public static void main(String[] args) {
		System.out.println(FindBoyerMoore.findBoyerMoore(new String("ABABABAB").toCharArray(), new String("ABABABAB").toCharArray()));
		System.out.println(FindBoyerMoore.findBoyerMoore(new String("ABABABCB").toCharArray(), new String("CB").toCharArray()));
		System.out.println(FindBoyerMoore.findBoyerMoore(new String("ABABABAB").toCharArray(), new String("AD").toCharArray()));
	}

	public static int findBoyerMoore(char[] text, char[] pattern) {
		int n = text.length;
		int m = pattern.length;
		if (m == 0) {
			return 0;
		}
		Map<Character, Integer> last = new HashMap<>();
		for (int i = 0; i < n; i++) {
			last.put(text[i], -1);
		}
		for (int k = 0; k < m; k++) {
			last.put(pattern[k], k);
		}
		int i = m - 1;
		int k = m - 1;
		while (i < n) {
			if (text[i] == pattern[k]) {
				if (k == 0)
					return i;
				i--;
				k--;
			} else {
				i += m - Math.min(k, 1 + last.get(text[i]));
				k = m - 1;
			}
		}
		return -1;
	}
}
