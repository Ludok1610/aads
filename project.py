def trees(n, m):
    left=3
    right=n

    def check(k):
        for i in range(m):
            types=set()
            for j in range(k):
                types.add((i+j)%m)
            if len(types)<3:
                return False
        return True

    while left<right:
        mid=(left+right)//2
        if check(mid):
            right=mid
        else:
            left=mid+1
    return left

# tr=trees(100, 85)
# print(tr)