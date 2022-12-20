package course.c03;

public class MyModel {
	private String name;
	
	public void setName(String s) {
		name = s;
	}
	
	public String getName() {
		return name;
	}

	public int getNameLength() {
		return name.length();
	}
}
