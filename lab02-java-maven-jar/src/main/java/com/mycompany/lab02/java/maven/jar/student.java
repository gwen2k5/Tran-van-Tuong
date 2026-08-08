/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.lab02.java.maven.jar;

/**
 *
 * @author tranv
 */
public class student {
      private String studentId;
    private String fullName;
    private double attendanceScore;
    private double midtermScore;
    private double finalScore;

    public student(String studentId, String fullName,
                   double attendanceScore, double midtermScore,
                   double finalScore) {

        this.studentId = studentId;
        this.fullName = fullName;
        this.attendanceScore = attendanceScore;
        this.midtermScore = midtermScore;
        this.finalScore = finalScore;
    }

    public String getStudentId() {
        return studentId;
    }

    public String getFullName() {
        return fullName;
    }

    public double getAttendanceScore() {
        return attendanceScore;
    }

    public double getMidtermScore() {
        return midtermScore;
    }

    public double getFinalScore() {
        return finalScore;
    }
    
}
