class IFCONDITION
{
    public static void main(String[] args) {
        // int age=20;
        // if(age>18){
        //     System.out.println("YOU ARE THE MAJOR");
        // }
        // if(age%2==0){
        //     System.out.println("Even");
        // }
        // else{
        //     System.out.println("ODD");
        // }



        int year=2008;
        if(((year%4==0)&(year%100==0))||(year%4==0)){
            System.out.println("LeapYear");

        }
        else{
            System.out.println("Not a leapYear");
        }
    }
}