def longestIncreasingSubsequence(arr, maxl=0, d={}):
    # Write your code here
    if(str(arr) in d):
        return d[str(arr)]
    res = [0]
    # ret = []
    for i in range(1, len(arr)):
        if arr[i] > arr[0]:
            # res+=longestIncreasingSubsequence(arr[i:],maxl)
            res.append(longestIncreasingSubsequence(arr[i:], maxl))
            if((max(res)+1) > maxl):
                maxl = max(res)+1
                # ret = res

    d[str(arr)] = (max(res)+1)
    return max(res)+1


print("hello", longestIncreasingSubsequence([2, 5, 3, 6, 2, 4, 5, 6]))
