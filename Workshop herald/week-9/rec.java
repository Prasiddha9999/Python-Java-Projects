import java.util.*;
class rec{
    int length;
    int breadth;
    rec(int length, int breadth){
        this.length = length;
        this.breadth = breadth;
    }
    void area(){
        System.out.println("Area is "+ (length*breadth));
    }
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
class Square extends rec{
    Square(int s){
        super(s,s);
    }
}