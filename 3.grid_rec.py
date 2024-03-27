#time complexity is O(2^(n+m))
#space complexity is O(n+m)
def grid(n,m):
    if (m==1 and n==1):
        return 1
    if (m==0 or n==0):
        return 0
    return grid(n-1,m)+grid(n,m-1)
print(grid(2,3))