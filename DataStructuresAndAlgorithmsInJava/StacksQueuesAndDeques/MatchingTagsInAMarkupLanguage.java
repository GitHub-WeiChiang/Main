/**
 * 
 * @author ChiangWei
 * @date 2020/3/16
 *
 */

import java.util.Stack;

public class MatchingTagsInAMarkupLanguage {
	public static void main(String[] args) {
		System.out.println(isHTMLMatched("<body><center><h1>TheLittleBoat</h1></center></body>"));
		System.out.println(isHTMLMatched("<body><center><h1>TheLittleBoat</center></body>"));
	}
	
	public static boolean isHTMLMatched(String html) {
		Stack<String> buffer = new Stack<>();
		int i = html.indexOf('<');
		while (i != -1) {
			int j = html.indexOf('>', i + 1);
			if (j == -1) return false;
			String tag = html.substring(i + 1, j);
			if (!tag.startsWith("/")) buffer.push(tag);
			else {
				if (buffer.isEmpty()) return false;
				if (!tag.substring(1).equals(buffer.pop())) return false;
			}
			i = html.indexOf('<', j + 1);
		}
		return buffer.isEmpty();
	}
}
