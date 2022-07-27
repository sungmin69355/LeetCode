class Solution {
    public boolean isSubsequence(String s, String t) {
        if(s.length() == 0) return true;
        if(t.length() == 0) return false;
        
        int len = 0;
        
        for(int i =0; i<t.length();i++){
            if(s.charAt(len) == t.charAt(i)){
                len +=1;
                if(len >=s.length()) return true;
            }
        }
        return false;
    }
}