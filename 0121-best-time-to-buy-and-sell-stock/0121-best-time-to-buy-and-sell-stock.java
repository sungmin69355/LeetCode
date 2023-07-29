class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length < 2) {
            return 0; // 주식 가격이 없거나 1개 뿐이라면 이익이 없으므로 0을 반환
        }

        int maxProfit = 0;
        int minPrice = prices[0]; // 첫 번째 가격을 최소 가격으로 초기화

        for (int i = 1; i < prices.length; i++) {
            // 현재 가격과 최소 가격을 비교하여 최소 가격 업데이트
            minPrice = Math.min(minPrice, prices[i]);
            // 현재 가격에서 최소 가격을 뺀 이익과 최대 이익을 비교하여 갱신
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);
        }

        return maxProfit;
    }
}