import java.util.*;

public class removedupl {
   
    public static ArrayList<Integer> removeduplicates(ArrayList<Integer> elements){
        ArrayList<Integer> solution = new ArrayList<>();

        for (int ele : elements){
            boolean dupl = false;
            for(int sol : solution){
                if(ele == sol){
                    dupl = true;
                    continue;
                }
            }
            if(dupl == false){
                solution.add(ele);
            }
        }
        return solution;
    }

    public static void main(String[] args){
        ArrayList<Integer> test = new ArrayList<>();
        test.add(1);
        test.add(2);   
        test.add(2);   
        test.add(3);                                                                                                                                                                                                                                                                                               
        System.out.println(removeduplicates(test));
    }
}

