package Quicksort;

public class qsort {
    
    public static void qsort1(int elements[], int left, int right){
        if (left < right){
            int pos = divide(elements, left, right);
            qsort1(elements, left, pos-1);
            qsort1(elements, pos+1, right);                                                       
        }
    }

    public static int divide(int elements[], int left, int right){
        int p = elements[right];
        int i = left;
        int j = right-1;

        while(true){
            while(elements[i] <= p && i<right){
                i = i+1;
            }
            while(elements[j] >= p && j>left){
                j = j-1;
            }
            if (i<j){
                swap(elements, i, j);
            }
            if(i>=j){
                break;
            }
        }
        swap(elements, i, right);
        return i;
    }

    public static void swap(int elements[], int i, int j){
        int tmp = elements[i];
        elements[i] = elements[j];
        elements[j] = tmp;
    }
    public static void main(String[] args){                                                                                                                                                                                                                                                                                     
        int test[] = {88, 56, 100, 2, 25, 20, 19};
        qsort1(test, 0, 6);
        for (int element : test){
            System.out.println(element);
        }
    }
}
