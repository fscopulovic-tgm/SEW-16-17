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
	<h1>Wähle ein Bundesland aus!</h1> 
	<p> Lerne dein Land kennen! </p> 
	<p> Bundesland: </p>
	<form action="Select.do" id="wish">
			<select name="wishState" id="wishSelected" size="3">
				<c:forEach items="${output}" var="item">
					<option value="${item}"><c:out value="${item}" /> </option>
				</c:forEach>
			</select>
		<br>
		<button type="submit">Submit!</button>
	</form>
	</body>
</html>