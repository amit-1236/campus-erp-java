<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head><title>Admin Dashboard</title><link rel="stylesheet" href="../assets/style.css"></head>
<body>
    <div class="dashboard">
        <h2>Welcome Admin: ${sessionScope.user.fullName}</h2>
        <a href="students">Manage Students</a> | <a href="${pageContext.request.contextPath}/logout">Logout</a>
    </div>
</body>
</html>
