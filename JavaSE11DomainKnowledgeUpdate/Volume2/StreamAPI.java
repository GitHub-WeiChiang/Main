import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Predicate;

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


public class StreamAPI {
    public static void main(String[] args) {
        List<Person> p1 = Person.createList();
        p1.forEach(Person::printPerson);

        System.out.println();

        List<Person> p2 = Person.createList();
        p2.stream().filter(
            p -> p.getAge() > 1 && p.getAge() <= 3
        ).forEach(System.out::println);

        System.out.println();

        List<Person> p3 = Person.createList();
        Predicate<Person> predicate = p -> p.getAge() > 1 && p.getAge() <= 3;
        Consumer<Person> consumer = System.out::println;
        p3.stream().filter(predicate).forEach(consumer);
    }
}
