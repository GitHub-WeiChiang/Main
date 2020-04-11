/**
 * 
 * @author ChiangWei
 * @date 2020/4/11
 *
 */

public class MatrixChain {
	public static int[][] matrixChain(int[] d) {
		int n = d.length - 1;
		int[][] N = new int[n][n];
		for (int b = 1; b < n; b++) {
			for (int i = 0; i < n - b; i++) {
				int j = i + b;
				N[i][j] = Integer.MAX_VALUE;
				for (int k = i; k < j; k++) {
					N[i][j] = Math.min(N[i][j], N[i][k] + N[k + 1][j] + d[i] * d[k + 1] * d[j + 1]);
				}
			}
		}
		return N;
	}
}
