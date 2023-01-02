package com.example.demo;

import java.io.IOException;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebFilter;

import org.springframework.core.annotation.Order;

// 多 filter 的時，序號小先執行
@Order(1)
// 作用範圍
@WebFilter(urlPatterns = "/*")
public class FilterDemo implements Filter {
	@Override
	public void init(FilterConfig filterConfig) throws ServletException {
		// init 邏輯，在服務器啟動時調用
	}
	
	@Override
	public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
		// request 相關處理
        // chain 重新寫回 request 和 response
		
		System.out.println("攔截器");
		filterChain.doFilter(servletRequest, servletResponse);
	}
	
	@Override
	public void destroy() {
	
	}
}
