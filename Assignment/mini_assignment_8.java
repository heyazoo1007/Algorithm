import java.util.Scanner;

public class Assignment {

    public static void main(String[] args) {

        System.out.println("[과세금액 계산 프로그램]");
        System.out.print("연소득을 입력해 주세요.:");
        Scanner sc = new Scanner(System.in);
        Integer money = Integer.parseInt(sc.nextLine());

        int[] standard = {12000000, 34000000, 42000000, 62000000, 150000000, 200000000, 500000000, 1000000000};
        double[] rate = {0.06, 0.15, 0.24, 0.35, 0.38, 0.40, 0.42, 0.45};

        int answer = 0;
        for (int i = 0; i < standard.length; i++) {
            if (money >= standard[i]) {
                answer += standard[i] * rate[i];
                System.out.printf("%d * %d", standard[i], (int)(rate[i] * 100));
                System.out.print("% =");
                System.out.printf("%10d", (int)(standard[i] * rate[i]));
                System.out.println();
                money -= standard[i];

            } else if (money < standard[i] && money > 0) {
                answer += money * rate[i];
                System.out.printf("%d * %d", money, (int)(rate[i] * 100));
                System.out.print("% =");
                System.out.printf("%10d", (int)(money * rate[i]));
                System.out.println();
                money = 0;
            }
        }
        System.out.println();
        System.out.printf("[세율에 의한 세금]: %17d" , answer);
        System.out.println();
        System.out.printf("[누진공제 계산에 의한 세금]: %10d", answer);
    }
}
