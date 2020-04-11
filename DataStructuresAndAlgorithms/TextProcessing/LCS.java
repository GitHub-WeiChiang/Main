/**
 * 
 * @author ChiangWei
 * @date 2020/4/11
 *
 */

public class LCS {
	public static int[][] lcs(char[] X, char[] Y) {
		int n = X.length;
		int m = Y.length;
		int[][] L = new int[n + 1][m + 1];
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < m; k++) {
				if (X[j] == Y[k]) {
					L[j + 1][k + 1] = L[j][k] + 1;
				} else {
					L[j + 1][k + 1] = Math.max(L[j][k + 1], L[j + 1][k]);
				}
			}
		}
		return L;
	}
}
