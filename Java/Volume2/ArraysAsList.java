import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ArraysAsList {
    public static void main(String[] args) {
        List<String> list_1 = Arrays.asList("i1", "i1", "i1");

        try {
            list_1.set(0, "ii1");
            System.out.println(list_1);

            // 不可新增或刪除成員。
            // list_1.remove(0);
        } catch (Exception e) {
            e.printStackTrace();
        }

        List<String> list_2 = new ArrayList<>(list_1);
        list_2.remove(0);
        System.out.println(list_2);
    }
}
