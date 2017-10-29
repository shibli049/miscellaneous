/**
A funny java program, takes input from user between 0 to 3 and call respective functions without using any conditional logic.
You can see the preview at (ideone)[https://ideone.com/JQclAE].
 */

import java.io.Serializable;
import java.util.Scanner;
import java.util.function.Supplier;

/**
 *
 * @author Shibli 
 */
public class FunFunctionExperiment {
    public static Integer f0(){
        return 0;
    }
    
    public static String f1(){
        return "Hello world!!";
    }
    
    public static Double f2(){
        return 2.0;
    }
    
    public static Long f3(){
        return Long.MAX_VALUE;
    }
    
    public static void main(String[] args) {
        Supplier<Serializable>[] suppliers = new Supplier[4];
        suppliers[0] = FunFunctionExperiment::f0;
        suppliers[1] = FunFunctionExperiment::f1;
        suppliers[2] = FunFunctionExperiment::f2;
        suppliers[3] = FunFunctionExperiment::f3;
        Scanner sc=new Scanner(System.in);
        do{
            System.out.print("n [0 <= n <= 3 ]: ");
            int n = sc.nextInt();
            if(n<0 || n>3){
                break;
            }
            System.out.println(suppliers[n].get());
        }while (true);
    }
}