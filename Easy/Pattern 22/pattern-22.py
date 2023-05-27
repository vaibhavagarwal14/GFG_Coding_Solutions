#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N,0,-1):
            for j in range(N,i-1,-1):
                print(j,end=' ')
            for j in range(1,i):
                print(i,end=' ')
            for j in range(2,i):
                print(i,end=' ')
            for j in range(i-1,N):
                if(i==1 and j==0):
                    pass
                else:
                    print(j+1,end=' ')
            print()
        for i in range(1,N):
            for j in range(N,i,-1):
                print(j,end=' ')
            for j in range(i):
                print(i+1,end=' ')
            for j in range(1,i):
                print(i+1,end=' ')
            for j in range(i,N):
                print(j+1,end=' ')
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