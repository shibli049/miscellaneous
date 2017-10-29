/**
 * A demo is on (ideone)[https://ideone.com/45e3uk]
 */
public class CheckPolymorphism {
    public static void main(String[] args) {
        A a = new B();
        System.out.println(a.name);
        System.out.println(a.getName());
        
        B b = new B();
        System.out.println(b.name);        
        System.out.println(b.getName());
        
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