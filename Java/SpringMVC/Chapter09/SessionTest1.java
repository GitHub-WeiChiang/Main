package course.c04;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet(name = "SessionTest1", urlPatterns = { "/SessionTest1" })
public class SessionTest1  extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String param = request.getParameter("param");
		
		HttpSession session = request.getSession();
		session.setAttribute("msg1", "Hi, this is msg1 saved in SessionTest1: " + param + "</br>");
	}
}
