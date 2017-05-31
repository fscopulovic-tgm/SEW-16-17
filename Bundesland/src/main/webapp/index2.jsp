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
	<h1>Wähle ein Bundesland aus!</h1> 
	<br>
	<label> Lerne dein Land kennen! </label> 
	<br>
		<form action="Select.do" id="wish">
			<label> Bundesland:
				<select name="wishState" id="wishSelected" size="3">
					<c:forEach items="${ouput}" var="item">
						<option value="${item}"><c:out value="${item}" /> </option>
					</c:forEach>
				</select>
			</label>
			<br>
			<button type="submit">Submit!</button>
		</form>
	</body>
</html>