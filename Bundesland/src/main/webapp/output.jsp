<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>Politische Bildung</title>
	</head>
	<body>
	<h1>Politische Bildung JSP</h1>
	<h2><c:out value="${typeOfOutput}" /></h2>
	<ul>
		<c:forEach items="${output}" var="item">
			<li><c:out value="${item}" /> </li>
		</c:forEach>
	</ul>
	</body>
</html>