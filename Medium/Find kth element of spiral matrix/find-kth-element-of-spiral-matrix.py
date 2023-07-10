#User function Template for python3

class Solution:
    def findK(self, a, n, m, k):
        
        # Write Your Code here
        if (n < 1 or m < 1):
            return -1
        if (k <= m):
            return a[0][k - 1]
        if (k <= (m + n - 1)):
            return a[(k - m)][m - 1]
        if (k <= (m + n - 1 + m - 1)):
            return a[n - 1][m - 1 - (k - (m + n - 1))]
        if (k <= (m + n - 1 + m - 1 + n - 2)):
            return a[n - 1 - (k - (m + n - 1 + m - 1))][0]
        a.pop(0)
        [j.pop(0) for j in a]
        return self.findK(a, n - 2, m - 2, k - (2 * n + 2 * m - 4))

#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n, m, k = map(int,input().split())
    a = [
            list(map(int,input().split()))
            for _ in range(n)
        ]
    
    ob = Solution()
    print(ob.findK(a,n,m,k))
    
# } Driver Code Ends