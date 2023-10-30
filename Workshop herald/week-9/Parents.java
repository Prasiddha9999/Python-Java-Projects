public class Parents
{
    void parent(){
        System.out.println("This is Parent Class");
    }
    public static void main (String[] args){
        Parents p = new Parents();
        Child c = new Child();
        p.parent();
        c.child();
        c.parent();
        System.out.println(" ");
    }
} class Child extends Parents
{
    void child(){
        System.out.println("This is Child Class");
    }
}