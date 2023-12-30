#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        mp={}
        for i in arr:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]= 1
        a1=arr[0]
        a2=mp[arr[0]]
        for i,j in zip(mp.keys(), mp.values()):
            if j>a2:
                a2=j
                a1=i
            elif j==a2:
                if i<a1:
                    a1=i
                    a2=j
        return [a1,a2]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
# } Driver Code Ends