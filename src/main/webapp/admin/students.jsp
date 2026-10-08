<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<html>
<head><title>Manage Students</title><link rel="stylesheet" href="../assets/style.css"></head>
<body>
    <div class="dashboard">
        <h2>Student List</h2>
        <table border="1">
            <tr><th>ID</th><th>Name</th><th>Enrollment No</th><th>Course</th></tr>
            <c:forEach var="student" items="${students}">
                <tr>
                    <td>${student.id}</td>
                    <td>${student.fullName}</td>
                    <td>${student.enrollmentNo}</td>
                    <td>${student.course}</td>
                </tr>
            </c:forEach>
        </table>
        <br><a href="dashboard">Back</a>
    </div>
</body>
</html>
