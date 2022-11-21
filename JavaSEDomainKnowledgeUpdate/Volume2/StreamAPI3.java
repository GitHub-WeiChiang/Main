import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class StreamAPI3 {
    static class Person {
        private final int age;
        public Person(int age) { this.age = age; }
        public int getAge() { return age; }
    }

    public static void main(String[] args) {
        StreamAPI3.testCount();
        System.out.println();
        StreamAPI3.testMaxMin();
        System.out.println();
        StreamAPI3.testAverage();
        System.out.println();
        StreamAPI3.testToListToSet();
        System.out.println();
        StreamAPI3.testToMap();
        System.out.println();
        StreamAPI3.testAveragingDouble();
        System.out.println();
        StreamAPI3.testJoining();
        System.out.println();
        StreamAPI3.testGroupingBy();
        System.out.println();
        StreamAPI3.testPartitioningBy();
        System.out.println();
        StreamAPI3.testFiltering();
    }

    public static void testFiltering() {
        Stream<Person> stream1 = Arrays.stream(
                new Person[] {new Person(1), new Person(1), new Person(2)}
        );

        Stream<Person> stream2 = Arrays.stream(
                new Person[] {new Person(1), new Person(1), new Person(2)}
        );

        List<Person> filter1 = stream1.filter(p -> p.age > 1).collect(Collectors.toList());
        System.out.println(filter1);

        List<Person> filter2 = stream2.collect(Collectors.filtering(p -> p.age > 1, Collectors.toList()));
        System.out.println(filter2);
    }

    public static void testPartitioningBy() {
        Map<Boolean, List<Person>> personsByAge = Arrays.stream(
                new Person[] {new Person(1), new Person(1), new Person(2)}
        ).collect(Collectors.partitioningBy(s -> s.getAge() > 1));

        personsByAge.forEach((k, v) -> System.out.println(k + ": " + v));
    }

    public static void testGroupingBy() {
        Function<Person, Integer> classifier = Person::getAge;

        Map<Integer, List<Person>> personsByAge = Arrays.stream(
            new Person[] {new Person(1), new Person(1), new Person(2)}
        ).collect(Collectors.groupingBy(classifier));

        personsByAge.forEach((age, list) -> System.out.println(age + ": " + list));
    }

    public static void testJoining() {
        List<String> list = Arrays.asList("a", "b", "c");
        // String str = list.stream().collect(Collectors.joining("-"));
        String str = String.join("-", list);
        System.out.println(str);
    }

    public static void testAveragingDouble() {
        Double average = Arrays.stream(new Integer[] {1, 2, 3, 4}).collect(Collectors.averagingDouble(i -> i));
        System.out.println(average);
    }

    public static void testToMap() {
        class Point {
            int x, y;

            Point(int x, int y) {
                this.x = x;
                this.y = y;
            }

            int getX() { return x; }
            int getY() { return y; }
        }

        Point[] points = new Point[] {new Point(1, 1), new Point(2, 2)};
        Map<Integer, Integer> map = Arrays.stream(points).collect(Collectors.toMap(Point::getX, Point::getY));
        System.out.println(map);
    }

    public static void testToListToSet() {
        String[] sArr = new String[] {"111 ", "222 ", "111 "};

        Stream<String> s1 = Stream.of(sArr);
        Set<String> set = s1.collect(Collectors.toSet());
        set.forEach(System.out::print);
        System.out.println();

        Stream<String> s2 = Stream.of(sArr);
        List<String> list = s2.collect(Collectors.toList());
        list.forEach(System.out::print);
        System.out.println();
    }

    public static void testAverage() {
        OptionalDouble od = Stream.of(1, 2, 3).mapToInt(i -> i).average();
        System.out.println(od);
        System.out.println(od.isPresent() ? od.getAsDouble() : -1);

        int sum = Stream.of(1, 2, 3).mapToInt(i -> i).sum();
        System.out.println(sum);
    }

    public static void testMaxMin() {
        Comparator<String> comparator = String::compareTo;

        Optional<String> os = Stream.of("x", "y").max(comparator);
        System.out.println(os);

        List<String> list = new ArrayList<String>();
        Optional<String> empty = list.stream().max(comparator);
        System.out.println(empty);

        OptionalInt oi = Stream.of(1, 2, 3).mapToInt(i -> i).min();
        System.out.println(oi);
    }

    public static void testCount() {
        long cnt = Stream.of("Hello", "World").count();
        System.out.println(cnt);
    }
}
