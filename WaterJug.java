public class WaterJug{
    public static void main(String[] args) {
        int steps = 0;
        int[] state = {0,0};
        int m = 4;
        int n = 3;
        int target = 2;

        while(true){

            printState(state);

            if(steps>=m*n){
                System.out.println("Cannot be Solved");
                break;
            }

            if(state[0] == target || state[1] == target){
                System.out.println("Solved -> "+steps);
                break;
            }

            else if(state[0] == 0){
                state[0] = m;
                steps++;
            }

            else if(state[1] == n){
                state[1] = 0;
                steps++;
            }
            
            else{
                pour(state,m,n);
                steps++;
            }
        }
    }

    static void pour(int[] state,int m,int n){
        if(state[0] >= n){
            int toBePoured = n - state[1];
            state[0] -= toBePoured;
            state[1] += toBePoured;
        }
        else{
            int toBePoured = state[0];
            state[0] = 0;
            state[1] = toBePoured;
        }
    }

    static void printState(int[] state){
        System.out.print("["+state[0]+","+state[1]+"]");
        System.out.println();
    }
}