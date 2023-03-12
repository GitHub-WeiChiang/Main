<%@ page contentType="text/html;charset=UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>JSP Page</title>
</head>
<body>
    <table border="1">
        <tr>
            <th>images</th>
        </tr>
        <tr>
            <td><img src="<c:url value='/showImage'/>"/></td>
        </tr>
        <tr>
            <td><img src="<c:url value='/images/duke.jpg'/>"/></td>
        </tr>
    </table>
</body>
</html>
