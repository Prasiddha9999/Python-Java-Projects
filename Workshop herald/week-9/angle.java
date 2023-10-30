
import java.util.*;
public class angle
{
     public static void main(String[] args){
        ArrayList<Square> al = new ArrayList();
        for(int i=0; i<10;i++){
            al.add(new Square(i+1));
        }
        for (Square ob : al){
            ob.area();
        }
    }
}
class Rectangle{
    int length;
    int breadth;
    
    Rectangle(int length, int breadth){
        this.length = length;
        this.breadth = breadth;
    }
    
    void area(){
        System.out.println("Area is "+ (this.length*this.breadth));
    }
}

class Square extends Rectangle{
    Square(int s){
        super(s,s);
    }
}
    

