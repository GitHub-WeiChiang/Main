<%-- 頁面指令 page directive --%>
<%-- isELIgnored 為 false 代表不要忽略 EL (expression language) 語法 --%>
<%@page isELIgnored="false"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>A View Built With A JSP</title>
</head>
<body>
	<h1>Season information:</h1>
	<%-- 透過 EL 拿取 request 所帶的參數，效果如同 request.getParameter --%>
	The input of season is [${param.season}].
</body>
</html>