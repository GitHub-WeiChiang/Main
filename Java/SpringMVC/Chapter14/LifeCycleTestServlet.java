package course.c09;

import java.io.IOException;
import java.io.PrintWriter;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


public class LifeCycleTestServlet extends HttpServlet {

	private static final long serialVersionUID = 1L;
	
	@PostConstruct
	void myInit() {
		System.out.println("myInit() is called by container");
	}
	
	String myParam;
	@Override
	public void init() throws ServletException {
		this.myParam = super.getServletConfig().getInitParameter("myParam");
	//	this.myParam = super.getInitParameter("myParam");
		System.out.println("init() hooks!");
	}

	@Override
    public void destroy() {
		System.out.println("destroy() is called by container");
    }
	
	@PreDestroy
    public void myDestroy() {
    	System.out.println("myDestroy() is called by container");
    }

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=UTF-8");
		PrintWriter out = response.getWriter();
		try {
			out.println("<h1>myParam = " + myParam + "</h1>");
		} finally {
			out.close();
		}
	}
}