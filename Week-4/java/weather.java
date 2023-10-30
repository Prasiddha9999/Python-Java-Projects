public class Main {
public static void main(String[] args) {
int temperature = 66;
int humidity = 50;
if (temperature >= 85 && humidity > 60) {
System.out.println("muggy day today");
}
else {
if (temperature >= 85) {
System.out.println("warm, but not muggy today");
}
else {
if (temperature >= 65) {
System.out.println("pleasant today");

}
else {
if (temperature <= 45) {
System.out.println("cold today");
}
else {
System.out.println("cool today");
}
}
}
}
}
}