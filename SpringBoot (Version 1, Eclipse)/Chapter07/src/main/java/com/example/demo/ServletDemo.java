package com.example.demo;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

// 指定作用範圍
@WebServlet(urlPatterns = "/ServletDemo/*")
public class ServletDemo extends HttpServlet{
    
	// 重寫 doGet 方法，父類 HttpServlet 的 doGet 方法是空的，沒有實現任何代碼，子類需要重寫此方法。
	// 客戶使用 GET 請求 Servlet 時，Web 容器調用 doGet 方法處理請求。
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("doGet");
        resp.getWriter().print("Servlet ServletDemo");
    }
    
}
