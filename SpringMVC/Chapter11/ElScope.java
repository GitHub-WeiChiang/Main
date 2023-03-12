package course.c06;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet(name = "ElScope", urlPatterns = { "/ElScope" })
public class ElScope extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		Employee emp2 = new Employee();
		emp2.setName("Bill");

		request.setAttribute("emp2", emp2);

		// test object
		Employee emp1 = new Employee();
		emp1.setId(1);
		emp1.setName("Jim");
		Address addr = new Address();
		addr.setLocation("Taipei");
		emp1.setAddress(addr);

		// test session
		HttpSession session = request.getSession();
		session.setAttribute("emp1", emp1);

		RequestDispatcher rd = getServletContext().getRequestDispatcher("/course/c06/elScope.jsp");
		rd.forward(request, response);
	}

}