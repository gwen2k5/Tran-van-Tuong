import java.util.Scanner;

public class Bai3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap so nguyen n: ");
        int n = sc.nextInt();

        if (kiemTraNguyenTo(n)) {
            System.out.println(n + " la so nguyen to");
        } else {
            System.out.println(n + " Khong phai la so nguyen to");
        }
    }

    static boolean kiemTraNguyenTo(int n) {
        if (n < 2) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}