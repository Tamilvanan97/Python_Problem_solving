class solutions :

    def __init__(self):
        self.nums=list(map(int, input("enter a self.nums: ").split()))
        self.removeDuplicates(self.nums)

    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        count=1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count+=1
        print(nums[:count])
        print(count)
        
solutions()