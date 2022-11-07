package chapter01;

import java.util.List;
import java.util.Map;
import java.util.Set;

public class Of {
	public static void main(String[] args) {
		List<String> list = List.of("1", "2", "3");
		Set<String> set = Set.of("1", "2", "3");
		Map<String, String> map = Map.of("key1", "value1", "key2", "value2");
		
		try {
			list.add("4");
			set.add("4");
			map.put("key4", "value4");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
