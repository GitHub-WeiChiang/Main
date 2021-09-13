package com.example.demo;

import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;
import javax.servlet.annotation.WebListener;

// 標記為監聽類別
@WebListener
public class listenerDemo implements ServletContextListener {

	@Override
    public void contextInitialized(ServletContextEvent servletContextEvent) {
		System.out.println("ServletContex 初始化");
		System.out.println(servletContextEvent.getServletContext().getServerInfo());
    }
	
	@Override
    public void contextDestroyed(ServletContextEvent servletContextEvent) {
		System.out.println("ServletContex 銷毀");
    }
	
}
