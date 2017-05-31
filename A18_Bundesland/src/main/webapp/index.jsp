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
	<h1>Wähle ein Thema aus!</h1>
	<p> Lerne dein Land kennen! </p>
	<p> Themen: </p>
		<form action="Select.do" id="wish">
			<select name="wishSelected" id="wishSelected" size="3">
				<option value="allCaptials">Alle Hauptstädte</option>
				<option value="federalStates">Alle Bundesländer</option>
				<option value="oneCapital">Eine Hauptstadt</option>
			</select>
			<br>
			<button type="submit">Submit!</button>
		</form>
	</body>
</html>