/**
 * 
 * @author ChiangWei
 * @date 2020/3/11
 *
 */

import java.io.File;

public class DiskUsage {	
	public static void main(String[] args) {
		File root = new File("D:\\Videos");
		diskUsage(root);
	}
	
	public static long diskUsage(File root) {
		long total = root.length();
		if (root.isDirectory()) {
			for (String childname: root.list()) {
				File child = new File(root, childname);
				total += diskUsage(child);
			}
		}
		System.out.println(total + "\t" + root);
		return total;
	}
}
