import java.util.Arrays;
class MyArray {
    public static void main(String args[]){
        int[] arr={1,2,3,4,5};
        System.out.println(Arrays.toString(arr));
        for(int i=0;i<arr.length-1;i++){
            int temp = arr[0];
            for(int j=0;j<arr.length-1;j++){
                arr[j]=arr[j+1];
            }
            arr[arr.length-1]=temp;
            System.out.println(Arrays.toString(arr));
        }
    }
}