<%-- 註解 comment --%>
<%-- Simple Hello World JSP example --%>

<%-- 頁面指令 page directive --%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>JSP Page</title>
	</head>
	<body>
		<%-- Java 運算式 --%>
		<h1><%="Hello World! This's a JSP, it is " + new java.util.Date()%></h1>
	</body>
</html>