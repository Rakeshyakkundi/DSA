// import java.util.Scanner ;

// class Pattern{
//     public static void main(String args[]){
//         int num=5;
//         // Scanner sc = new Scanner(System.in);
//         // System.out.println("Enter number for line :");
//         // num = sc.nextInt();
//         for(int i=0; i<num;i++){
//             for(int j=0;j<num-i;j++){
//                 System.out.print(" ");
//             }
//             for(int k=0;k<=i;k++){
//                 System.out.print("*");
//             }
            
//             System.out.println("\n");
//         }
//     }
// }

// import java.util.Scanner ;

// class Pattern{
//     public static void main(String args[]){
//         int num=5;
//         // Scanner sc = new Scanner(System.in);
//         // System.out.println("Enter number for line :");
//         // num = sc.nextInt();
//         int number;
//         number=1;
//         for(int i=0; i<num;i++){
//             for(int j=0;j<num-i+1/2;j++){
//                 System.out.print(" ");
//             }
//             for(int k=0;k<=i;k++){
//                 System.out.print(" "+(number)+" ");
//                 number ++;
//             }
//             for(int l=0;l<num-i+1/2;l++){
//                 System.out.print(" ");
//             }
//             System.out.println("");
//         }
//     }
// }

// import java.util.Scanner ;

// class Pattern{
//     public static void main(String args[]){
//         int num=5,l=0,number=2;
//         for(int i=0; i<num+num;i++){
//             if(l<=9){
//             for(int j=0;j<i;j++){
//                 System.out.print("*");
//                 l =l+1;
//             }}else{
//             for(int k=num-number-1;k>=0;k--){
//                 System.out.print("*");
//             }
//             number = number +1;
//         }
//             System.out.println(" ");
//         }
//     }
// }

import java.util.Scanner ;

class Pattern{
    public static void main(String args[]){
        int num1=0,num2=0,num3=0;
        for(int i=0;i<=5;i++){
            if(i==0 || i==5 || i==1){
            for(int j=0;j<i+1;j++){
                System.out.print("*");
            }}
            else if(i !=0 || i != 5 || i != 1){
                
                for(int j=0;j<i+1;j++){
                System.out.print(i);
                 }
                for(int j=0;j<i+1;j++){
                System.out.print(i);
                 }
                for(int j=0;j<i+1;j++){
                System.out.print(i);
                 }
            }
            System.out.println();
        }
    }
}
