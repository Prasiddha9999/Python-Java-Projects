public class Stud
{
    String name;
    int roll_no;
    public static void main(String[]args){
        Stud objects = new Stud();
        objects.name="John";
        objects.roll_no=2;
        System.out.println("Name of student is " + objects.name);
        System.out.println("Roll no. of "+objects.name+" is "+objects.roll_no);
    } 
}
