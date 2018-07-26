/**
 * A demo is on (ideone)[https://ideone.com/45e3uk]
 */
public class CheckPolymorphism {
    public static void main(String[] args) {
        A a = new B();
        System.out.println(a.name); // Super-A
        System.out.println(a.getName()); // Child-B
        
        B b = new B();
        System.out.println(b.name); // Child-B        
        System.out.println(b.getName()); // Child-B
        
    }
}


class A{
    String name = "Super-A";

    public String getName() {
        return name;
    }
    
    
}

class B extends A{
    String name = "Child-B";

    @Override
    public String getName() {
        return name;
    }
    
}
