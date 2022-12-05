<%@page contentType="text/html;charset=UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<html>
	<head>
		<title></title>
	</head>
	<body>
		<form action='jstlIfFor1.jsp'>
			<table>
				<tr>
					<td>選擇程式語言:</td>
					<td><select name='languages' size='6' multiple>
							<option value='Ada'>Ada</option>
							<option value='C'>C</option>
							<option value='C++'>C++</option>
							<option value='Cobol'>Cobol</option>
							<option value='Objective-C'>Objective-C</option>
							<option value='Java'>Java</option>
					</select></td>
				</tr>
			</table>
			<p>
				<input type='submit' value='Finish Survey' />
		</form>
	
		<font color="red"> 
			<c:if test="${not empty param.languages}" var="langSelected" scope="session">
				Selected languages were:<br/>
				${param.languages}<br/>
			</c:if> 
			<c:if test="${empty param.languages}">
				No language was selected!!
			</c:if>
		</font>
	
		<br/>
		<br/>
		<p>Go to <a href="jstlIfFor2.jsp">jstlIfFor2.jsp</a></p>
	</body>
</html>
