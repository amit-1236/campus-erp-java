# College ERP (MVP)

[![Repository](https://img.shields.io/badge/GitHub-campus--erp--java-blue?logo=github)](https://github.com/amit-1236/campus-erp-java)

A lightweight College Enterprise Resource Planning (ERP) web application built using **Java Servlets**, **JSP**, **JSTL**, and **MySQL**. The system provides Role-Based Access Control (RBAC) for Administrators, Teachers, and Students to streamline academic and administrative workflows.

- **Repository**: [https://github.com/amit-1236/campus-erp-java](https://github.com/amit-1236/campus-erp-java)

---

## 📌 Features

### 🔐 Authentication & Security
- **Role-Based Authentication**: Supports 3 distinct user roles — `ADMIN`, `TEACHER`, and `STUDENT`.
- **Session-Based Access Control**: Protected routes guarded by a servlet filter (`AuthFilter`).
- **Secure Session Invalidation**: Complete session logout with automatic cleanup.
- **Resource Leak Prevention**: Custom `AppContextListener` for deregistering JDBC drivers and terminating MySQL cleanup threads on shutdown.

### 👑 Administrator Module
- **Admin Dashboard**: Centralized management panel.
- **Student Management**: View all registered students with linked user profiles, enrollment numbers, courses, and semesters.

### 👨‍🏫 Teacher Module
- **Teacher Dashboard**: Streamlined dashboard for daily operations.
- **Attendance Tracking**: Mark and record daily attendance (`PRESENT` / `ABSENT`) for students.

### 🎓 Student Module
- **Student Dashboard**: Portal for students to access academic notices, view attendance status, and check enrolled details.

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| **Language** | Java 11 |
| **Backend Framework** | Java EE (Servlet API 4.0.1, JSP API 2.3.3, JSTL 1.2) |
| **Database** | MySQL 8.0+ |
| **JDBC Driver** | MySQL Connector/J 8.0.30 |
| **Build & Dependency Tool** | Apache Maven 3.x |
| **Application Server** | Apache Tomcat 8.5+ / Tomcat 9 / Embedded Tomcat 7 Maven Plugin |

---

## 📂 Project Structure

```text
college-erp-mvp/
├── pom.xml                               # Maven project dependencies and build plugins
├── database.sql                          # MySQL database schema and initial seed data
├── generate_code.py                      # Code generator utility script
├── README.md                             # Project documentation
└── src/
    └── main/
        ├── java/
        │   └── com/
        │       └── collegeerp/
        │           ├── dao/              # Data Access Objects (JDBC queries)
        │           │   ├── AttendanceDAO.java
        │           │   ├── StudentDAO.java
        │           │   └── UserDAO.java
        │           ├── model/            # Plain Old Java Objects (Entities)
        │           │   ├── Student.java
        │           │   └── User.java
        │           ├── util/             # Utility classes
        │           │   └── DBConnection.java
        │           └── web/              # Servlets, Listeners, and Filters
        │               ├── AppContextListener.java
        │               ├── AttendanceServlet.java
        │               ├── AuthFilter.java
        │               ├── DashboardServlet.java
        │               ├── LoginServlet.java
        │               ├── LogoutServlet.java
        │               └── StudentServlet.java
        └── webapp/                       # Web resources and views
            ├── assets/
            │   └── style.css             # Application stylesheet
            ├── admin/
            │   ├── dashboard.jsp         # Admin dashboard view
            │   └── students.jsp          # Student list view
            ├── teacher/
            │   └── dashboard.jsp         # Teacher dashboard and attendance form
            ├── student/
            │   └── dashboard.jsp         # Student portal view
            └── login.jsp                 # Login page
```

---

## 🗄️ Database Setup

1. **Start MySQL Server**: Ensure MySQL service is running on your machine.
2. **Execute Schema & Seed Script**:
   Import `database.sql` into MySQL:
   ```bash
   mysql -u root -p < database.sql
   ```
3. **Database Schema Details**:
   - `users`: Stores user credentials, full name, and role (`ADMIN`, `TEACHER`, `STUDENT`).
   - `students`: Stores student-specific records (`enrollment_no`, `course`, `semester`) linked to `users`.
   - `attendance`: Stores daily attendance logs (`date`, `status: PRESENT/ABSENT`) linked to `students`.

4. **Verify Database Configuration**:
   Open [`src/main/java/com/collegeerp/util/DBConnection.java`](src/main/java/com/collegeerp/util/DBConnection.java) and update credentials if needed:
   ```java
   private static final String URL = "jdbc:mysql://localhost:3306/college_erp";
   private static final String USER = "root";
   private static final String PASSWORD = "password"; // <-- Update with your MySQL password
   ```

---

## 🚀 Getting Started

### Prerequisites
- **JDK 11** or higher installed (`java -version`)
- **Apache Maven 3.6+** installed (`mvn -version`)
- **MySQL 8.0+** running locally

### 1. Clone & Navigate to Project
```bash
git clone https://github.com/amit-1236/campus-erp-java.git
cd campus-erp-java
```

### 2. Build the Project
Compile classes and package the application into a `.war` file:
```bash
mvn clean package
```

### 3. Run the Application

#### Option A: Run with Maven Tomcat Plugin (Recommended for Development)
Run directly from terminal using the configured embedded Tomcat plugin:
```bash
mvn tomcat7:run
```
Once started, access the application in your browser at:
```
http://localhost:8080/college-erp/login.jsp
```

#### Option B: Deploy to Standalone Apache Tomcat
1. Build the WAR:
   ```bash
   mvn clean package
   ```
2. Copy `target/college-erp-mvp-1.0-SNAPSHOT.war` (or rename to `college-erp.war`) into your Tomcat `webapps/` directory.
3. Start Tomcat (`bin/startup.sh` or `bin/startup.bat`).
4. Access via:
   ```
   http://localhost:8080/college-erp/login.jsp
   ```

---

## 🔑 Default Credentials

The database script initializes an administrator account:

| Role | Username | Password |
|---|---|---|
| **Admin** | `admin` | `admin123` |

> Additional teachers and students can be seeded in the `users` and `students` tables via SQL or created through the application.

---

## 🛣️ API & Route Endpoints

| Endpoint | HTTP Method | Access | Description |
|---|---|---|---|
| `/login.jsp` | `GET` | Public | Login interface |
| `/login` | `POST` | Public | Authenticates credentials and redirects based on role |
| `/logout` | `GET` | Authenticated | Invalidates session and redirects to login |
| `/admin/dashboard` | `GET` | `ADMIN` | Admin home dashboard |
| `/admin/students` | `GET` | `ADMIN` | Displays table of all registered students |
| `/teacher/dashboard` | `GET` | `TEACHER` | Teacher home dashboard |
| `/teacher/attendance` | `POST` | `TEACHER` | Records attendance for a student on a specific date |
| `/student/dashboard` | `GET` | `STUDENT` | Student home dashboard |

---

## 🔮 Future Enhancements

- [ ] **Password Security**: Introduce BCrypt hashing instead of plain text storage.
- [ ] **Full Student CRUD**: Add web forms for creating, updating, and deleting student records.
- [ ] **Attendance Reports**: Monthly/semester attendance percentage calculator for students.
- [ ] **Marks & Examination Module**: Grade entry, marksheet generation, and GPA calculation.
- [ ] **Fee Management**: Fee structure configuration, fee payment history, and receipt generation.
- [ ] **Modern UI**: Enhanced dashboard with modern responsive UI and charting library.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) (or academic project use).
