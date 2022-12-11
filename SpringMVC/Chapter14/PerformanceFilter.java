package course.c09;

import java.io.IOException;

import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebFilter;
import javax.servlet.annotation.WebInitParam;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.DispatcherType;

@WebFilter(
		// 命名
		filterName = "perfFilter",
		// 需過濾資源型式
		urlPatterns = { "/*" },
		// 觸發時機
		dispatcherTypes = { 
			DispatcherType.FORWARD,
			DispatcherType.ERROR, 
			DispatcherType.REQUEST,
			DispatcherType.INCLUDE
		},
		// 初始參數
		initParams = { @WebInitParam(name = "Log Entry Prefix", value = "Performance:") })
// 實作 Filter 介面
public class PerformanceFilter implements Filter {

	private FilterConfig config;

	// 容器建立 Filter 時被呼叫
	public void init(FilterConfig config) throws ServletException {
		this.config = config;		
	}

	// 每一次攔截時都會執行一次
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws ServletException, IOException {
		// 記錄進入前時間
		long begin = System.currentTimeMillis();
		// 繼續下一個 Filter 或是 Servlet
		chain.doFilter(request, response);
		// 記錄離開後時間
		long end = System.currentTimeMillis();

		StringBuffer logMessage = new StringBuffer();
		if (request instanceof HttpServletRequest) {
			logMessage = ((HttpServletRequest) request).getRequestURL();
		}
		logMessage.append(": ");
		logMessage.append(end - begin);
		logMessage.append(" ms");

		String logPrefix = config.getInitParameter("Log Entry Prefix");
		if (logPrefix != null) {
			logMessage.insert(0, logPrefix);
		}		
		System.out.println(logMessage.toString());
	}

	public void destroy() {
		config = null;
	}
}
