/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.lab02.java.maven.jar;

/**
 *
 * @author tranv
 */
public class GradeCalculator {
     public static double calculateFinalScore(student student) {

        return student.getAttendanceScore() * 0.10
                + student.getMidtermScore() * 0.30
                + student.getFinalScore() * 0.60;
    }

    public static String classify(double score) {

        if (score >= 8.5) {
            return "A";
        }

        if (score >= 7.0) {
            return "B";
        }

        if (score >= 5.5) {
            return "C";
        }

        if (score >= 4.0) {
            return "D";
        }

        return "F";
    }

    public static void validateScore(double score, String fieldName) {

        if (score < 0 || score > 10) {
            throw new IllegalArgumentException(
                    fieldName + " phai nam trong khoang 0 den 10"
            );
        }
    }
 }

