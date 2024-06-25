import java.util.Scanner;

public class Main {
    static int N, S;
    static int[] arr;
    static int count = 0;
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        N = sc.nextInt();
        S = sc.nextInt();
        arr = new int[N];
        
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        
        sc.close();
        
        find(0, 0);
        

        if (S == 0) {
            count--;
        }
        
        System.out.println(count);
    }
    
    static void find(int index, int sum) {
        if (index == N) {
            if (sum == S) {
                count++;
            }
            return;
        }
        
        // 현재 원소를 포함하지 않음
        find(index + 1, sum);
        
        // 현재 원소를 포함
        find(index + 1, sum + arr[index]);
    }
}
