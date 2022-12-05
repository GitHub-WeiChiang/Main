<%@page contentType="text/html;charset=UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<html>
<head>
<title>param, paramValues, header, headerValues</title>
</head>
<body>

	<h2>header:</h2>
	<p>1. \${header["cookie"]} => ${header["cookie"]}</p>
	
	<h2>headerValues:</h2>
	<p>1. \${headerValues["cookie"]} => ${headerValues["cookie"]}</p>
	<p>2. \${headerValues["cookie"][0]} => ${headerValues["cookie"][0]}</p>
	<p>3. \${headerValues["cookie"][1]} => ${headerValues["cookie"][1]}</p>
	
	<h2>param:</h2>
	<p>1. \${param} => ${param}</p>
	<p>2. \${param.name} => ${param.name}</p>
	<p>3. \${param.languages} => ${param.languages}</p>
	
	<h2>paramValues:</h2>
	<p>1. \${paramValues} => ${paramValues}</p>
	<p>2. \${paramValues.name} => ${paramValues.name}</p>
	<p>3. \${paramValues.name["0"]} => ${paramValues.name["0"]}</p>
	<p>4. \${paramValues.languages} => ${paramValues.languages}</p>
	<p>5. \${paramValues.languages[0]} => ${paramValues.languages[0]}</p>
	<p>6. \${paramValues.languages["1"]} => ${paramValues.languages["1"]}</p>

</body>
</html>
