
/**
 * 
 * @author ChiangWei
 * @date 2020/4/5
 *
 */

import java.util.Scanner;

public class WordCount {
	public static void main(String[] args) {
		Map<String, Integer> freq = new ChainHashMap<>();
		Scanner doc = new Scanner(System.in).useDelimiter("[^a-zA-Z]+");
		while (doc.hasNext()) {
			String word = doc.next().toLowerCase();
			if (word.equals("exit")) break;
			Integer count = freq.get(word);
			if (count == null) {
				count = 0;
			}
			freq.put(word, 1 + count);
		}
		int maxCount = 0;
		String maxWord = "no word";
		for (Entry<String, Integer> ent : freq.entrySet()) {
			if (ent.getValue() > maxCount) {
				maxWord = ent.getKey();
				maxCount = ent.getValue();
			}
		}
		System.out.print("The most frequent word is '" + maxWord);
		System.out.println("' with " + maxCount + " occurrences.");
	}
}
