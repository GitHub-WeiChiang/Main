import java.sql.*;

public class Jdbc {

    public static String url = "jdbc:mysql://localhost:3306/db";
    public static String name = "root";
    public static String password = "!QAZ2wsx";

    public static void main(String[] args) {
        String query = "SELECT * FROM BASIC";

        try (
                Connection con = DriverManager.getConnection(url, name, password);
                Statement stmt = con.createStatement();
                /*
                 * SELECT: executeQuery(sql) -> ResultSet
                 * INSERT, UPDATE, DELETE, ...: executeUpdate(sql) -> int
                 */
                ResultSet rs = stmt.executeQuery(query)
        ) {
            DatabaseMetaData dbm = con.getMetaData();
            System.out.println("Support for Entry-level SQL-92 standard: " + dbm.supportsANSI92EntryLevelSQL());
            System.out.println();

            Jdbc.showData(rs);
            System.out.println();
            Jdbc.showRow(rs);
            System.out.println();

            String query2 = "SELECT * FROM BASIC WHERE id = ?";
            PreparedStatement pStmt = con.prepareStatement(query2);
            pStmt.setInt(1, 2);
            ResultSet rs2 = pStmt.executeQuery();
            Jdbc.showData(rs2);
        } catch (SQLException se) {
            System.out.println("SQL State: " + se.getSQLState());
            System.out.println("Error Code in DB: " + se.getErrorCode());
            System.out.println("Message: " + se.getMessage());
        }
    }

    public static void showRow(ResultSet rs) throws SQLException {
        int num = rs.getMetaData().getColumnCount();

        for (int i = 0; i < num; i++) {
            String str1 = rs.getMetaData().getColumnName(i + 1);
            String str2 = rs.getMetaData().getColumnTypeName(i + 1);
            System.out.println(str1 + ": " + str2);
        }
    }

    public static void showData(ResultSet rs) throws SQLException {
        while (rs.next()) {
            int id = rs.getInt("id");
            String name = rs.getString("name");

            System.out.println(id + " " + name);
        }
    }
}
