# User function Template for python3
class Solution:

    def equilibrium(self, arr, n):

        def prefixar(arr):

            prefix = [0 for i in range(n)]

            prefix[0] = arr[0]

            for i in range(1, n):
                prefix[i] = arr[i]+prefix[i-1]

            return prefix

        prefix = prefixar(arr)

        s = sum(arr)

        for i, j in enumerate(prefix):
            if i+1 < n and j == s-arr[i+1]-j:
                return 'YES'

        return 'NO'
    # code here

# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.equilibrium(a, n)
        print(ans)
        tc = tc-1
# } Driver Code Ends
