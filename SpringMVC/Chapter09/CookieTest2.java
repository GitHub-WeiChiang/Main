package course.c04;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/CookieTest2")
public class CookieTest2 extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		Cookie[] allCookies = request.getCookies();
		
		for (int i = 0; i < allCookies.length; i++) {
			Cookie c = allCookies[i];
			response.getWriter().append("Cookie Name: " + c.getName() + ", Cookie Value: " + c.getValue() + "</br>");
		}
		
	}

}
