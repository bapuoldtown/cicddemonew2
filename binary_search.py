from typing import List
def binary_search(nums: List, item: int):
    l=0
    r=len(nums) - 1
    
    while l < r:
        mid = (l+r)//2
        if nums[mid] == item:
            return True
        if nums[mid] < item:
            l = mid+1
        if nums[mid] > item:
            r=mid-1
    return False

if __name__ == '__main__':
    print(binary_search([1,2,3,4,5], -4))