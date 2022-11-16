import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;

class Person {
    private String name, email;
    private int age;

    public Person() {}

    public Person(String name, String email, int age) {
        this.name = name;
        this.age = age;
        this.email = email;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public String getEmail() {
        return email;
    }

    @Override
    public String toString() {
        return "Name = " + name + ", Age = " + age + ", email = " + email;
    }

    public void printPerson() {
        System.out.println(this);
    }

    public static List<Person> createList() {
        List<Person> people = new ArrayList<>();

        people.add(new Person("Java", "Java@gmail.com", 1));
        people.add(new Person("Python", "Python@gmail.com", 2));

        return people;
    }
}

public class Lambda {
    public static void main(String[] args) {
        Predicate<Person> predicate = p -> p.getAge() != 0;
        for (Person p : Person.createList()) {
            if (predicate.test(p)) {
                System.out.println(p);
            }
        }

        System.out.println();

        Consumer<Person> consumer = Person::printPerson;
        for (Person p : Person.createList()) {
            consumer.accept(p);
        }

        System.out.println();

        Function<Person, String> function = Person::getName;
        for (Person p : Person.createList()) {
            System.out.println(function.apply(p));
        }

        System.out.println();

        Supplier<Person> supplier = () -> new Person("Julia", "Julia@gmail.com", 3);
        System.out.println(supplier.get());
    }
}
