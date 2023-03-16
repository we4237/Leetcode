from typing import List


# class Solution:
#     def finalPrices(self, prices: List[int]) -> List[int]:
#         n = len(prices)
#         ans = [0]*n
#         for i,p in enumerate(prices):
#             discount = 0
#             for j in range(i+1 , n):
#                 if prices[j]<=p:
#                     discount = prices[j]
#                     break
#             ans[i] = p - discount
#         return ans

# 单调栈
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0]*n
        st=[0]
        for i in range(n-1,-1,-1):
            p = prices[i]
            while len(st)>1 and st[-1] > p: #当前栈顶的元素大于prices[i]
                st.pop()
            ans[i]=p-st[-1]
            st.append(p) # 将price[i]压入栈中,保证prices[i]位当前栈的最大值
        return ans
