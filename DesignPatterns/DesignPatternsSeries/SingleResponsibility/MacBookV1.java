// 整合
public class MacBookV1 {
	private MacLaptopProperty property;
	private MacLaptopFunction function;
    
    public static void main(String[] args) {
        System.out.println("Hello");   
    }

	public MacBookV1(MacLaptopProperty p, MacLaptopFunction f) {
		this.property = p;
		this.function = f;
	}
}

// 依據數值分類
interface LaptopProperty {
	String cpu = "";
	int size = 0;
	String resolution = "";
}

// 依據功能分類
interface LaptopFunction {
	void startUp();
	void shutDown();
}

// 實作
class MacLaptopProperty implements LaptopProperty {
	String cpu = "";
	int size = 0;
	String resolution = "";
}

// 實作
class MacLaptopFunction implements LaptopFunction {
	public void startUp() {};
	public void shutDown() {};
}
