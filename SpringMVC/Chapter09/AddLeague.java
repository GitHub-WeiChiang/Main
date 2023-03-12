package course.c04;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/AddLeague")
public class AddLeague extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// 編碼方式
		response.setContentType("text/html;charset=UTF-8");
		// 瀏覽器透過 GET 送出的資料會自動將繁體中文編碼，但 POST 不會，所以需加上下方設定。
		request.setCharacterEncoding("UTF-8");
		String season = request.getParameter("season");
		String title = request.getParameter("title");
		String year = request.getParameter("year");
		response.getWriter().append("Season: " + season + ", Title: " + title + ", Year: " + year);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
