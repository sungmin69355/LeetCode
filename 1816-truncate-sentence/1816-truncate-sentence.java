class Solution {
    public String truncateSentence(String s, int k) {
        String[] str = s.split(" ");
        String result = "";
        
        result+= str[0];
        for(int i = 1; i<k;i++) {
            result+= " "+str[i];
        }
        return result;
    }
}