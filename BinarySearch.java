import java.util.Arrays;
import java.io.*;
import java.util.Scanner;
class BinarySearch
{
    public static void main(String  args[]){
       int[] arr = {4,5,6,2,0,1,45};
       System.out.println("Array given :"+Arrays.toString(arr));
       for(int i=0;i<arr.length;i++){
            int temp;
            for(int j=i+1;j<arr.length;j++){
                if(arr[i]>arr[j]){
                    temp=arr[i];
                    arr[i]=arr[j];
                    arr[j]=temp;
                }
           }
       }
       System.out.println("Aranged array :"+Arrays.toString(arr));
       int num; 
       System.out.println("Enter the number to search: "); 
       Scanner s = new Scanner(System.in); 
       num = s.nextInt(); 
        int ini,mid,last;
        ini = 0;
        mid= arr.length/2;
        last=arr.length;
         while(ini<=last){
             if(num==arr[mid]){
                System.out.println("Number found in "+mid+" index");
                System.exit(0);
             }
             else if(num>arr[mid]){
                 ini = mid;
                 mid = (ini+last)/2;
             }
             else if(num<arr[mid]){
                 last = mid;
                 mid=(ini+last)/2;
             }
             
         }

       
    }
}