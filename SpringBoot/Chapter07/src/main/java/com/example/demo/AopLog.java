package com.example.demo;

import javax.servlet.http.HttpServletRequest;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.AfterThrowing;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;

// 標記為剖面類別
@Aspect
// 加到 IOC 容器
@Component
public class AopLog {
	
	private Logger logger = LoggerFactory.getLogger(this.getClass());
	
	// 執行緒局部變數，用於解決多執行緒相同變數的存取衝突問題
	ThreadLocal<Long> startTime = new ThreadLocal<>();
	
	// 定義切入點
	// @Pointcut("execution(public * com.example..*.*(..))")
	@Pointcut("execution(public * com.example.demo.AopLogController.*(..))")
    public void aopWebLog() {}
	
	// 在切入點開始處切入內容
	@Before("aopWebLog()")
    public void doBefore(JoinPoint joinPoint) throws Throwable {
        startTime.set(System.currentTimeMillis());
        // 接收到请求，记录请求内容
        ServletRequestAttributes attributes = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();
        HttpServletRequest request = attributes.getRequest();

        // 记录下请求内容
        logger.info("URL: " + request.getRequestURL().toString());
        logger.info("HTTP 方法: " + request.getMethod());
        logger.info("IP 地址: " + request.getRemoteAddr());
        logger.info("類別方法: " + joinPoint.getSignature().getDeclaringTypeName() + "." + joinPoint.getSignature().getName());
        logger.info("参数: " + request.getQueryString());
    }
	
	// 在切入點傳回 return 內容後切入內容，對傳回值做加工處理
    @AfterReturning(pointcut = "aopWebLog()",returning = "retObject")
    public void doAfterReturning(Object retObject) throws Throwable {
        // 处理完请求，返回内容
        logger.info("應答值: " + retObject);
        logger.info("費時: " + (System.currentTimeMillis() - startTime.get()));
    }
	
    //抛出异常后通知(After throwing advice): 在方法抛出异常退出时执行的通知。
    @AfterThrowing(pointcut = "aopWebLog()", throwing = "ex")
    public void addAfterThrowingLogger(JoinPoint joinPoint, Exception ex) {
        logger.error("執行 " + " 異常", ex);
    }
    
}
