class Operators
{
    public static void main(String[] args) {
        int a = 10;
        // System.out.println(a);
        //Java Unary Operator Example: ++ and --
        System.out.println(a++);
        System.out.println(++a);
        System.out.println(a--);
        System.out.println(--a);

        


        //Java Unary Operator Example: ~ and !
        int b=-10;  
boolean c=true;  
boolean d=false;
System.out.println(a++ + ++a);//10+12=22  
System.out.println(b++ + b++);//10+11=21 

//Java Unary Operator Example 2: ++ and --
System.out.println(~a);//-11 (minus of total positive value which starts from 0)  
System.out.println(~b);//9 (positive of total minus, positive starts from 0)  
System.out.println(!c);//false (opposite of boolean value)  
System.out.println(!d);//true  


//Java Arithmetic Operator Example
System.out.println(a+b);//15  
System.out.println(a-b);//5  
System.out.println(a*b);//50  
System.out.println(a/b);//2  
System.out.println(a%b);//0  



//Java Left Shift Operator Example
System.out.println(10<<2);//10*2^2=10*4=40  
System.out.println(10<<3);//10*2^3=10*8=80  
System.out.println(20<<2);//20*2^2=20*4=80  
System.out.println(15<<4);//15*2^4=15*16=240  



//Java Right Shift Operator Example
System.out.println(10>>2);//10/2^2=10/4=2  
System.out.println(20>>2);//20/2^2=20/4=5  
System.out.println(20>>3);//20/2^3=20/8=2  



//Java AND Operator Example: Logical && and Bitwise &
int g=20;  
System.out.println(a<b&&a<g);//false && true = false  
System.out.println(a<b&a<g);//false & true = false  


//Java Ternary Operator Example


int aa=22;  
int bb=55;  
int min=(aa<bb)?aa:bb;  
System.out.println(min);  


    }
}