#User function Template for python3

class Solution:
    def smallestSubstring(self, S):
        # Code here
        p=[len(S)+1]*3
        mn=len(S)+1
        for i in range(len(S)):
            p[ord(S[i])-48]=i
            mn=min(mn,max(p)-min(p)+1)
        if p[0]!=(len(S)+1) and p[1]!=(len(S)+1) and p[2]!=(len(S)+1):
            return mn
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends