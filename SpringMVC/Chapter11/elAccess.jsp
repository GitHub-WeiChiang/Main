<%@ page contentType="text/html;charset=UTF-8"%>
<%@ page import="java.util.*"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<html>
	<head>
		<title>JSP EL Access</title>
	</head>
	<body>
		<h2>Test variable:</h2>
		<p>1. \${myNum} => ${myNum}</p>
		<p>2. \${myStr} => ${myStr}</p>
	
		<h2>Test Java bean:</h2>
		<p>1. \${emp1.address.location} => ${emp1.address.location}</p>
		<p>2. \${emp1.address["location"]} => ${emp1.address["location"]}</p>
	
		<h2>Test Map:</h2>
		<p>1. \${myMap} => ${myMap}</p>
		<p>2. \${myMap["emp1"].name} => ${myMap["emp1"].name}</p>
		<p>3. \${myMap.emp1.name} => ${myMap.emp1.name}</p>
		<p>4. \${myMap[myStr].name} => ${myMap[myStr].name}</p>
	
		<h2>Test List:</h2>
		<p>1. \${myList} => ${myList}</p>
		<p>2. \${myList["0"].name} => ${myList["0"].name}</p>
		<p>3. \${myList[0].name} => ${myList[0].name}</p>
		<p>4. \${myList[myNum].name} => ${myList[myNum].name}</p>
	
		<h2>Test Array:</h2>
		<p>1. \${myArray} => ${myArray}</p>
		<p>2. \${myArray["0"].name} => ${myArray["0"].name}</p>
		<p>3. \${myArray[0].name} => ${myArray[0].name}</p>
		<p>4. \${myArray[myNum].name} => ${myArray[myNum].name}</p>
	
		<h2>Test NotFound:</h2>
		<p>1. \${myListX} => ${myListX}</p>
		<p>2. \${myList["5"].name} => ${myList["5"].name}</p>
		<p>3. \${myList["0"].nameX} => javax.el.PropertyNotFoundException: Property 'nameX' not found on type course.c06.Employee</p>
		<p>4. \${empX.address.location} => ${empX.address.location}</p>
		<p>5. \${myMap.empX.name} => ${myMap.empX.name}</p>
		<p>6. \${myArray[X].name} => ${myArray[X].name}</p>	
		<p>7. \${myArray["X"].name} => java.lang.NumberFormatException: For input string: "X"</p>
	</body>
</html>