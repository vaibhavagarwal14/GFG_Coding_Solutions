//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

void isPrime(int n) {
    int f=0;
    for (int i = 2; i <= sqrt(n); i++) {
        // code here
        if(n%i==0)
        {
            f=1;
        }
    }
    if(f==1 || n==1)
    {
        cout<<"No";
    }
    else
    {
        cout<<"Yes";
    }
cout << endl;
}

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        isPrime(n);
    }
    return 0;
}
// } Driver Code Ends