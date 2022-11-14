import java.sql.*;

public class Jdbc {

    public static String url = "jdbc:mysql://localhost:3306/db";
    public static String name = "root";
    public static String password = "!QAZ2wsx";

    public static void main(String[] args) {
        try {
            Connection con = DriverManager.getConnection(url, name, password);
            Statement stmt = con.createStatement();

            String query = "SELECT * FROM BASIC";

            ResultSet rs = stmt.executeQuery(query);

            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");

                System.out.println(id + " " + name);
            }
        } catch (SQLException e) {
            System.out.println("SQL Exception: " + e);
        }
    }
}
