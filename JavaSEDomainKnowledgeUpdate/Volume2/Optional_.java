import java.util.Optional;

public class Optional_ {
    public static void main(String[] args) {
        Optional<Double> o1 = Optional_.average();
        System.out.println(o1.isPresent());

        Optional<Double> o2 = Optional_.average(1, 2, 3);

        o2.ifPresent(System.out::println);

        if (o2.isPresent()) {
            double average = o2.get();
            System.out.println(average);
        }
    }

    public static Optional<Double> average(int... num) {
        if (num.length == 0) return Optional.empty();

        int sum = 0;

        for (int i : num) {
            sum += i;
        }

        return Optional.of((double) sum / num.length);
    }
}
