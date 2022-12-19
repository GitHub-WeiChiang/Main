// 整合
public class MacBookV2 {
	private MacbookBasicProperty basicProperty;
	private MacbookExtensionProperty extensionProperty;
	private MacbookBasicFunction basicFunction;
	private MacbookExtensionFunction extensionFunction;

    public static void main(String[] args) {
        System.out.println("Hello");
    }

	public MacBookV2(MacbookBasicProperty bp, MacbookExtensionProperty ep,  MacbookBasicFunction bf, MacbookExtensionFunction ef) {
		this.basicProperty = bp;
		this.extensionProperty = ep;
		this.basicFunction = bf;
        this.extensionFunction = ef;
	}
}

// 實作
class MacbookBasicProperty implements LaptopBasicProperty {
	String cpu = "";
	int size = 0;
}
class MacbookExtensionProperty implements LaptopExtensionProperty {
	String resolution = "";
}
class MacbookBasicFunction implements LaptopBaseFunction {
	public void startUp() {};
	public void shutDown() {};
}
class MacbookExtensionFunction implements LaptopExtentionFunction {
	public void sleep() {};
}


// 數值接口
interface LaptopBasicProperty {
	String cpu = "";
	int size = 0;
}

// 數值擴充接口
interface LaptopExtensionProperty {
	String resolution = "";
}

// 功能接口
interface LaptopBaseFunction {
	void startUp();
	void shutDown();
}

// 功能擴充接口
interface LaptopExtentionFunction {
	void sleep();
}
