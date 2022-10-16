import java.util.Scanner;
public class calculator {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter 1st number: ");
        int num1 = s.nextInt();
        System.out.println("Enter 2nd number: ");
        int num2 = s.nextInt();
        System.out.println("Enter the operation : ");
        String oper = s.next();
        int res;
        switch (oper) {
            case "+":
                res = num1+num2;
                System.out.println("Result : "+res);
        }

    }
}
