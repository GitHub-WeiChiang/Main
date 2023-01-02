package course.c03;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(name = "MyController", urlPatterns = { "/MyController" })
public class MyController extends HttpServlet {
	private static final long serialVersionUID = 1L;

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String name = request.getParameter("name");
		
		if (name == null) {
			name = "Secret";
		}
		
		MyModel model = new MyModel();
		model.setName(name);
		
		request.setAttribute("model", model);
				
		RequestDispatcher rd = request.getRequestDispatcher("/course/c03/myView.jsp");
		rd.forward(request, response);
		
	}
}