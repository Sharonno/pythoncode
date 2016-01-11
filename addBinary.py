
def containsNearbyDuplicate(nums, k):
    dic = {}
    for i, v in enumerate(nums):
        if v in dic and i - dic[v] <= k:
            return True
        dic[v] = i
    return False


if __name__ == '__main__':
    num = [2,2]
    k = 3
    print containsNearbyDuplicate(num,k)