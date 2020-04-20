/**
 * 
 * @author ChiangWei
 * @date 2020/4/11
 *
 */

public class ReconstructLCS {
	public static char[] reconstructLCS(char[] X, char[] Y, int[][] L) {
		StringBuilder solution = new StringBuilder();
		int j = X.length;
		int k = Y.length;
		while (L[j][k] > 0) {
			if (X[j - 1] == Y[k - 1]) {
				solution.append(X[j - 1]);
				j--;
				k--;
			} else if (L[j - 1][k] >= L[j][k - 1]) {
				j--;
			} else {
				k--;
			}
		}
		return solution.reverse().toString().toCharArray();
	}
}
