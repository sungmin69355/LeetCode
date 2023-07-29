class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> bracketsMap = new HashMap<Character, Character>(){{
            put(')', '(');
            put('}', '{');
            put(']', '[');
         
        }};
        
        Stack<Character> stack = new Stack<Character>();
        for (char c : s.toCharArray()) {
            if (bracketsMap.containsKey(c)) {
                // 현재 문자가 닫는 괄호인 경우
                if (stack.isEmpty() || stack.pop() != bracketsMap.get(c)) {
                    return false; // 스택이 비어있거나 짝이 맞지 않는 경우
                }
            } else {
                stack.push(c); // 여는 괄호인 경우 스택에 추가
            }
        }
        return stack.isEmpty(); // 스택이 비어있다면 모든 괄호가 짝이 맞는 경우
    }
}