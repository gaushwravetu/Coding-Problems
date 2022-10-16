import java.util.Scanner;
class UserInput {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter your name : ");
        String name = s.next();
        System.out.println("Enter age : ");
        int age = s.nextInt();
        System.out.println("Enter gender : ");
        char gender = s.next().charAt(0);
        System.out.println("Enter phone number : ");
        long phone = s.nextLong();

        System.out.println("...........................................");

        System.out.println("Your name : "+name);
        System.out.println("Your age : "+age);
        System.out.println("Your gender : "+gender);
        System.out.println("Your phone no : "+phone);


    }
}
