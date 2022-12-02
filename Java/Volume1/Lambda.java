package chapter17;

@FunctionalInterface
interface Double {
	public abstract int func(int a, int b);
}

@FunctionalInterface
interface Single {
	public abstract int func(int a);
}

@FunctionalInterface
interface Generic<T>{
	public abstract void func(T t);
}

@FunctionalInterface
interface Void {
	public abstract void func(int a);
}

public class Lambda {
	public static void main(String[] args) {
		Double li1 = (int a, int b) -> a + b;
		System.out.println(li1.func(1, 1));
		
		Double li2 = (a, b) -> a + b;
		System.out.println(li2.func(1, 1));
		
		// Syntax error on token "->", = expected
		// Double li3 = a, b -> a + b;
		
		Single li4 = a -> a * 2;
		System.out.println(li4.func(1));
		
		Single li5 = a -> {
			a++;
			a++;
			return a;
		};
		System.out.println(li5.func(0));
		
		// Void methods cannot return a value
		// Void li6 = a -> a == 0;
		
		Void li7 = a -> System.out.println(a);
		li7.func(2);
		
		Lambda.generic(Integer.valueOf("2"), a -> System.out.println(a));
		Lambda.generic(Float.valueOf("2"), a -> System.out.println(a));
		Lambda.generic(String.valueOf(2), a -> System.out.println(a));
	}
	
	public static void generic(Object obj, Generic<Object> g) {
		g.func(obj);
	}
}
