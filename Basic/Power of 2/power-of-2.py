#User function Template for python3

class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        ##Your code here
        if n==0:
            return 0
        if n==1:
            return 1
        i=1
        while i<n:
            i*=2
        return i==n


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        if ob.isPowerofTwo(n):
            print("YES")
        else:
            print("NO")
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends