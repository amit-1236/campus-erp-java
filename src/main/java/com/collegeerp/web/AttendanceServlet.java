package com.collegeerp.web;

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
