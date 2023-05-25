#User function Template for python3

class Solution:
    def printDiamond(self, N):
        # Code here
        for i in range(N):
            for j in range(N-1-i):
                print(end=' ')
            for j in range(i+1):
                print('*',end=' ')
            print()
        for i in range(N):
            for j in range(i):
                print(end=' ')
            for j in range(N-i):
                print('*',end=' ')
            print()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printDiamond(N)
# } Driver Code Ends