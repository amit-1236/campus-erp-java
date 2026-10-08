package com.collegeerp.web;

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
