<%@ page contentType="text/html;charset=UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%><html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=US-ASCII">
<title>Cookie, ServletContext Param</title>
</head>
<body>
	
	<h2>cookie:</h2>
	<p>1. \${cookie} => ${cookie}</p>
	<p>2. \${cookie["User.Cookie"].value} => ${cookie["User.Cookie"].value}</p>
	
	<h2>ServletContext Param:</h2>
	<p>1. \${initParam} => ${initParam}</p>
	<p>2. \${initParam.ServletContextParam} => ${initParam.ServletContextParam}</p>
	
</body>
</html>