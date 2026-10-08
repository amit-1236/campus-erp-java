package com.collegeerp.model;

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
