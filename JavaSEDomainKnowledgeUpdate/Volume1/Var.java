package chapter06;

public class Var {
	
	// 'var' is not allowed here
	// var instanceVar = 0;
	
	public static void main(String[] args) {
		var num0 = 0;
		
		// cannot convert from String to int
		// num0 = "0";
		
		// Cannot use 'var' on variable without initializer
		// var num1;
		
		// Cannot infer type for local variable initialized to 'null'
		// var obj1 = null;
		
		var var1 = new Var();
		
		// 'var' is not allowed in a compound declaration
		// var a = 0, b = 0;
		
		var1 = null;
		
		var var2 = (String) null;
		
		// Type mismatch: cannot convert from null to int
		// num0 = null;
	}
}
