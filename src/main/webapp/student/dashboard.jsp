<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head><title>Student Dashboard</title><link rel="stylesheet" href="../assets/style.css"></head>
<body>
    <div class="dashboard">
        <h2>Welcome Student: ${sessionScope.user.fullName}</h2>
        <p>View your attendance and marks here.</p>
        <a href="${pageContext.request.contextPath}/logout">Logout</a>
    </div>
</body>
</html>
