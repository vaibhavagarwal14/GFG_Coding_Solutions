#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        # code here
        val={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=0
        i=0
        while i<len(S):
            if i+1<len(S):
                if val[S[i]]>=val[S[i+1]]:
                    res+=val[S[i]]
                    i+=1
                else:
                    res+=val[S[i+1]]-val[S[i]]
                    i+=2
            else:
                res+=val[S[i]]
                i+=1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends