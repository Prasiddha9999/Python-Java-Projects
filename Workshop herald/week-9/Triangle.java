public class Triangle
{
   int len,bre,hei;
   int areaval, perimeterval;
   int area(int length, int breadth, int height){
        this.len = length;
        this.bre = breadth;
        this.hei = height;
        areaval = 12*len*bre*hei;
        return areaval;
    }
   int perimeter(int length, int breadth, int height){
        this.len = length;
        this.bre = breadth;
        this.hei = height;
        perimeterval = len + bre + hei;
        return perimeterval;
    }
   public static void main(String[] args){
        Triangle t = new Triangle();
        int area = t.area(3,4,5);
        int peri = t.perimeter(3,4,5);
        System.out.println("The area is: "+area);
        System.out.println("The perimeter is: " +peri);
    }
}