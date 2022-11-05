package chapter17;

@FunctionalInterface
interface FuncInterface {
	public abstract void func01();
	
	// Invalid '@FunctionalInterface' annotation; FuncInterface is not a functional interface
	// public abstract void func02();
}

class FuncInteInstance implements FuncInterface {
	@Override
	public void func01() { System.out.println("func01"); }
}

public class Functional_Interface {
	public static void main(String[] args) {
		FuncInteInstance fii = new FuncInteInstance();
		fii.func01();
	}
}
