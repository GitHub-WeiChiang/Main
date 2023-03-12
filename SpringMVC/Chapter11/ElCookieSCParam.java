package course.c06;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebInitParam;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(name = "ElCookieSCParam", urlPatterns = { "/ElCookieSCParam" }, initParams = {@WebInitParam(name = "ServletInitParam", value = "this is value of ServletInitParam")})
public class ElCookieSCParam extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		response.addCookie(new Cookie("User.Cookie", "Tomcat User"));

		RequestDispatcher rd = getServletContext().getRequestDispatcher("/course/c06/elCookieSCParam.jsp");
		rd.forward(request, response);
	}
}