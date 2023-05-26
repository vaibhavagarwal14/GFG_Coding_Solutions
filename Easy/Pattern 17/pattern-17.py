#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N):
            for j in range(N-1,i,-1):
                print(end=' ')
            for j in range(i+1):
                print(chr(j+65),end='')
            for j in range(i-1,-1,-1):
                print(chr(j+65),end='')
            print()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends