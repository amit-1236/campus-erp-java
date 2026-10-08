package com.collegeerp.web;

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
