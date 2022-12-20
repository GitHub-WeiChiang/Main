package course.c01;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

// 讓容器知道這是一個 Servlet。
// 透過 urlPatterns 建立 URL 對應關係。
//Servlet 必須繼承 HttpServlet。
@WebServlet(name = "HelloServlet", urlPatterns = { "/HelloServlet", "/HelloServlet2" })
public class HelloServlet extends HttpServlet {

	private static final long serialVersionUID = 1L;

	// GEY 請求會調用 doGet method。
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=UTF-8");
		PrintWriter out = response.getWriter();
		System.out.println();
		try {
			out.println("<html>");
			out.println("<head>");
			out.println("<title>HelloServlet</title>");
			out.println("</head>");
			out.println("<body>");
			out.println("<h1>HelloServlet says \"Hello, World!\"</h1>");
			out.println("</body>");
			out.println("</html>");
		} finally {
			out.close();
		}
	}
}
