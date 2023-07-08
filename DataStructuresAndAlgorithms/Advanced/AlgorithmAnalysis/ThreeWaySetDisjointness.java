/**
 * 
 * @author ChiangWei
 * @date 2020/3/10
 *
 */

public class ThreeWaySetDisjointness {
	public static boolean disjoint1(int[] groupA, int[] groupB, int[] groupC) {
		for (int a: groupA) {
			for (int b: groupB) {
				for (int c: groupC) {
					if (a == b && b == c) return false;
				}
			}
		}
		return true;
	}
	
	public static boolean disjoint2(int[] groupA, int[] groupB, int[] groupC) {
		for (int a: groupA) {
			for (int b: groupB) {
				if (a == b) {
					for (int c: groupC) {
						if (a == c) return false;
					}
				}
			}
		}
		return true;
	}
}
