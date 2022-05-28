public class BinarySearch{
    public static void main(String[] args){

        int myArray[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};
        int first = 0;
        int last = myArray.length;
        int guess = 10;


        while(first <= last){
            int mid = (first + last) / 2;

            if (myArray[mid] == guess){
                System.out.println(mid);
                break;
            }
            if (myArray[mid] > guess)
                    last = mid - 1;
            if (myArray[mid] < guess)
                first = mid + 1;
        }
    }
}