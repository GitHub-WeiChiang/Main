/**
 * 
 * @author ChiangWei
 * @date 2020/02/13
 *
 */

public class LazySingleton {
	private static LazySingleton uniqueInstance;
	
	private LazySingleton() {}
	
	public static LazySingleton getInstance() {
		if (uniqueInstance == null) {
			uniqueInstance = new LazySingleton();
		}
		return uniqueInstance;
	}
}
