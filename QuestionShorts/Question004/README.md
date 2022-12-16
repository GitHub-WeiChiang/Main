Question004 什麼是 Java Bean
=====
* ### JavaBean 是將許多物件封裝到單個物件（bean）中的類，它具有以下特性。
    * ### 導可序列化的介面
    * ### 私有欄位
    * ### 建構函式
    * ### getter / setter
* ### 類的可序列化由實現 java.io.Serializable 介面的類啟用，未實現此介面的類將不會對其任何狀態進行序列化或反序列化。
* ### 欄位應該是私有的，以防止外部類輕易修改這些欄位，通常不直接訪問這些欄位，而是使用 getter / setter 方法。
* ### 它可能有零個或多個引數建構函式來建立一個物件。
* ### 它具有用於訪問和修改私有欄位的 getter 和 setter 方法。
```
// Implements Serializable interface
public class SimpleTesting implements Serializable {

    // private fields

    // no-args constructor

    // list of getters and setters
}
```
* ### Javabean 類範例 SimpleTesting。
```
import java.io.Serializable;

public class SimpleTesting implements Serializable {

    private int id;
    private String name;   
    private int salary;

    public SimpleTesting() {}

    public SimpleTesting(int id, String name, int salary) {
        this.id = id;
        this.name = name;
        this.salary = salary;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }  
}
```
* ### 在 Java 中如何實現 / 訪問 JavaBeans。
```
public class Main {
    public static void main(String[] args) {
        SimpleTesting st = new SimpleTesting(1, "Rohan", 100000);
        System.out.println("id = " + st.getId());
        System.out.println("name = " + st.getName());
        System.out.println("salary = " + st.getSalary());
    }
}
```
* ### Java 中 JavaBeans 的 Setter 和 Getter。
```
public class Main {

    public static void main(String[] args) {

        SimpleTesting st = new SimpleTesting();
        st.setId(1);
        st.setName("Rohan");
        st.setSalary(100000);
        System.out.println("id = " + st.getId());
        System.out.println("name = " + st.getName());
        System.out.println("salary = " + st.getSalary());
    }
}
```
* ### JavaBean 的優點: Java Bean 在整個 Java EE 中用作執行時發現和訪問的通用契約，例如，JavaServer Pages (JSP) 使用 Java Bean 作為頁面之間或 servlet 和 JSP 之間的資料傳輸物件。
<br />
