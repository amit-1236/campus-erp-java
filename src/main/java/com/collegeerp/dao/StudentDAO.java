package com.collegeerp.dao;

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
