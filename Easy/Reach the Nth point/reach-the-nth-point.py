#User function Template for python3

class Solution:
	def nthPoint(self,n):
		# Code here
		m=10**9+7
		dp=[1,2]
		if n<=2:
		    return dp[n-1]
		for i in range(2,n):
		    dp.append((dp[i-1]%m+dp[i-2]%m)%m)
		return dp[n-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthPoint(n)
		print(ans)
# } Driver Code Ends