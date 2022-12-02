package chapter01;

import java.util.List;
import java.util.Map;
import java.util.Set;

public class CopyOf {
	public static void main(String[] args) {
		List<String> list1 = List.of("1", "2", "3");
		Set<String> set1 = Set.of("1", "2", "3");
		Map<String, String> map1 = Map.of("key1", "value1", "key2", "value2");
		
		List<String> list2 = List.copyOf(list1);
		Set<String> set2 = Set.copyOf(set1);
		Map<String, String> map2 = Map.copyOf(map1);
		
		try {
			list2.add("4");
			set2.add("4");
			map2.put("key4", "value4");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
