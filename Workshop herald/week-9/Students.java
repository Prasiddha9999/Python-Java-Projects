import java.util.*;
public class Students
{
    public static void main(String []args){
        Std one=new Std("Sam");
        Std two=new Std();
        one.student();
        two.student();       
    }
}
    class Std{
        String name;
        Std(){
            this.name="Unknown";
        }
        Std(String name){
            this.name=name;
        }
        void student(){
            System.out.println("Your name is "+this.name);
        }
        
}
