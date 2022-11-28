<%-- 編碼方式 --%>
<%@ page contentType="text/html;charset=UTF-8"%>
<%@ page import="java.util.*"%>
<%-- JSP 標準標記庫 (JSTL, JSP Standard Tag Library) --%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<html>
	<head>
		<title>Duke's Soccer League: Add a New League</title>
	</head>
	<body bgcolor='white'>
		<%-- 必要時自動執行 URL 重寫。 --%>
		<form action='<c:url value="/AddLeague" />' method='POST'>
			Year: <input type='text' name='year' /> <br /> <br /> 
			Season: 
			<select	name='season'>
				<option value='UNKNOWN'>select...</option>
				<option value='Spring'>Spring</option>
				<option value='Summer'>Summer</option>
				<option value='Fall'>Fall</option>
				<option value='Winter'>Winter</option>
			</select> <br /> <br /> 
			Title: <input type='text' name='title' /> <br /> <br />
			<input type='submit' value='Add League' />
		</form>
	</body>
</html>