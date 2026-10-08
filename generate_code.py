import os

base_dir = "/home/amit/Documents/ram/gec/college-erp-mvp"

files = {
    "database.sql": """CREATE DATABASE IF NOT EXISTS college_erp;
USE college_erp;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('ADMIN', 'TEACHER', 'STUDENT') NOT NULL,
    full_name VARCHAR(100) NOT NULL
);

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    enrollment_no VARCHAR(20) NOT NULL UNIQUE,
    course VARCHAR(50),
    semester INT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    date DATE NOT NULL,
    status ENUM('PRESENT', 'ABSENT') NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);

INSERT INTO users (username, password, role, full_name) VALUES ('admin', 'admin123', 'ADMIN', 'System Admin');
""",

    "pom.xml": """<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.collegeerp</groupId>
    <artifactId>college-erp-mvp</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>war</packaging>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
    </properties>

    <dependencies>
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>javax.servlet.jsp</groupId>
            <artifactId>javax.servlet.jsp-api</artifactId>
            <version>2.3.3</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>jstl</groupId>
            <artifactId>jstl</artifactId>
            <version>1.2</version>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.30</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.2</version>
            </plugin>
        </plugins>
    </build>
</project>
""",

    "src/main/java/com/collegeerp/util/DBConnection.java": """package com.collegeerp.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBConnection {
    private static final String URL = "jdbc:mysql://localhost:3306/college_erp";
    private static final String USER = "root";
    private static final String PASSWORD = "password";

    public static Connection getConnection() throws SQLException, ClassNotFoundException {
        Class.forName("com.mysql.cj.jdbc.Driver");
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }
}
""",

    "src/main/java/com/collegeerp/model/User.java": """package com.collegeerp.model;

public class User {
    private int id;
    private String username;
    private String password;
    private String role;
    private String fullName;

    // Getters and Setters
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }
    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }
    public String getRole() { return role; }
    public void setRole(String role) { this.role = role; }
    public String getFullName() { return fullName; }
    public void setFullName(String fullName) { this.fullName = fullName; }
}
""",

    "src/main/java/com/collegeerp/model/Student.java": """package com.collegeerp.model;

public class Student {
    private int id;
    private int userId;
    private String enrollmentNo;
    private String course;
    private int semester;
    private String fullName; // from User table

    // Getters and Setters
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    public int getUserId() { return userId; }
    public void setUserId(int userId) { this.userId = userId; }
    public String getEnrollmentNo() { return enrollmentNo; }
    public void setEnrollmentNo(String enrollmentNo) { this.enrollmentNo = enrollmentNo; }
    public String getCourse() { return course; }
    public void setCourse(String course) { this.course = course; }
    public int getSemester() { return semester; }
    public void setSemester(int semester) { this.semester = semester; }
    public String getFullName() { return fullName; }
    public void setFullName(String fullName) { this.fullName = fullName; }
}
""",

    "src/main/java/com/collegeerp/dao/UserDAO.java": """package com.collegeerp.dao;

import com.collegeerp.model.User;
import com.collegeerp.util.DBConnection;
import java.sql.*;

public class UserDAO {
    public User login(String username, String password) {
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE username=? AND password=?")) {
            ps.setString(1, username);
            ps.setString(2, password);
            ResultSet rs = ps.executeQuery();
            if (rs.next()) {
                User user = new User();
                user.setId(rs.getInt("id"));
                user.setUsername(rs.getString("username"));
                user.setRole(rs.getString("role"));
                user.setFullName(rs.getString("full_name"));
                return user;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }
}
""",

    "src/main/java/com/collegeerp/dao/StudentDAO.java": """package com.collegeerp.dao;

import com.collegeerp.model.Student;
import com.collegeerp.util.DBConnection;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class StudentDAO {
    public List<Student> getAllStudents() {
        List<Student> students = new ArrayList<>();
        try (Connection conn = DBConnection.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery("SELECT s.*, u.full_name FROM students s JOIN users u ON s.user_id = u.id")) {
            while (rs.next()) {
                Student s = new Student();
                s.setId(rs.getInt("id"));
                s.setUserId(rs.getInt("user_id"));
                s.setEnrollmentNo(rs.getString("enrollment_no"));
                s.setCourse(rs.getString("course"));
                s.setSemester(rs.getInt("semester"));
                s.setFullName(rs.getString("full_name"));
                students.add(s);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return students;
    }
}
""",

    "src/main/java/com/collegeerp/dao/AttendanceDAO.java": """package com.collegeerp.dao;

import com.collegeerp.util.DBConnection;
import java.sql.*;

public class AttendanceDAO {
    public void markAttendance(int studentId, String date, String status) {
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement("INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)")) {
            ps.setInt(1, studentId);
            ps.setDate(2, Date.valueOf(date));
            ps.setString(3, status);
            ps.executeUpdate();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
""",

    "src/main/java/com/collegeerp/web/LoginServlet.java": """package com.collegeerp.web;

import com.collegeerp.dao.UserDAO;
import com.collegeerp.model.User;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;

@WebServlet("/login")
public class LoginServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        User user = new UserDAO().login(request.getParameter("username"), request.getParameter("password"));
        if (user != null) {
            request.getSession().setAttribute("user", user);
            response.sendRedirect(request.getContextPath() + "/" + user.getRole().toLowerCase() + "/dashboard");
        } else {
            response.sendRedirect("login.jsp?error=1");
        }
    }
}
""",

    "src/main/java/com/collegeerp/web/LogoutServlet.java": """package com.collegeerp.web;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;

@WebServlet("/logout")
public class LogoutServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.getSession().invalidate();
        response.sendRedirect("login.jsp");
    }
}
""",

    "src/main/java/com/collegeerp/web/DashboardServlet.java": """package com.collegeerp.web;

import com.collegeerp.model.User;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;

@WebServlet({"/admin/dashboard", "/teacher/dashboard", "/student/dashboard"})
public class DashboardServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        User user = (User) request.getSession().getAttribute("user");
        request.getRequestDispatcher("/" + user.getRole().toLowerCase() + "/dashboard.jsp").forward(request, response);
    }
}
""",

    "src/main/java/com/collegeerp/web/StudentServlet.java": """package com.collegeerp.web;

import com.collegeerp.dao.StudentDAO;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;

@WebServlet("/admin/students")
public class StudentServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setAttribute("students", new StudentDAO().getAllStudents());
        request.getRequestDispatcher("/admin/students.jsp").forward(request, response);
    }
}
""",

    "src/main/java/com/collegeerp/web/AttendanceServlet.java": """package com.collegeerp.web;

import com.collegeerp.dao.AttendanceDAO;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;

@WebServlet("/teacher/attendance")
public class AttendanceServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        int studentId = Integer.parseInt(request.getParameter("studentId"));
        String date = request.getParameter("date");
        String status = request.getParameter("status");
        new AttendanceDAO().markAttendance(studentId, date, status);
        response.sendRedirect(request.getContextPath() + "/teacher/dashboard");
    }
}
""",

    "src/main/java/com/collegeerp/web/AuthFilter.java": """package com.collegeerp.web;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.*;
import java.io.IOException;

@WebFilter("/*")
public class AuthFilter implements Filter {
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        HttpServletRequest req = (HttpServletRequest) request;
        HttpServletResponse res = (HttpServletResponse) response;
        String uri = req.getRequestURI();
        
        if (uri.endsWith("login.jsp") || uri.endsWith("/login") || uri.contains("/assets/")) {
            chain.doFilter(request, response);
            return;
        }
        
        HttpSession session = req.getSession(false);
        if (session == null || session.getAttribute("user") == null) {
            res.sendRedirect(req.getContextPath() + "/login.jsp");
        } else {
            chain.doFilter(request, response);
        }
    }
}
""",

    "src/main/webapp/login.jsp": """<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Login - College ERP</title>
    <link rel="stylesheet" href="assets/style.css">
</head>
<body>
    <div class="login-container">
        <h2>College ERP Login</h2>
        <form action="${pageContext.request.contextPath}/login" method="post">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
""",

    "src/main/webapp/assets/style.css": """body { font-family: Arial, sans-serif; background: #f4f4f4; margin: 0; padding: 20px; }
.login-container { max-width: 300px; margin: 100px auto; background: #fff; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 3px; }
button { width: 100%; padding: 10px; background: #28a745; color: white; border: none; border-radius: 3px; cursor: pointer; }
button:hover { background: #218838; }
.dashboard { background: #fff; padding: 20px; border-radius: 5px; }
""",

    "src/main/webapp/admin/dashboard.jsp": """<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head><title>Admin Dashboard</title><link rel="stylesheet" href="../assets/style.css"></head>
<body>
    <div class="dashboard">
        <h2>Welcome Admin: ${sessionScope.user.fullName}</h2>
        <a href="students">Manage Students</a> | <a href="${pageContext.request.contextPath}/logout">Logout</a>
    </div>
</body>
</html>
""",

    "src/main/webapp/admin/students.jsp": """<%@ page contentType="text/html;charset=UTF-8" language="java" %>
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
""",

    "src/main/webapp/teacher/dashboard.jsp": """<%@ page contentType="text/html;charset=UTF-8" language="java" %>
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
""",

    "src/main/webapp/student/dashboard.jsp": """<%@ page contentType="text/html;charset=UTF-8" language="java" %>
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
"""
}

for rel_path, content in files.items():
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    print(f"Written: {rel_path}")
