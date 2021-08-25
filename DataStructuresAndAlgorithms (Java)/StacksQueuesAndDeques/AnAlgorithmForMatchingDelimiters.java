/**
 * 
 * @author ChiangWei
 * @date 2020/3/16
 *
 */

import java.util.Stack;

public class AnAlgorithmForMatchingDelimiters {
	public static void main(String[] args) {
		System.out.println(isMatched("1 - {[(1 + 2) * (5 + 1)] + 1 * 2}"));
		System.out.println(isMatched("1 - {[(1 + 2) * (5 + 1] + 1 * 2}"));
	}
	
	public static boolean isMatched(String expression) {
		final String opening = "({[";
		final String closing = ")}]";
		Stack<Character> buffer = new Stack<>();
		for (char c: expression.toCharArray()) {
			if (opening.indexOf(c) != -1) {
				buffer.push(c);
			}
			else if (closing.indexOf(c) != -1) {
				if (buffer.isEmpty()) return false;
				if (closing.indexOf(c) != opening.indexOf(buffer.pop())) return false;
			}
		}
		return buffer.isEmpty();
	}
}
