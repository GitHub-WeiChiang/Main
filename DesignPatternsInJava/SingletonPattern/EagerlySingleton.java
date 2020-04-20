/**
 * 
 * @author ChiangWei
 * @date 2020/02/13
 *
 */

public class EagerlySingleton {
	private static EagerlySingleton uniqueInstance = new EagerlySingleton();
	
	private EagerlySingleton() {}
	
	public static EagerlySingleton getInstance() {
		return uniqueInstance;
	}
}
