package Lab5Mutations;

/**
 * Hello world!
 *
 */
public class App 
{
    public Boolean isBigger(int a, int b){
        return a > b;
    }

    public Boolean isBigger2(int a, int b, int c){
        Boolean r1 = a > b;
        Boolean r2 = a > c;
        Boolean r3 = r1 && r2;
        return r3;
    }

    public Boolean isBigger3(int a, int b, int c, int d){
        Boolean r1 = a > b;
        Boolean r2 = a > c;
        Boolean r3 = a > d;
        Boolean r4 = r1 && r2 && r3;
        return r4;
    }


    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
}
