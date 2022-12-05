<%@ page contentType="text/html;charset=UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<html>
<head>
<title></title>
</head>
<body>

	<h1>Show "index, count" of varStatus:</h1>
	<h2>
		<c:forEach begin="0" end="10" step="2" varStatus="status">
			${status.index},&nbsp;&nbsp;${status.count}<br/>
		</c:forEach>
	</h2>

</body>
</html>
