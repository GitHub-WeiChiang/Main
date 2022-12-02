import java.util.ArrayList;
import java.util.stream.IntStream;

public class StreamAPI5 {
    public static void main(String[] args) {
        StreamAPI5.parallelStreamingFromCollection();
        System.out.println();
        StreamAPI5.parallelStreamingFromStream();
        System.out.println();
        StreamAPI5.testReduceInSequential();
        System.out.println();
        StreamAPI5.testReduceInParallel();
        System.out.println();
    }

    public static void testReduceInParallel() {
        int result = IntStream.rangeClosed(1, 4).parallel().reduce(0, Integer::sum);
        System.out.println(result);
    }

    public static void testReduceInSequential() {
        int result1 = IntStream.rangeClosed(1, 4).reduce(0, Integer::sum);
        System.out.println(result1);
        int result2 = IntStream.rangeClosed(1, 4).reduce(0, Integer::max);
        System.out.println(result2);
        int result3 = IntStream.rangeClosed(1, 4).reduce(0, Integer::min);
        System.out.println(result3);
    }

    public static void parallelStreamingFromStream() {
        ArrayList<Integer> al = new ArrayList<>();
        al.add(1);
        al.add(1);
        al.add(1);
        int sum = al.stream().mapToInt(i -> i).parallel().sum();
        System.out.println(sum);
    }

    public static void parallelStreamingFromCollection() {
        ArrayList<Integer> al = new ArrayList<>();
        al.add(1);
        al.add(1);
        al.add(1);
        int sum = al.parallelStream().mapToInt(i -> i).sum();
        System.out.println(sum);
    }
}
