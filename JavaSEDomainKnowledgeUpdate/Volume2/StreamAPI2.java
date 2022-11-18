import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Objects;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class StreamAPI2 {
    public static void main(String[] args) {
        StreamAPI2.createStream();
        System.out.println();
        StreamAPI2.testMap();
        System.out.println();
        StreamAPI2.testPeek();
        System.out.println();
        StreamAPI2.testSorted();
        System.out.println();
        StreamAPI2.testComparing();
    }

    public static void testComparing() {
        class Point {
            int x, y;

            Point(int x, int y) {
                this.x = x;
                this.y = y;
            }

            int getX() { return x; }
            int getY() { return y; }
        }

        List<Point> pointList = Arrays.asList(
                new Point(1, 3),
                new Point(1, 1),
                new Point(1, 2)
        );

        Comparator<Point> comp = Comparator.comparing(Point::getX).thenComparing(Point::getY);

        for (Object point : pointList.stream().sorted(comp).toArray()) {
            System.out.print(((Point) point).getY());
        }
        System.out.println();
    }

    public static void testSorted() {
        List<Integer> list = Arrays.asList(3, 1, 2);
        list.stream().sorted().forEach(System.out::print);
        System.out.println();
    }

    public static void testPeek() {
        Consumer<Integer> action = System.out::println;
        Stream<Integer> stream = Stream.of(1, 2, 3).peek(action);
        Object[] arr = stream.toArray();
    }

    public static void testMap() {
        Function<Integer, Integer> mapper = n -> 2 * n;
        Stream<Integer> mapResult = Stream.of(1, 2, 3).map(mapper);
        Object[] arr = mapResult.toArray();
        List<Object> list = Arrays.asList(arr);
        System.out.println(list);
    }

    public static void createStream() {
        Stream<Integer> s1 = Stream.of(1, 2, 3);
        Stream<Integer> s2 = Arrays.stream(new Integer[] {1, 2, 3});
        IntStream s3 = Arrays.stream(new int[] {1, 2, 3});

        s1.forEach(System.out::print);
        System.out.println();
        s2.forEach(System.out::print);
        System.out.println();
        s3.forEach(System.out::print);
        System.out.println();
    }
}
