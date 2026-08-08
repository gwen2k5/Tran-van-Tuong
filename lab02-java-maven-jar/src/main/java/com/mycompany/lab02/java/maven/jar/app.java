/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.lab02.java.maven.jar;
import java.util.Scanner;

/**
 *
 * @author tranv
 */
public class app {
      public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Nhap ma sinh vien: ");
        String studentId = scanner.nextLine();

        System.out.print("Nhap ho ten sinh vien: ");
        String fullName = scanner.nextLine();

        double attendanceScore =
                inputScore(scanner, "diem chuyen can");

        double midtermScore =
                inputScore(scanner, "diem giua ky");

        double finalScore =
                inputScore(scanner, "diem cuoi ky");

        student student = new student(
                studentId,
                fullName,
                attendanceScore,
                midtermScore,
                finalScore
        );

        double totalScore =
                GradeCalculator.calculateFinalScore(student);

        String grade =
                GradeCalculator.classify(totalScore);

        System.out.println("\n----- KET QUA HOC PHAN -----");

        System.out.println("Ma SV: "
                + student.getStudentId());

        System.out.println("Ho ten: "
                + student.getFullName());

        System.out.printf("Diem tong ket: %.2f%n",
                totalScore);

        System.out.println("Xep loai: "
                + grade);

        scanner.close();
    }
       private static double inputScore(
            Scanner scanner,
            String label) {

        while (true) {

            try {

                System.out.print("Nhap " + label + ": ");

                double score =
                        Double.parseDouble(scanner.nextLine());

                GradeCalculator.validateScore(
                        score,
                        label
                );

                return score;

            } catch (IllegalArgumentException ex) {

                System.out.println(
                        "Loi: " + ex.getMessage()
                );
            }
        }
    }
    
}
