<%@ page contentType="text/html;charset=UTF-8"%>
<%@ page import="java.util.*"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<html>
	<head>
		<title>JSP EL Scope</title>
	</head>
	<body>
	
		<%
			List<String> names = new ArrayList<String>();
			names.add("Jim1");
			names.add("Jim2");
			pageContext.setAttribute("names", names);
			pageContext.setAttribute("str", "Hi,Jim", PageContext.REQUEST_SCOPE);
		%>
	
		<h2>pageContext:</h2>
		<p>1. \${pageContext.request.method} => ${pageContext.request.method}</p>
		<p>2. \${pageContext.request.contextPath} => ${pageContext.request.contextPath}</p>
		<p>3. \${pageContext.out.bufferSize} => ${pageContext.out.bufferSize} </p>
	
		<h2>pageScope:</h2>
		<p>1. \${pageScope.names[0]} => ${pageScope.names[0]}</p>
		<p>2. \${names[1]} => ${names[1]}</p>
	
		<h2>requestScope:</h2>
		<p>1. \${requestScope.emp2} => ${requestScope.emp2}</p>
	
		<h2>sessionScope:</h2>
		<p>1. \${sessionScope.emp1.address.location} => ${sessionScope.emp1.address.location}</p>
		<p>2. \${sessionScope["emp1"].address["location"]} => ${sessionScope["emp1"].address["location"]}</p>
	
	</body>
</html>