// 實作接口
public class BasicLaptop implements Laptop {
    String cpu = "";
    int size = 0;

    public static void main(String args[]) {
      System.out.println("Hello");
    }

    public void startUp() {};
    public void shutDown() {};
}

// 全部放在一起
interface Laptop {
    String cpu = "";
    int size = 0;
    void startUp();
    void shutDown();
}
