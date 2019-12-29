class Variable
{
    public static void main(String[] args) {
        int a=10;
        float b=a;
        System.out.println(a);
        System.out.println(b);


        float f=10.5f;
        int i=(int)f;//TypeCasting
        System.out.println(f);
        System.out.println(i);


        int ii=130;
        byte bb=(byte)ii;//Overflow Because the above ii is > than byte dataType
        System.out.println(ii);
        System.out.println(bb);


        //byte c=a+b;//Compile Time Error: because a+b=20 will be int 
        //Adding Lower Type
        byte g=10;
        byte h=10;
        byte s=(byte)(g+h);
        System.out.println(s);

    }
}