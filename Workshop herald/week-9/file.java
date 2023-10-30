
public class file
{
 public static void main(String []args){
     parent p=new parent();
     Child c=new Child();
     p.parentmethod();
     c.childmethod();
     c.parentmethod();
}
}
class parent{
    void parentmethod(){
        System.out.println("This is parent method");
    }
}
class Child extends parent{
    void childmethod(){
        System.out.println("This is child method");
    }
}

        

        
