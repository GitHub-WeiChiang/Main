package course.c06;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(name = "ElAccess", urlPatterns = { "/ElAccess" })
public class ElAccess extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//test variable
		request.setAttribute("myNum", 0);
		request.setAttribute("myStr", "emp1");
		
		//Java bean
		Employee emp1 = new Employee();
		emp1.setId(1);
		emp1.setName("Jim");
		Address addr = new Address();
		addr.setLocation("Taipei");
		emp1.setAddress(addr);
		request.setAttribute("emp1", emp1);
		
		Employee emp2 = new Employee();
		emp2.setName("Bill");
				
		//Map
		Map<String, Employee> myMap = new HashMap<>();
		myMap.put("emp1", emp1);
		myMap.put("emp2", emp2);
		request.setAttribute("myMap", myMap);
		
		//List
		List<Employee> myList = new ArrayList<>();
		myList.add(emp1);
		myList.add(emp2);
		request.setAttribute("myList", myList);
		
		//Array
		Employee[] myArray = new Employee[2];
		myArray[0] = emp1;
		myArray[1] = emp2;
		request.setAttribute("myArray", myArray);
		
		RequestDispatcher rd = getServletContext().getRequestDispatcher("/course/c06/elAccess.jsp");
		rd.forward(request, response);
	}

}