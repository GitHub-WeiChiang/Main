import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.stream.Stream;

public class StreamAPI4 {
    public static void main(String[] args) {
        StreamAPI4.testAllMatch();
        System.out.println();
        StreamAPI4.testNoneMatch();
        System.out.println();
        StreamAPI4.testAnyMatch();
        System.out.println();
        StreamAPI4.testFindFirst();
        System.out.println();
        StreamAPI4.testFindAny();
        System.out.println();
    }

    public static void testFindAny() {
        List<String> list = Arrays.asList("111", "222", "333");
        Optional<String> val = list.stream().findAny();
        System.out.println(val);
    }

    public static void testFindFirst() {
        Optional<String> val = Stream.of("one", "two").findFirst();
        System.out.println(val);
    }

    public static void testAnyMatch() {
        List<String> list = Arrays.asList("111", "112", "223");
        boolean judge = list.stream().anyMatch(p -> p.contains("2"));
        System.out.println(judge);
    }

    public static void testNoneMatch() {
        List<String> list = Arrays.asList("111", "112", "223");
        boolean judge = list.stream().noneMatch(p -> p.contains("5"));
        System.out.println(judge);
    }

    public static void testAllMatch() {
        List<String> list = Arrays.asList("111", "112", "223");
        boolean judge = list.stream().allMatch(p -> p.contains("1"));
        System.out.println(judge);
    }
}
