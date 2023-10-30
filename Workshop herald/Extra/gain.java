public class Gain
{
    public static void main(String[] args) {
        String name = System.console().readLine("What is your name?");
        String answer = System.console().readLine("How many times?");
        int num = Integer.parseInt(answer);
        for(int i=1; i<=num; i++){
        System.out.println("Hello"+name);
        }
    }
}