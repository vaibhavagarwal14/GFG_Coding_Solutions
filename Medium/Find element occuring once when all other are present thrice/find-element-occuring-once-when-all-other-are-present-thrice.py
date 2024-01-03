#User function Template for python3

class Solution:
    def singleElement(self, arr, N):
        # code here 
        arr.sort()
        if N==1:
            return arr[0]
        if arr[0]!=arr[1]:
            return arr[0]
        for i in range(1,N-1):
            if arr[i-1]!=arr[i] and arr[i]!=arr[i+1]:
                return arr[i]
        return arr[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.singleElement(arr,N))
# } Driver Code Ends