class Solution:
    def __init__(self):
        nums=list(map(int,input("enter a list: ").split()))
        target=int(input("enter a value: "))
        self.twosum(nums,target)

    def twosum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    print([i,j])
                    
Solution()