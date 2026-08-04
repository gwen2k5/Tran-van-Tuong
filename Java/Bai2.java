import java.util.Scanner;

public class Bai2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap n so nguyen duong: ");
        int n = sc.nextInt();

        double s = 0;
        for (int i = 1; i <= n; i++) {
            s += 1.0 / i;
        }

        System.out.println("tong s = 1 + 1/2 + ... + 1/" + n + " = " + s);
    }
}