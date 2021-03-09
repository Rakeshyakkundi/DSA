import java.util.Scanner;
class SquareRoot{
    public static void main(String args[]){ 
        System.out.print("Enter a number: ");  
        Scanner sc = new Scanner(System.in);  
        int n = sc.nextInt();  
        System.out.println("The square root of "+ n+ " is: "+squareRoot(n));  

    }

    public static double squareRoot(int n){ 
        int i; 
        for(i=1;i<n;i++){
            if(i*i==n) return i;
            if(i*i>n) return i-1;
        }
        return i;
    //    double t;
    //    double squareroot=n/2;
    //    do{
    //        t=squareroot;
    //        squareroot=(squareroot+(n/t))/2;
    //    }while((t-squareroot)!=0);
    //    return squareroot;
    }
}