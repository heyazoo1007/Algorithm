import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class Assignment {

    public static void main(String[] args) {

        System.out.println("[로또 당첨 프로그램]");
        System.out.print("로또 개수를 입력해 주세요.(숫자 1 ~ 10):");
        Scanner sc = new Scanner(System.in);
        Integer number = Integer.parseInt(sc.nextLine());

        Random random = new Random();

        int[][] numberList = new int[number][6];
        for (int i = 0; i < number; i++) {
            System.out.printf("%c   ", (char)(i + 65));
            for (int j = 0; j < 6; j++) {
                numberList[i][j] = random.nextInt(45) + 1;
                for (int k = 0; k < j; k++) {
                    if (numberList[i][k] == numberList[i][j]) {
                        j--;
                    }
                }
            }
            Arrays.sort(numberList[i]);
            System.out.printf("%02d,%02d,%02d,%02d,%02d,%02d", numberList[i][0], numberList[i][1], numberList[i][2], numberList[i][3], numberList[i][4], numberList[i][5]);
            System.out.println();
        }

        System.out.println();
        System.out.println("[로또 발표]");
        int[] answer = new int[6];
        for (int i = 0; i < 6; i++) {
            answer[i] = random.nextInt(45) + 1;
            for (int j = 0; j < i; j++) {
                if (answer[j] == answer[i]) {
                    i--;
                }
            }
        }
        Arrays.sort(answer);
        System.out.printf("   %02d,%02d,%02d,%02d,%02d,%02d", answer[0], answer[1], answer[2], answer[3], answer[4], answer[5]);
        System.out.println();

        System.out.println();
        System.out.println("[내 로또 결과]");
        for (int i = 0; i < number; i++) {
            int count = 0;
            for (int j = 0; j < 6; j++) {
                for (int k = 0; k < 6; k++) {
                    if (numberList[i][j] == answer[k]) {
                        count += 1;
                    }
                }
            }
            System.out.printf("%c  %02d,%02d,%02d,%02d,%02d,%02d", (char)i + 65, numberList[i][0], numberList[i][1], numberList[i][2], numberList[i][3], numberList[i][4], numberList[i][5]);
            System.out.printf(" => %d개 일치", count);
            System.out.println();
        }
    }
}
