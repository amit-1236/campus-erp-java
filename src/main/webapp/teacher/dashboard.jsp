<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head><title>Teacher Dashboard</title><link rel="stylesheet" href="../assets/style.css"></head>
<body>
    <div class="dashboard">
        <h2>Welcome Teacher: ${sessionScope.user.fullName}</h2>
        <form action="attendance" method="post">
            Student ID: <input type="number" name="studentId"><br>
            Date: <input type="date" name="date"><br>
            Status: <select name="status"><option value="PRESENT">Present</option><option value="ABSENT">Absent</option></select><br>
            <button type="submit">Mark Attendance</button>
        </form>
        <a href="${pageContext.request.contextPath}/logout">Logout</a>
    </div>
</body>
</html>
