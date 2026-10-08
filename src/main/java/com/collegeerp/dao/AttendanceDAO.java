package com.collegeerp.dao;

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
