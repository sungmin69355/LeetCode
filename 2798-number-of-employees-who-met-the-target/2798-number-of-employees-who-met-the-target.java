class Solution {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int result = 0;
        
        for(int i : hours) {
            if(i >= target) result+=1;   
        }
        
        return result;
    }
}