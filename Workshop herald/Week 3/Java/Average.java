public class Average{
    public static int multiple( int a, int b, int c, int d, int e)
    {
     int mean = (a+b+c+d+e)/5;
     return(mean);
    }
    public static void main(String[] args){
    int num1=3;
    int num2=4;
    int num3=5; 
    int num4=6; 
    int num5=7;
    int men = multiple(num1, num2, num3, num4, num5);
    System.out.println("The mean of five number is "+men);
    
    }
    
}