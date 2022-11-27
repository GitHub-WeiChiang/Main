<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>JSP Page</title>
</head>
<body>
	<h1>
		Hello, 
		<%-- 取值 --%>
		<%=request.getParameter("name")%>
	</h1>
</body>
</html>