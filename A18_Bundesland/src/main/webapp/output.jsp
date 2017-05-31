<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<link rel="stylesheet" type="text/css" href="style.css">
		<title>Politische Bildung</title>
	</head>
	<body>
	<h1>Politische Bildung JSP</h1>
	<h2><c:out value="${typeOfOutput}" /></h2>
	<c:forEach items="${output}" var="item">
		<p><c:out value="${item}" /> </p>
	</c:forEach>
	<br>
	<a href="${pageContext.request.contextPath}">Let's start again...</a>
	</body>
</html>