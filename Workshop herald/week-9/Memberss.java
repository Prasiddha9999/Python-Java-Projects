
public class Memberss{
    public static void main(String[] args){
        Employee e = new Employee("Manish", 20, 127000, "Kathmandu", 20000, "enginner");
        Manager m = new Manager("Rahul", 30, 127000, "Kathmandu", 200000, "IT");
        e.displayInfo();
        System.out.println("\n\n");
        m.displayInfo();
    }
}
class Member{
    String name;
    int age;
    int phno;
    String Address;
    int salary;
    
    Member(String name, int age, int phno, String Address, int salary){
        this.name = name;
        this.age = age;
        this.phno = phno;
        this. Address = Address;
        this.salary = salary;
    }
    void displayInfo(){
        System.out.println("Name "+name);
        System.out.println("Age "+age);
        System.out.println("Phone number "+phno);
        System.out.println("Address "+Address);
        System.out.println("Salary "+salary);
    }
    
    void printSalary(){
        System.out.println("Salary is "+salary);
    }
}
class Employee extends Member{
    String specialization;
    Employee(String name, int age, int phno, String Address, int salary, String specialization){
        super(name, age, phno, Address, salary);
        this.specialization = specialization;
    }
    void displayInfo(){
        super.displayInfo();
        System.out.println("Specialization: "+specialization);
    }
}
class Manager extends Member{
    String department;
     Manager(String name, int age, int phno, String Address, int salary, String department){
        super(name, age, phno, Address, salary);
        this.department = department;
    }
      void displayInfo(){
        super.displayInfo();
        System.out.println("Department: "+department);
    }
}