package com.collegeerp.web;

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
