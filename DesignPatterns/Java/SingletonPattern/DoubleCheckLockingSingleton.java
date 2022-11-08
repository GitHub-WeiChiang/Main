/**
 * 
 * @author ChiangWei
 * @date 2020/02/13
 *
 */

public class DoubleCheckLockingSingleton {
	private volatile static DoubleCheckLockingSingleton uniqueInstance;
	
	private DoubleCheckLockingSingleton() {}
	
	public static DoubleCheckLockingSingleton getInstance() {
		if (uniqueInstance == null) {
			synchronized (DoubleCheckLockingSingleton.class) {
				if (uniqueInstance == null) {
					uniqueInstance = new DoubleCheckLockingSingleton();
				}
			}
		}
		return uniqueInstance;
	}
}
