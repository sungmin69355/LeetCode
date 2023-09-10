class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int start=0; int end =0; //포인트 시작,끝
        int n = nums.length;
        int[] result = new int[n-k+1];
        int x = 0;
        Deque<Integer> deque = new ArrayDeque<>();
        while(end<n) {
            //deque가 비어있지않고 마지막 요소가 현재 요소보다 작아질 때까지 Deque에서 요소를 제거
            while(!deque.isEmpty() && nums[deque.peekLast()] < nums[end]) {
                deque.pollLast();
            }
            deque.addLast(end);
            if(end-start+1>k) {
                if (nums[start] == nums[deque.peekFirst()]) {
                    deque.removeFirst();
               }
               start++;
            }

           if(end - start + 1 == k) {
               result[x++] = nums[deque.peekFirst()];
           }
            end++;
        }
        return result;
    }
}