package chapter11;

interface _Interface {
	// SE 7
	public abstract void method01();
	abstract void method02();
	void method03();
	
	// SE 8
	public default void method04() { System.out.println("method04"); }
	default void method05() { System.out.println("method05"); }
	
	public static void method06() { System.out.println("method06"); }
	static void method07() { System.out.println("method07"); }
	
	// SE 9
	private static void method08() { System.out.println("method08"); }
	private void method09() { System.out.println("method09"); }
	// Illegal combination of modifiers for the private interface method method10; additionally only one of static and strictfp is permitted
	// private default void method10() {};
}

class InterfaceInstance implements _Interface {
	@Override
	public void method01() { System.out.println("method01"); }
	@Override
	public void method02() { System.out.println("method02"); }
	@Override
	public void method03() { System.out.println("method03"); }
}

public class Interface {
	public static void main(String[] args) {
		_Interface ii = new InterfaceInstance();
		
		ii.method01();
		ii.method02();
		ii.method03();
		ii.method04();
		ii.method05();
		
		_Interface.method06();
		_Interface.method07();
		
		// The method method08() from the type Interface is not visible
		// ii.method08();
		
		// The method method09() from the type Interface is not visible
		// ii.method09();
	}
}
